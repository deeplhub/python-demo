'''
os.fork() 创建一个新的进程, 复制父进程的所有资源到子进程中
然后父进程和子进程都会从 fork() 获取返回值
子进程获取的返回值是 0
父进程获取的返回值是子进程的编号(每一个进程都有一个唯一的编号 pid)

@see: https://segmentfault.com/a/1190000010523894
@author: xilh
@since: 20200129
'''
# 仅 linux 系统可用, windows 系统环境下没有此函数
# ret = os.fork()

import multiprocessing
import os


def runChildProcess(name):
    print("Run Child Process, ppid = {}, pid = {}, pname = {}".format(os.getppid(), os.getpid(), name))

if __name__ == '__main__':
    print("Run Parent Process, pid =", os.getpid())
    # args 是个 tuple
    child = multiprocessing.Process(target=runChildProcess,args=('test',))
    print()
    child.start()
    # 等待 child 完成后再执行主进程
    child.join()
