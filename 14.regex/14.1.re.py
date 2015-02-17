# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'
import re

class LearnRegex(object):
    def re(self):
        p = r'^\d{3}\-\d{3,8}$'
        result = re.match(p, '010-12345')

        if result:
            print 'ok'

    def split(self):
        #\s 可以匹配空格
        print 'a b    c'.split(' ')
        print re.split(r'\s+', 'a b    c')
        print re.split('[\s\,]+',  'a,b ,   c')
        print re.split('[\s\,\;]+',  'a,b;; ,   c')

    def group(self):
        m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
        print m.group(0)
        print m.group(1)
        print m.group(2)
        print m.groups()

    def greedy(self):
        print re.match(r'^(\d+)(0*)$', '102300').groups()
        print re.match(r'^(\d+?)(0*)$', '102300').groups()

    def complie(self):
        re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
        print re_telephone.match('010-12345').groups()
        print re_telephone.match('010-8086').groups()

    def run(self):
        self.re()
        self.split()
        self.group()
        self.greedy()
        self.complie()

obj = LearnRegex()
obj.run()