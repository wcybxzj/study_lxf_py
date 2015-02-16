__author__ = 'yangbingxi'


class Student(object):
    def __init__(self, name):
        self.name  = name

    def __str__(self):
        return 'this is str'
    #__repr__显示在命令行直接调用的返回结果
    __repr__ = __str__
s = Student('ybx')
print s