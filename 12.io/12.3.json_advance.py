# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


#通常class的实例都有一个__dict__属性，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class。
s = Student('Bob', 20, 88)
student_json = (json.dumps(s, default=lambda obj:obj.__dict__))
print student_json

student_obj = (json.loads(student_json, object_hook=dict2student))
print student_obj.name

