'''
Title: 多线程同步锁02
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
'''
from multiprocessing import Lock
from threading import Thread
import time

num = 0
# 锁
lock1 = Lock()
# 创建一把锁, 并且锁上
lock2 = Lock()
lock2.acquire()
# 创建一把锁, 并且锁上
lock3 = Lock()
lock3.acquire()


class Task1(Thread):

    def run(self):
        while True:
            if lock1.acquire():
                print('--- Task1 ---')
                time.sleep(0.2)
                lock2.release()


class Task2(Thread):

    def run(self):
        while True:
            if lock2.acquire():
                print('--- Task2 ---')
                time.sleep(0.2)
                lock3.release()


class Task3(Thread):

    def run(self):
        while True:
            if lock3.acquire():
                print('--- Task3 ---')
                time.sleep(0.2)
                lock1.release()

                
if __name__ == '__main__':
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()

    t1.start()
    t2.start()
    t3.start()
