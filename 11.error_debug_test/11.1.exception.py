# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

#抛出错误

# err.py
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        #可以直接抛出异常也可以修改异常类型发
        #raise ValueError('input error!')
        raise

def main():
    bar('0')

main()