#!/usr/bin/env python
# -*- coding: utf-8 -*-

class func_arg(object):

    def add_end_bug(self, L=[]):
        L.append('END')
        return L

    #默认参数必须指向不变对象
    def add_end_ok(self, L=None):
        if L is N   one:
            L = []
        L.append('END')
        return L

    def run(self):
        print self.add_end_bug([1, 2, 3])
        print self.add_end_bug(['x', 'y', 'z'])

        print self.add_end_bug()
        print self.add_end_bug()
        print self.add_end_bug()

        #wrong
        print self.add_end_ok()
        print self.add_end_ok()
        print self.add_end_ok()

obj = func_arg()
obj.run()
