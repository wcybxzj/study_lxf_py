# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'


class B(object):
    def method(self, str='good'):
        return str

class C(B):
    def method(self, arg='1111'):
        return super(C, self).method(arg)

obj_c = C()
print obj_c.method('ok123')
