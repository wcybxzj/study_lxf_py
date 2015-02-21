#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

class ClassOne(object):
    def test_one(self):
        return '测试获取函数名称'

    @classmethod
    def test_static(self):
        return 'three!!!'

    def run(self):
        print self.test_one
        print self.test_one.__name__
        print ClassOne.test_static()


class ClassTwo(object):
    def log1(func):
        def wrapper(*args, **kw):
            print '调用:%s():' %func.__name__
            return func(*args, **kw)
        return wrapper

    def log2(text):
        def decorator(func):
            def wrapper(*args, **kw):
                print '%s  调用:  %s():' % (text, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator

    def log3(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'call %s():' % func.__name__
            return func(*args, **kw)
        return wrapper

    def log4(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print '%s  调用:  %s():' % (text, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator

    @log1
    def func1(self):
        return '111111'

    @log2('日志内容2222')
    def func2(self):
        return '222222'

    @log3
    def func3(self):
        return '33333'

    @log4('日志内容4444')
    def func4(self):
        return '44444'

    def run(self):
        print self.func1()
        print self.func1.__name__
        print '====================='
        print self.func2()
        print self.func2.__name__
        print '====================='
        print self.func3()
        print self.func3.__name__
        print '====================='
        print self.func4()
        print self.func4.__name__
        print '====================='


obj = ClassOne()
obj.run()
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print ClassOne.test_static()
print ClassOne().test_static()
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
obj2 = ClassTwo()
obj2.run()
