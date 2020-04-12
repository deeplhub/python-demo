'''
Title: 当前文件夹
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

import os

# 获取当前文件夹
print(os.getcwd())
#  切换当前文件夹
os.chdir("d:\\tmp")
print(os.getcwd())
