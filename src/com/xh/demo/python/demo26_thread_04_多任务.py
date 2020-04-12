'''
Title: 多任务
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
'''
import time
from multiprocessing import Process
from threading import Thread


def sing():
    for i in range(3):
        print("正在唱歌...", i)
        time.sleep(0.2)


def dance():
    for i in range(3):
        print("正在跳舞...", i)
        time.sleep(0.2)


def myProcess():
    p1 = Process(target=sing)
    p2 = Process(target=dance)
    p1.start()
    p2.start()


def myThread():
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == '__main__':
    # 进程跑
    myProcess()
    
    time.sleep(1)
    print()
    
    # 线程跑
    myThread() 
