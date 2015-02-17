# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'
import time, threading

def loop():
    print 'thread %s is running ...' % \
          threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % \
              (threading.current_thread().name, n)

        time.sleep(1)
    print 'thread %s ended.' % \
          threading.current_thread().name

#主线程实例的名字叫MainThread
print '主线程 %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='子进程')
t.start()
t.join()
print '主线程 %s is running...' % threading.current_thread().name