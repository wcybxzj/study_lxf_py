# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'


class ClassOne(object):
    def fact(self, n):
        if n == 1:
            return 1
        return n * self.fact(n - 1)


obj = ClassOne()
print obj.fact(1000)