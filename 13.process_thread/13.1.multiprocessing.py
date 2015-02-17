# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'
from multiprocessing import Process
import os, time

def run(name):
    time.sleep(2)
    print '子进程 %s (%s)...' %\
          (name, os.getpid())

#创建子进程时，只需要传入一个执行函数和函数的参数，
#创建一个Process实例，用start()方法启动，比fork()简单。
#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run, args=('test',))
    print '开始'
    p.start()
    #p.join()
    print '如果写上join主进程就会等待，子进程的返回才会执行'
