# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

class Fib(object):
    """a   b
       0   1
       1   1
       1   2
       2   3
       3   5"""
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10:
            raise StopIteration()
        return self.a

def run():
    #__iter__
    for n in Fib():
        print n,
    print

    #__getitem__
    f = Fib()
    print f[0],
    print f[1],
    print f[2]

    #__getitem__
    print f[0:3]

run()

