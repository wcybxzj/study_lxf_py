# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'
from collections import Iterable

class ClassOne:
    def for_dict(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        for k in d:
            print k,
        print

        for val in d.itervalues():
            print val,
        print

        for key, val in d.iteritems():
            print '%s --> %s' % (key, val) ,
        print

    def for_str(self):
        for ch in 'ABC':
            print ch,
        print

    def is_iterable(self):
        print isinstance('abc', Iterable)
        print isinstance([1, 2, 3], Iterable)
        print isinstance(123, Iterable)

    def for_list(self):
        for k, v in enumerate(['A', 'B', 'C']):
            print '%d - %s' % (k, v) ,

    def run(self):
        self.for_dict()
        self.for_str()
        self.is_iterable()
        self.for_list()


obj = ClassOne()
obj.run()