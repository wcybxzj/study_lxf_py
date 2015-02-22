# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if not hasattr(cls, 'count'):
            cls.count = 0
        cls.count = cls.count + 1
        print cls.count
        print'+++++++++++++++++++++++++++++++++++++++++'
        print name
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v ,Field):
                print ('Found mapping: %s==>%s' %(k , v))
                mappings[k] = v

        #在我们编写的ORM中，ModelMetaclass会删除掉User类的所有类属性，目的就是避免造成混淆。
        for k in mappings.iterkeys():
            attrs.pop(k)

        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)

print '============================================'
print '定义class Model'

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            str = r"'Model' object has no attribute '%s'" % key
            raise AttributeError(str)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
            #args.append(self[k])

        sql = 'insert into %s (%s) values (%s)' % \
              (self.__table__, ','.join(fields), ','.join(params))

        print ('SQL: %s' % sql)
        print ('ARGS: %s' % str(args))

print '============================================'
print '定义class User'

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('pasword')

print '类中的继承关系:'
print User.__mro__

user_info = {'id':12345, 'name':'Michael',
               'email':'ybx@163.com', 'password':'123'}
print '============================================'
print '创建对象'
u = User(**user_info)
u.save()

