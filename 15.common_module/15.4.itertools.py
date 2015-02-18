# -*- coding: utf-8 -*-
__author__ = 'yangbingxi'
import itertools

class ClassOne(object):
    '''itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，
        而是迭代对象，只有用for循环迭代的时候才真正计算。'''
    def count(self):
        #count()会创建一个无限的迭代器
        natuals = itertools.count(1)
        for n in natuals:
            print n

    def cycle(self):
        # 注意字符串也是序列的一种
        cs = itertools.cycle('ABC')
        for c in cs:
             print c

    def repeat(self):
        ns = itertools.repeat('A', 10)
        for n in ns:
             print n

    def takewhile(self):
        natuals = itertools.count(1)
        ns = itertools.takewhile(lambda x: x <= 10, natuals)
        for n in ns:
             print n

    def chain(self):
        for c in itertools.chain('ABC', 'XYZ'):
            print c,
        print

    def groupby(self):
        for key, group in itertools.groupby('AAABBBCCAAA'):
            print key, list(group)
        print

        for key, group in itertools.groupby('AaaBBbcCAAa', lambda c:c.upper()):
            print key, list(group)
        print

    def imap1(self):
        '''imap()可以作用于无穷序列，
            如果两个序列的长度不一致，以短的那个为准。'''
        for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], \
                                itertools.count(1)):
            print x




    def imap2(self):
        '''imap()返回一个迭代对象，而map()返回list。'''
        r = map(lambda x: x*x, [1, 2, 3])
        print r

        r = itertools.imap(lambda x: x*x, itertools.count(1))
        for n in itertools.takewhile(lambda x: x<100, r):
            print n,

        # r = map(lambda x: x*x, itertools.count(1))
        # for x in r:
        #     print x


    def run(self):
        #self.count()
        #self.cycle()
        #self.repeat()
        #self.takewhile()
        #self.chain()
        #self.groupby()
        #self.imap1()
        self.imap2()



obj = ClassOne()
obj.run()