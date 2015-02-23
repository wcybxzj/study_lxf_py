#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools, logging

class Template(object):
    def __init__(self, template_name, **kw):
        self.template_name = template_name
        self.model = dict(**kw)

def view(path):
    def _decorator(func):
        print '00000000000000000000000000000000000'
        @functools.wraps(func)
        def _wrapper(*args, **kw):
            print '11111111111111111111111111111111'
            r = func(*args, **kw)
            if isinstance(r, dict):
                return Template(path, **r)
            raise ValueError('Expect  @view() decorator.')
        return _wrapper
    return _decorator

def get(path):
    def _decorator(func):
        print '222222222222222222222222222222222222'
        func.__web_route__ = path
        func.__web_method__ = 'GET'
        return func
    return _decorator


#然后掉后这个
@view('test_users.html')
#先调用这个
@get('/')
def test_users():
    print 'tttttttttttttttttttttttttttttttttttttttt'
    return dict(users='ybx')

print 'before calling'
t = test_users()
print type(t)