#!/usr/bin/env python
# -*- coding: utf-8 -*-

def a(func):
    def wrapper(*args, **kw):
        print 'aaaaa'
        return func(*args, **kw)
    return wrapper


def b(func):
    def wrapper(*args, **kw):
        print 'bbbbb'
        return func(*args, **kw)
    return wrapper

@a
@b
def c():
    print 'ccccc'

print 'before calling'
c()
