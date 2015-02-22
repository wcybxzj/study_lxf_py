# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'


# class B(object):
#     def method(self, str='good'):
#         return str
#
# class C(B):
#     def method(self, arg='1111'):
#         return super(C, self).method(arg)
#
# obj_c = C()
# print obj_c.method('ok123')


print '=========================================='
print '=========================================='
print '=========================================='


class Mammal(object):
    def say(self):
        print '妈妈'

class RunnableMixin(object):
    def say(self):
        print '跑跑'

class CarnivorousMixin(object):
    def say(self):
        print '肉肉'

class Dog(Mammal, RunnableMixin, CarnivorousMixin):
    def say(self):
        super(Dog, self).say()

obj = Dog()
print Dog.__mro__
obj.say()

print '=========================================='
print '=========================================='
print '=========================================='


