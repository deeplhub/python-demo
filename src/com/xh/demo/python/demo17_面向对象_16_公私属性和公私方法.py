'''
Title: 公有、私有属性和公有、私有方法
Description: 

私有属性和私有方法需要在前面加上两个下划线即可，私有属性和私有方法只能在当前类中使用，否则会出异常

参考地址：
    https://www.cnblogs.com/Sup-to/p/10878954.html
    https://blog.csdn.net/liuskyter/article/details/80387726
    
    
@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''
class Student():
    def __init__(self, name, age, sex):
        self.name = name
        self.__age = age
        self.sex = sex
        
    def __private(self):
        print("这是一个私有方法")
    
    def public(self):
        print("这是一个共有方法")
    
    def getAge(self):
        return self.__age


if __name__ == '__main__':
    stu = Student("张三", 24, "男")
    print(stu.name)
#     print(stu.__age)
    print(stu.sex)
    
#     stu.__private()
    print(stu.getAge())
#     stu.public()
