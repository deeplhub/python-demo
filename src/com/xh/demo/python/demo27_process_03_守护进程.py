'''
守护进程: 进程创建默认是非守护进程
    - 如果一个程序中, 所有非守护进程都停止了, 只剩守护进程, 程序终止. 所有守护进程都会停止
    - 主进程是非守护进程的
@author: xilh
@since: 20200130
'''
import multiprocessing
import os
import time


def runChildProcess(name, a, b):
    print("Run Child Process, ppid = {}, pid = {}, pname = {}".format(os.getppid(), os.getpid(), name))
    time.sleep(5)
    
if __name__ == '__main__':
    print("Run Parent Process, pid =", os.getpid())
    child = multiprocessing.Process(target=runChildProcess,args=('test', 10, 20))
    # 守护进程, 只剩守护进程, 程序终止, 所以主进程结束后, 会马上结束(没机会执行)
    child.daemon = True
    print()
    child.start()
    print('主进程结束')
