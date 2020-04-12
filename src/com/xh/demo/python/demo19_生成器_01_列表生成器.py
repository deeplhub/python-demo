'''
Title: 生成器 - 简单生成器
Description: 

生成器
    - 如果能将列表元素能按一定规则推算出来, 而且可以循环获取这种元素

生成器仅仅保存了一套生成数值的算法，并且没有让这个算法现在就开始执行，而是我什么时候调它，它什么时候开始计算一个新的值，并给你返回。
由此看出 generator 保存的是算法，每次调用next(generaotr_ex)就计算出他的下一个元素的值，直到计算出最后一个元素，没有更多的元素时，抛出StopIteration的错误。

如果在函数中出现了yield关键字，则这个函数不再是普通的函数，而是一个生成器，其实这个yield的含义就是将一个普通函数变成一个生成器。
这种方式下，生成器可以实现无限制的列表元素，而列表生成式就无法做到这一点。

生成器的本质：生成器和列表生成式的不同之处在于，列表生成式其实就是一个list；
而生成器并不是一个完整的列表，而是保存的是算法，是一种状态。也可以这么说，生成器的作用就是用来生成迭代器的。

生成器generator的两种方式，对于列表生成式简单改造的方式来说，这种方式是比较简单，两者区别不大；
而对于生成器函数来说，这种方式中函数不再是一个普通函数，生成器保存的是算法，而不是列表。
实际上，我们通过for循环就可以实现对生成器的迭代，因为我们说生成器的作用其实就是用来生成迭代器的。

参考地址：
    https://www.cnblogs.com/wj-1314/p/8490822.html
    https://www.cnblogs.com/liangmingshen/p/9706181.html
    https://baijiahao.baidu.com/s?id=1602421350847230663&wfr=spider&for=pc

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

# 列表生成式和生成器作用是完全一样的，唯一的区别在于如果列表中元素数量过于巨大，使用列表生成式占用内存会大一点。
# 生成列表
ls = [x + 1 for x in range(10)]
# 打印的是列表
print(ls)

print("\n##############################\n")
# 把列表中的每个元素加 1
for index, i in enumerate(ls):
    ls[index] += 1
print(ls)

print("\n##############################\n")

vals = map(lambda x:x + 1, ls)
for index in vals:
    print(index)
    
print("\n##############################\n")

vals = [i + 1 for i in range(10)]
print(vals)

print("\n##############################")
print("##############################\n")

# 生成器
gen = (x + 1 for x in range(10))
# 打印的是<generator object <genexpr> at 0x000000000239BA50>
print(gen)
print(type(gen))
# 输出迭代器的下一个元素
print(next(gen))
print(next(gen))

print("\n###########################\n")

gen = (i for i in range(10))
print(type(gen))
for i in gen:
    print(i)

#  只能迭代一次， 再迭代就报错
# print(next(gen))
