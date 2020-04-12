'''
Title: 创建线程 - 直接实例化
Description: 

线程实现方法：
    - 直接实例化 Thread
    - 继承实现
开发中推荐使用第二种，使用面向对象完成，利于功能的扩展   

Python3 线程中常用的两个模块为：
    - _thread
    - threading(推荐使用)
thread 模块已被废弃。用户可以使用 threading 模块代替。所以，在 Python3 中不能再使用"thread" 模块。为了兼容性，Python3 将 thread 重命名为 "_thread"。


在线程里，传递参数有三种方法：
    - 使用元组传递 threading.Thread(target=方法名，args=（参数1,参数2, ...）)
    - 使用字典传递 threading.Thread(target=方法名, kwargs={"参数名": 参数1, "参数名": 参数2, ...})
    - 混合使用元组和字典 threading.Thread(target=方法名，args=（参数1, 参数2, ...）, kwargs={"参数名": 参数1,"参数名": 参数2, ...})

参考地址：
    https://www.jianshu.com/p/a4aedd66af7c
    https://www.cnblogs.com/luyuze95/p/11289143.html#%E4%BA%8C%E7%BA%BF%E7%A8%8B%E5%AE%9E%E7%8E%B0

@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
'''
from threading import current_thread, Thread
import time


def runFun(num):
    print(num, "子线程 work", current_thread().name)
    time.sleep(2)


if __name__ == '__main__':
    print("主线程开始")
    # 创建一个线程实例
    # target=<function>：要执行的函数
    # name：线程名称
    # args=()：元组中只包含一个元素时，需要在元素后面添加逗号
    my_thread = Thread(target=runFun, name="my_thread", args=(1,))
    print(my_thread.name)
    
    # 启动线程活动。
    my_thread.start()  
    # 等待至线程中止
    # 不加join的话，主线程和子线程完全是并行的，加了join主线程得等这个子线程执行完毕，才能继续往下走
    my_thread.join()  
    print("主线程结束")
