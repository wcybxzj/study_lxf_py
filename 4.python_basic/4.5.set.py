# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'


class ClassOne(object):

    def one(self):
        mylist = [11,11, 22, 33]
        print set(mylist)

    def union(self):
        s1 = set([1, 2, 3])
        s2 = set([2, 3, 4])
        print s1 & s2

    def intersection(self):
        s1 = set([1, 2, 3])
        s2 = set([2, 3, 4])
        print s1 |s2

    def discuss_unchange_object(self):
        a = ['c', 'b', 'a']
        a.sort()
        print a

        # str is unchangable object
        a = 'abc'
        b = a.replace('a', 'A')
        print a
        print b

    def run(self):
        self.one()
        self.union()
        self.intersection()
        self.discuss_unchange_object()


obj = ClassOne()
obj.run()