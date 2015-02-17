# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'


d = dict(name='Bob', age=20, score=88)

try:
    import cPickle as pickle
except ImportError:
    import pickle

print pickle.dumps(d)

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)

print d