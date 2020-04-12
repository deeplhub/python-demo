'''
Title: os.path
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

import os

# 分隔
path = 'd:/python_test.log'
print(os.path.splitext(path))
print(os.path.split(path))

# 判断
print("exists:", os.path.exists(path))
print("isfile:", os.path.isfile(path))
print("isdir :", os.path.isdir(path))
