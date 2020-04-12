'''
Title: 生成器 - 函数生成器 - yield
Description: 

如果在函数中出现了yield关键字，则这个函数不再是普通的函数，而是一个生成器，其实这个yield的含义就是将一个普通函数变成一个生成器。
这种方式下，生成器可以实现无限制的列表元素，而列表生成式就无法做到这一点。

生成器generator的两种方式，对于列表生成式简单改造的方式来说，这种方式是比较简单，两者区别不大；
而对于生成器函数来说，这种方式中函数不再是一个普通函数，生成器保存的是算法，而不是列表。
实际上，我们通过for循环就可以实现对生成器的迭代，因为我们说生成器的作用其实就是用来生成迭代器的。

简单来说 yield 返回值的过程是每次停在哪，下次又开始在哪
理解的关键在于：下次迭代时，代码从yield的下一条语句开始执行

参考地址：
    https://www.cnblogs.com/wj-1314/p/8490822.html
    https://www.cnblogs.com/liangmingshen/p/9706181.html
    https://baijiahao.baidu.com/s?id=1602421350847230663&wfr=spider&for=pc


@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
# 生成器函数(函数内部使用yield)
# 生成器函数=函数+yield，但是此时的函数已经不再是一个普通函数，而是一个生成器
#
# 模拟数据库主键自增。
def increment(primarykey=1):
    while True:
        # 每次执行到此语句就中断，等待下一次调用从该句的下一次执行
        yield primarykey
        
        primarykey = primarykey + 1


g1 = increment()
# 获取第一次自增的主键
key = next(g1)
print(key)

# 获取第二次自增的主键
key = next(g1)
print(key)

# 获取第三次自增的主键
key = next(g1)
print(key)
