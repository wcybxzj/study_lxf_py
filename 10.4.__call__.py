# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print 'My name is %s' % self.name

s = Student('ybx')
s()

print callable(Student('ybx'))
print callable('string')
print callable(None)
