'''
实现进程的方法：
1. 方法
    - demo27 01~05
2. 继承类（重写 run 方法）
开发中推荐使用第二种, 使用面向对象完成, 利于功能的扩展    
@author: xilh
@since: 20200130
'''
from multiprocessing import Process
import os
import time


class MyProcess(Process):
    def __init__(self, pname, a, b):
        # 这句话不能少
        Process.__init__(self, name = pname)
        self.a = a
        self.b = b
        
    def run(self):
        print(self.name+":",self.a, self.b)
        print("Run Child Process, ppid = {}, pid = {}".format(os.getppid(), os.getpid()))
        time.sleep(3)
        
if __name__ == '__main__':
    print('主进程开始')
    p1 = MyProcess('p1', 1, 2)
    print("p1.namet1", p1.name)
    p1.start()
    p2 = MyProcess('p2', 3, 4)
    print("p2.name:", p2.name)
    p2.start()
    
    p1.join()
    p2.join()
    print('主进程结束')