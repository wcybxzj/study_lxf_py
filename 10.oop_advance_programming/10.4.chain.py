# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

class Chain(object):

    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    def __call__(self, args):
        return Chain('%s/:%s' % (self, args))

print Chain().status.user.timeline.list
print Chain().users('micheal').repo