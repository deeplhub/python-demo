'''
Title: 创建线程 - 继承实现
Description: 

线程实现方法：
    - 直接实例化 Thread
    - 继承实现
开发中推荐使用第二种，使用面向对象完成，利于功能的扩展

参考地址：
    https://www.jianshu.com/p/a4aedd66af7c
    https://www.cnblogs.com/luyuze95/p/11289143.html#%E4%BA%8C%E7%BA%BF%E7%A8%8B%E5%AE%9E%E7%8E%B0


@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
'''
from threading import Thread, current_thread
import time


# 示例： 1 - 创建线程 - 继承实现 
class MyThread1(Thread):

    def __init__(self, threadName, param1, param2):
        # 这句话不能少
        # name：指定线程名称
        Thread.__init__(self, name=threadName)
        self.param1 = param1
        self.param2 = param2
    
    # 固定方法名，不能随便起
    def run(self):
        print(self.name, ":", self.param1, "-", self.param2)
        print("Run Child Thread, name:", current_thread().name)
        time.sleep(2)


# 示例： 2 - 创建线程 - 继承实现 
class MyThread2(Thread):

    def __init__(self, param1, param2):
        # 这句话不能少
        super(MyThread2, self).__init__()  # 重构run函数必须要写
        self.param1 = param1
        self.param2 = param2
    
    def run(self):
        print(self.name, ":", self.param1, "-", self.param2)
        print("Run Child Thread, name:", current_thread().name)
        time.sleep(2)


if __name__ == '__main__':
    print('主线程开始')
    print(1, "创建线程 - 继承实现")
    t1 = MyThread1("t1", 1, 2)
    print("t1.name:", t1.name)
    t1.start()
    
    t2 = MyThread1('t2', 3, 4)
    print("t2.name:", t2.name)
    t2.start()
    
    t1.join()
    t2.join()
    print()
    
    print(2, "创建线程 - 继承实现")
    t3 = MyThread2(5, 6)
    print("t3.name:", t3.name)
    t3.start()
    t3.join()
    
    t4 = MyThread2(7, 8)
    print("t4.name:", t4.name)
    t4.start()
    t4.join()
    print()

    print('主进程结束')
