'''
Title: 异步
Description: 
- 同步: 协同步调, 按照约定的顺序执行, 借助锁
- 异步: 异步处理不用阻塞当前线程来等待处理, 而是允许后续操作, 直至其他线程处理完成, 并回调通知此线程

@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
'''
from multiprocessing import Pool
import os
import time


def test1(a, b):
    print(a, b)
    print('test1 begin   ... pid=', os.getpid())
    print()
    time.sleep(0.3)
    return 'python'


def test2(python):
    print('from test1:', python)
    print('test2 callback... pid=', os.getpid())


if __name__ == '__main__':
    print('== 主进程开始 ==')
    # 进程池
    ppool = Pool(2)
    ppool.apply_async(test1, args=['a', 'b'], callback=test2)
    # 关闭进程池, 不再接收新的任务
    ppool.close()
    # 执行先
    ppool.join()
    print('== 主进程结束 ==')
