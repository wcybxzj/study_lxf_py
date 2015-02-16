# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'
"""
    __metaclass__ = ListMetaclass，
    在创建MyList时，要通过ListMetaclass.__new__()来创建，
    在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

    __new__()方法接收到的参数依次是：
    当前准备创建的类的对象；
    类的名字；
    类继承的父类集合；
    类的方法集合。
"""

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print cls  #<class '__main__.ListMetaclass'>
        print name  #Mylist
        attrs['add'] = lambda self, value : self.append(value)
        return type.__new__(cls, name, bases, attrs)

class Mylist(list):
    __metaclass__ = ListMetaclass

L = Mylist()
L.add(1)
print L