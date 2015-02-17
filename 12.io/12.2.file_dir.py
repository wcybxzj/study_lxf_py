# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'
import os
print os.path.split('/Users/michael/testdir/file.txt')

print os.path.splitext('/path/file.txt')

print [x for x in os.listdir('.') if os.path.isfile(x)]
print [x for x in os.listdir('.')
       if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']