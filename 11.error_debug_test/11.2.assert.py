# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10/n

foo('1')