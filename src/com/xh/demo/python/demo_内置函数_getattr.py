'''
Title: 内置函数 - 返回对象属性值
Description: 

getattr() 函数用于返回一个对象属性值。

getattr 语法：getattr(object, name[, default])
参数
    - object -- 对象。
    - name -- 字符串，对象属性。
    - default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。

参考地址：
    https://www.runoob.com/python/python-func-getattr.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/09
'''

class MyClass():
    bar = 432341
    
    def show(self):
        print("show...")

    
my = MyClass()
print(getattr(my, "bar"))  # 获取属性 bar 值

# print(getattr(my, "bar2"))  # 属性 bar2 不存在，触发异常

print(getattr(my, 'bar2', 3))  # 属性 bar2 不存在，但设置了默认值

obj = getattr(my, "show")
obj()

print("#################")
print(getattr(my, 'bar2', 3))
