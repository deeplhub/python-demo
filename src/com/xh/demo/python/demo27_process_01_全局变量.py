'''
@note: 在多进程中, 全局变量对于每个进程: 各执一份, 互不影响
@author: xilh
@since: 20200129
'''
# 仅 linux 系统可用, windows 系统环境下没有此函数
# ret = os.fork()

import multiprocessing
import os

num = 100000
def runChildProcess(name):
    print("Run Child Process, ppid = {}, pid = {}, pname = {}".format(os.getppid(), os.getpid(), name))
    global num
    while num < 200000:
        num = num + 1
    print("Child  num:", num)

if __name__ == '__main__':
    print("Run Parent Process, pid =", os.getpid())
    # args 是个 tuple
    child = multiprocessing.Process(target=runChildProcess,args=('test',))
    print()
    child.start()
    child.join()
    while num > 0:
        num = num - 1;
    print("Parent num:", num)
