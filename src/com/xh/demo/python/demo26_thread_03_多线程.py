'''
Title: 多线程
Description: 

多线程共享全局变量，一个线程修改会影响另一个线程
    - 本案例最终计算结果应该是 2000, 但是结果不是!!!

@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
'''
from threading import current_thread, Thread

num = 0

def fun1():
    index = 1
    while index <= 1000:
        global num
        num = num+1
        print(num,"...", current_thread().name)
        index = index +1


def fun2():
    index = 1
    while index <= 1000:
        global num
        num = num + 1
        print(num, "...", current_thread().name)
        index = index + 1

if __name__ == '__main__':
    t1 = Thread(target=fun1, name="t1")
    t2 = Thread(target=fun2, name="t2")
    
    t1.start()
    t2.start()
