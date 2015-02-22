# -*- coding: utf-8 -*-
__author__ = 'yangbingxi'

class T(object):
    a = 0
class A(T):
    pass
class B(T):
    a = 2
class C(A,B):
    pass

c = C()
print C.__mro__
print c.a
print super(C, c).a

print '=========================================='
print '=========================================='
print '=========================================='


