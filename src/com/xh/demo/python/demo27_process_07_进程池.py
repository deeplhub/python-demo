'''
进程池
@author: xilh
@since: 20200130
'''
from multiprocessing import Pool
import os
import time

def work(num):
    print(num, 'begin pid =', os.getpid())
    time.sleep(3)
    print(num, 'over  pid =', os.getpid())
    
if __name__ == '__main__':
    print('== 主进程开始 ==')
    # 创建进程池, 初始化4个进程, 都是守护进程
    ppool = Pool(4)
    for i in range(10):
        # 非阻塞
        ppool.apply_async(work, (i,))
        # 阻塞
        # ppool.apply(work, (i,))
    # 关闭进程池, 不再接收新的任务
    ppool.close()
    # 执行先
    ppool.join()
    print('== 主进程结束 ==')