# -*- coding: utf-8 -*-
__author__ = 'yangbingxi'

import time, uuid, functools, threading, logging

class Dict(dict):
    '''
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y=200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
    AttributeError: 'Dict' object has no attribute 'empty'
    >>> d3 = Dict(('a', 'b', 'c'), (1, 2, 3))
    >>> d3.a
    1
    >>> d3.b
    2
    >>> d3.c
    3
    '''

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            msg_pattern = r"'Dict' object has no attribute '%s'"
            raise AttributeError(msg_pattern % key)

    def __setattr__(self, key, value):
        self[key] = value

def next_id(t=None):
    if t is None:
        t = time.time()
    return '%015d%s000' % (int(t * 1000), uuid.uuid4().hex)

def _profiling(start, sql=''):
    t = time.time()
    if t > 0.1:
        logging.warning('[PROFILING] DB %s: %s' % (t, sql))
    else:
        logging.info('[PROFILING] DB %s: %s' % (t, sql))

class DBError(Exception):
    pass

class MultiColumnsError(DBError):
    pass

# global engine object:
engine = None

# 数据库引擎对象:
class _Engine(object):

    def __init__(self, connect):
        self._connect = connect

    def connect(self):
        return self._connect()

def create_engine(user, password, database, host='127.0.0.1',
                  port=3306, **kw):
    import mysql.connector
    global engine
    if engine is not None:
        raise DBError('Engine is already initialized.')
    params = dict(user=user, password=password, database=database,
                  host=host, port=port)
    defaults = dict(use_unicode=True, charset='utf8',
                    collation='utf8_general_ci', autocommit=False)
    for k, v in defaults.iteritems():
        params[k] = kw.pop(k, v)
    params.update(kw)
    params['buffered'] = True
    engine = _Engine(lambda: mysql.connector.connect(**params))
    logging.info('Init mysql engine <%s> ok.' % hex(id(engine)))


class _LazyConnection(object):

    def __init__(self):
        self.connection = None

    def cursor(self):
        if self.connection is None:
            self.connection = engine.connect()
            logging.info('open connection <%s>...' % hex(id(self.connection)))
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def cleanup(self):
        if self.connection:
            connection = self.connection
            self.connection = None
            logging.info('close connection <%s>...' % hex(id(connection)))
            connection.close()


# 持有数据库连接的上下文对象:
class _DbCtx(threading.local):
    '''由于_db_ctx是threadlocal对象，
        所以，它持有的数据库连接对于每个线程看到的都是不一样的。
        任何一个线程都无法访问到其他线程持有的数据库连接。
    '''

    def __init__(self):
        self.connection = None
        self.transaction = 0

    def is_init(self):
        return not self.connection is None

    def init(self):
        logging.info('open lazy connection')
        self.connection = _LazyConnection()
        self.transactions = 0

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        return self.connection.cursor()


_db_ctx = _DbCtx()


class _ConnectionCtx(object):

    def __enter__(self):
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_cleanup = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()

class _TransactionCtx(object):

    def __enter__(self):
        global _db_ctx
        self.should_close_conn = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_close_conn = True
        _db_ctx.transactions = _db_ctx.transactions + 1
        msg = 'begin transaction...' \
            if _db_ctx.transactions == 1 else \
            'join current transaction'
        logging.info(msg)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        global _db_ctx
        _db_ctx.transactions = _db_ctx.transactions - 1
        try:
            if _db_ctx.transactions == 0:
                if exc_type is None:
                    self.commit()
                else:
                    self.rollback()
        finally:
            if self.should_close_conn:
                _db_ctx.cleanup()

    def commit(self):
        global _db_ctx
        logging.info('commit transaction...')
        try:
            _db_ctx.connection.commit()
            logging.info('commit ok')
        except:
            logging.warning('commit failed. try rollback...')
            _db_ctx.connection.rollback()
            logging.warning('rollback ok.')
            raise

    def rollback(self):
        global _db_ctx
        logging.warning('rollback transaction...')
        _db_ctx.connection.rollback()
        logging.info('rollback ok')



def connection():
    return _ConnectionCtx()


def with_connection(func):
    '''
    Decorator for reuse connection.

    @with_connetion
    def foo(*args, **kw):
        f1()
        f2()
        f3()
    '''
    @functools.wraps(func)
    def _wrapper(*args, **kw):
        with _ConnectionCtx():
            return func(*args, **kw)
    return _wrapper


def with_transaction(func):
    '''
    A decorator that makes function around transaction.

    >>> @with_transaction
    ... def update_profile(id, name, rollback):
    ...     u = dict(id=id, name=name, email='%s@test.org' % name, passwd=name, last_modified=time.time())
    ...     insert('user', **u)
    ...     r = update('update user set passwd=? where id=?', name.upper(), id)
    ...     if rollback:
    ...         raise StandardError('will cause rollback...')
    >>> update_profile(8080, 'Julia', False)
    >>> select_one('select * from user where id=?', 8080).passwd
    u'JULIA'
    >>> update_profile(9090, 'Robert', True)
    Traceback (most recent call last):
      ...
    StandardError: will cause rollback...
    >>> select('select * from user where id=?', 9090)
    []
    '''
    @functools.wraps(func)
    def _wrapper(*args, **kw):
        _start = time.time()
        with _TransactionCtx():
            return func(*args, **kw)
        _profiling(_start)
    return _wrapper

def _select(sql, first, *args):
    global _db_ctx
    cursor = None
    sql = sql.replace('?', '%s')
    logging.info('SQL: %s, ARGS: %s' % (sql, args))
    try:
        cursor = _db_ctx.connection.cursor()
        cursor.execute(sql, args)
        if cursor.description:
            names = [x[0] for x in cursor.description]
        if first:
            values = cursor.fetchone()
            if not values:
                return None
            return Dict(names, values)
        return [Dict(names, x) for x in cursor.fetchall()]
    finally:
        if cursor:
            cursor.close()

@with_connection
def select_one(sql, *args):
    return _select(sql, True, *args)

@with_connection
def select_int(sql, *args):
    d = _select(sql, True, *args)
    if len(d) != 1:
        raise MultiColumnsError('Expect only one column.')
    return d.values()[0]

@with_connection
def select(sql, *args):
    return _select(sql, False, *args)

@with_connection
def _update(sql, *args):
    global _db_ctx
    cursor = None
    sql = sql.replace('?', '%s')
    logging.info('SQL: %s, ARGS: %s' % (sql, args))
    try:
        cursor = _db_ctx.connection.cursor()
        cursor.execute(sql, args)
        r = cursor.rowcount
        if _db_ctx.transactions==0:
            logging.info('auto commit')
            _db_ctx.connection.commit()
        return r
    finally:
        if cursor:
            cursor.close()

def insert(table, **kw):
    cols, args = zip(*kw.iteritems())
    format_pattern = 'insert into `%s` (%s) values (%s)'
    cols_sql = ','.join(['`%s`' % col for col in cols])
    content_sql = ','.join(['?'  for c in cols])
    sql = format_pattern % (table, cols_sql, content_sql)
    return _update(sql, *args)

def update(sql, *args):
    return _update(sql, *args)

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG)
#     create_engine('root', 'root', 'test')
#     update('drop table if exists user')
#     update('create table user (id int primary key, '
#            'name text, email text, passwd text, last_modified real)')
#     import doctest
#     doctest.testmod()