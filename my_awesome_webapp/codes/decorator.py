#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python

def b(func):
    def wrapper(*args, **kw):
        print 'b_func'
        return 'bbbbb' + func(*args, **kw) + 'bbbbb'
    return wrapper

def a(func):
    def wrapper(*args, **kw):
        print 'a_func'
        return 'aaaaa'+ func(*args, **kw) + 'aaaaa'
    return wrapper

def have_arg(p = '/'):
    def _decorator(func):
        print'在没调用函数之前就把此句执行了'
        return func
    return _decorator




#写法1:
@a
@b
@have_arg('me')
def c():
    return 'ccccc'

#写法2:
#c = b(c)
#c = a(c)

#写法3:
#c = a(b(c))

print 'before calling'
#print c()
