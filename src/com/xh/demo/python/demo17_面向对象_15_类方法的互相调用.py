'''
Title: 类方法的互相调用及self的含义
Description: 

参考地址：
    https://www.cnblogs.com/jins-note/p/9581568.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/09
'''


class MyClass1:
         
    def fun1(self):
        print(self.fun2())

    def fun2(self):
        return "MyClass1 fun2()"


class MyClass2:

    def fun1(self):
        return "MyClass2 fun1()"
        
    def fun2(self):
        print(self.fun1())


if __name__ == '__main__':
    my = MyClass1()
    my.fun1()
    
    my = MyClass2()
    my.fun2()
