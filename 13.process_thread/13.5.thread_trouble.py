# -*- coding: utf-8 -*-
__author__ = 'wcybxzj'

import time, threading

balance = 0

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

def run_one():
    t1 = threading.Thread(target=run_thread, args=(5, ))
    t2 = threading.Thread(target=run_thread, args=(8, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print balance

run_one()



lock = threading.Lock()

balance = 0

def run_thread_ok(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

def run_ok():
    t1 = threading.Thread(target=run_thread_ok, args=(5, ))
    t2 = threading.Thread(target=run_thread_ok, args=(8, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print balance


run_ok()