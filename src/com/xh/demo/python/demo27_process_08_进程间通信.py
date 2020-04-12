'''
进程间通信
@author: xilh
@since: 20200130
'''
from multiprocessing import Manager, Pool
import time


def write(q):
    for value in ['a', 'b', 'c', 'd', 'e']:
        print('put', value, 'to queue')
        q.put(value)
        time.sleep(1)
    
def read(q):
    while True:
        # 判断队列是否为空（里面是否还有数据）
        if not q.empty():
            # 从队列里获取值
            value = q.get()
            print('get', value, 'from queue')
            time.sleep(1)
        else:
            break
    
if __name__ == '__main__':
    q = Manager().Queue()
    print('== 主进程开始 ==')
    # 进程池
    ppool = Pool(2)
    ppool.apply(write, args=[q])
    ppool.apply(read, args=[q])
    # 关闭进程池, 不再接收新的任务
    ppool.close()
    # 执行先
    ppool.join()
    print('== 主进程结束 ==')