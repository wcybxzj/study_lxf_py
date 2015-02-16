# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        elif attr == 'age':
            return lambda: 25

s = Student()
print s.score
print s.age()