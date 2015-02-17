# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print '名称:%s 子进程号:%s' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random())
    end = time.time()
    print 'Task %s runs %0.2f sconds' %\
          (name, (end-start))

#task 0，1，2，3是立刻执行的，task 4要等待前面某个task完成后才执行，
#这是因为Pool的默认大小在我的电脑上是4 cpu core，因此，最多同时执行4个进程。
#这是Pool有意设计的限制，并不是操作系统的限制。
#如果改成：Pool(5) 就会同时运行5个
if __name__ == '__main__':
    print 'parent process %s' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print '等待所有子进程的结束'
    p.close()
    p.join()
    print '所有子进程都结束了'