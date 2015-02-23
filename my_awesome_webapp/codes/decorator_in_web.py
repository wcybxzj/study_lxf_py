#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types, os, re, cgi, sys, time, datetime, functools, mimetypes, threading, logging, urllib, traceback

ctx = threading.local()

class Dict(dict):
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


_RE_INTERCEPTROR_STARTS_WITH = re.compile(r'^([^\*\?]+)\*?$')
_RE_INTERCEPTROR_ENDS_WITH = re.compile(r'^\*([^\*\?]+)$')

def _build_pattern_fn(pattern):
    m = _RE_INTERCEPTROR_STARTS_WITH.match(pattern)
    if m:
        return lambda p: p.startswith(m.group(1))
    m = _RE_INTERCEPTROR_ENDS_WITH.match(pattern)
    if m:
        return lambda p: p.endswith(m.group(1))
    raise ValueError('Invalid pattern definition in interceptor.')

def interceptor(pattern='/'):
    def _decorator(func):
        print'在没调用函数之前就把此句执行了'
        func.__interceptor__ = _build_pattern_fn(pattern)
        return func
    return _decorator

def _build_interceptor_fn(func, next):
    def _wrapper():
        if func.__interceptor__(ctx.request.path_info):
            return func(next)
        else:
            return next()
    return _wrapper

def _build_interceptor_chain(last_fn, *interceptors):
    L = list(interceptors)
    L.reverse()
    fn = last_fn
    for f in L:
        fn = _build_interceptor_fn(f, fn)
    return fn

def target():
    print 'target'
    return 123

@interceptor('/')
def f1(next):
    print 'before f1()'
    return next()

@interceptor('/test/')
def f2(next):
    print 'before f2()'
    try:
        return next()
    finally:
        print 'after f2()'

@interceptor('/')
def f3(next):
    print 'before f3()'
    try:
        return next()
    finally:
        print 'after f3()'

if __name__ == '__main__':
    print 'before calling'
    # chain = _build_interceptor_chain(target, f1, f2, f3)
    # ctx.request = Dict(path_info='/test/abc')
    # chain()
    #before f1()
    #before f2()
    #before f3()
    #target
    #after f3()
    #after f2()
    #123

    # ctx.request = Dict(path_info='/api/')
    # chain()
    #before f1()
    #before f3()
    #target
    #after f3()
    #123
