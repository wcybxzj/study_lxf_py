# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

class ClassOne(object):
    def list_and_generator(self):
        L = [x * x  for x in  range(10)]
        print L

        G = (x * x  for x in  range(10))
        print G

    def use_next(self):
        G = (x * x  for x in  range(10))
        print G.next(),
        print G.next(),
        print G.next(),

        for x in G:
            print x,
        print

    def fib(self, m):
        n, a, b = 0, 0, 1
        while n < m:
            print b,
            a, b  = b, a + b
            n = n + 1
        print

    def fib_generator(self, m):
        n, a, b = 0, 0, 1
        while n < m:
            yield b
            a, b  = b, a + b
            n = n + 1

    def generator_func(self):
        print 'step 1'
        yield 1
        print 'step 2'
        yield 3
        print 'step 3'
        yield 5

    def run(self):
        self.list_and_generator()
        self.use_next()

        self.fib(6)
        g = self.fib_generator(6)
        for x in g:
            print x,
        print

        g = self.generator_func()
        print g.next()
        print g.next()
        print g.next()


obj = ClassOne()
obj.run()
