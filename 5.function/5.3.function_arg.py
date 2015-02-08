#!/usr/bin/env python
# -*- coding: utf-8 -*-

class func_arg(object):

    def add_end_bug(self, L=[]):
        L.append('END')
        return L

    #默认参数必须指向不变对象
    def add_end_ok(self, L=None):
        if L is None:
            L = []
        L.append('END')
        return L

    def change_arg(self, *numbers):
        sum = 0
        for n in numbers:
            sum = sum + n *n
        return sum

    def key_word_arg(self, name, age, **kw):
        print 'name', name, 'age', age, 'kw', kw

    def assembly_arg(self, name, age, school='beida', *args, **kw):
        print 'name:', name, 'age:', age, 'school', school, 'args:', args, 'kw:',kw


    def run(self):
        #part 1 默认参数
        print self.add_end_bug([1, 2, 3])
        print self.add_end_bug(['x', 'y', 'z'])

        for i in range(3):
            print self.add_end_bug()

        for i in range(3):
            print self.add_end_ok()

        #part 2 可变参数
        #可以传入0->N 个参数
        print self.change_arg(2, 3, 4)
        print self.change_arg()
        nums = [1, 2, 3]
        print self.change_arg(*nums)

        #part 3 关键字参数
        self.key_word_arg('ybx', 22)
        self.key_word_arg('ybx', 22, city='Beijing')
        self.key_word_arg('ybx', 22, gender='male', job='doctor')
        key_word = {'hobby':'reading', 'friend':'jsk'}
        self.key_word_arg('ybx', 22, **key_word)

        #part 4组合参数
        self.assembly_arg('ybx', 18)
        self.assembly_arg('ybx', 18, '清华', 'aa', 'bb')
        self.assembly_arg('ybx', 18, '清华', 'aa', 'bb', hobby='reading book')

        args = (1, 2, 3, 4)
        kw = {'x':99}
        self.assembly_arg(*args, **kw)

        args = [11, 22, 33, 44]
        self.assembly_arg(*args, **kw)

obj = func_arg()
obj.run()
