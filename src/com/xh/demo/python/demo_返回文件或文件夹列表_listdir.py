'''
Title: 
Description: 

用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。

参考地址：
    https://www.runoob.com/python3/python3-os-listdir.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/11
'''
import os

print(os.listdir(os.getcwd()))
