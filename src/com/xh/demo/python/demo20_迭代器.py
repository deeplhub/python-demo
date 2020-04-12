'''
Title: 迭代器
Description: 

迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：

迭代器还可以把一个类作为一个迭代器使用，需要在类中实现两个方法 __iter__() 与 __next__() 。
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法会返回下一个迭代器对象。

StopIteration：异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

使用迭代器的场景: 在程序需要处理大量集合数据的时候, 减少占用内存

Python类型判断有两种：type()和isinstance()
两者的区别：
    - 在判断子类上这两个函数不一样。type()不会认为子类是父类的类型，不考虑继承关系；isinstance()会认为子类是父类的类型，考虑继承关系。
    
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
isinstance() 与 type() 区别：
    - type() 不会认为子类是一种父类类型，不考虑继承关系。
    - isinstance() 会认为子类是一种父类类型，考虑继承关系。
    
如果要判断两个类型是否相同推荐使用 isinstance()。


参考地址：
    https://www.runoob.com/python3/python3-iterator-generator.html
    https://www.runoob.com/python/python-func-isinstance.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
import collections

print("***** 1 *****")
print("列表")
ls = [1, 2, 3]
it = iter(ls)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))

print("\n***** 2 *****")
print("字符串")
st = "12345"
print("st Iterator:", isinstance(st, collections.Iterator))
it = iter(st)
# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
print("it Iterator:", isinstance(it, collections.Iterator))
for i in it:
    print(i, end="")

print("\n***** 3 *****")
# 本身就是迭代器
ge = (i for i in range(10))
for i in ge:
    print(i, end="")

print("\n***** 4 *****")
# 迭代器对象可以使用常规for语句进行遍历：
ls = [1, 2, 3]
it = iter(ls)  # 创建迭代器对象
for i in it:
    print(i, end="")
print("\n=====================")
# 或
ls = [1, 2, 3]
it = iter(ls)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration as ex:
        break
        
print("\n***** 5 *****")

print("创建类迭代器")
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
class MyIter:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a = 1
        return x


myclass = MyIter()
myiter = iter(myclass)
print(next(myiter))

print("\n***** 6 *****")


# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
# 在 20 次迭代后停止执行
class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self
 
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
    print(x)
