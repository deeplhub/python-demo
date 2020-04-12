'''
Title: 异常 - 自定义异常
Description: 

自定义异常:
    - 继承异常类(Exception)

raise：抛出一个指定的异常。

内置函数列表：
    https://www.runoob.com/python/python-built-in-functions.html
    
参考地址：
    https://www.runoob.com/python3/python3-errors-execptions.html
    

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

# 继承异常类(Exception)
class MyException(Exception):

    def __init__(self, msg):
        self.msg = msg

    
age = 30
if age > 10:
    raise MyException("年龄不能大于 10 岁")
