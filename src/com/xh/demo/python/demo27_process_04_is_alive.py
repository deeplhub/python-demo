'''
@author: xilh
@since: 20200130
'''
import multiprocessing
import os
import time


def runChildProcess(name, a, b):
    print("Run Child Process, ppid = {}, pid = {}, pname = {}".format(os.getppid(), os.getpid(), name))
    time.sleep(3)
    
if __name__ == '__main__':
    print("Run Parent Process, pid =", os.getpid())
    child = multiprocessing.Process(target=runChildProcess,args=('test', 10, 20))
    print()
    child.start()
    # 查看进程状态
    print(child.is_alive())
    # 等待 child 完成后再执行主进程
    child.join()
    # 查看进程状态
    print(child.is_alive())
    print('主进程结束')
