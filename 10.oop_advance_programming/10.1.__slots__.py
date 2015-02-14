__author__ = 'yangbingxi'

class Student(object):
    pass

def set_age(self, age):
    self.age = age

#1.only add method in current object
from types import MethodType
s = Student()
s.set_age = MethodType(set_age, s, Student)
s.set_age(100)
print s.age

#2.add methodin class
def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student)
s.set_score(99)
print s.score