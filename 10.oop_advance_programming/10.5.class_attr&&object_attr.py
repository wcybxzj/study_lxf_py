# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

class Student(object):
    name = 'Student'

# 创建实例s：
s = Student()
print(s.name)
print(Student.name)

s.name = 'Michael'
print(s.name)
print(Student.name)

del s.name
print(s.name)
