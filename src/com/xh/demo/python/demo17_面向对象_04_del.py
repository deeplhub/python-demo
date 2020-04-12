'''
Title: 删除对象
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/06
'''


class Student:

    # 删除对象时调用
    def __del__(self):
        print("del....")
    
    def eat(self):
        print("eat.....")
        
    def gotoClass(self):
        print("go to class...")


s1 = Student()
s1.eat()

del s1
