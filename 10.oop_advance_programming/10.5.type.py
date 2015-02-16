# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

#example 1
class Hello(object):
    def hello(self, name = 'world'):
        print 'Hello, %s' % name


h = Hello()
h.hello()
#Hello是一个class，它的类型就是type
print type(Hello)
#h是一个实例，它的类型就是class Hello。
print type(h)


#example2
def fn(self, name='world'):
    print ('Hello, %s' % name)

Hello1 = type('Hello', (object, ),dict(hello=fn) )
h1 = Hello()
h1.hello()