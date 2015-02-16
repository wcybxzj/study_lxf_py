# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'


class Test(dict):
    def __init__(self, **kw):
        super(Test, self).__init__(**kw)

user_info = {'id':12345, 'name':'Michael',
               'email':'ybx@163.com', 'password':'123'}

t = Test(**user_info)
print t['email']