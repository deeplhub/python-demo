'''
Title: 删除文件夹
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
import os
import shutil

# 删除文件夹
path = "d:\\test01\\a\\b\\c"
if os.path.exists(path):  # 判断文件夹是否存在
    os.rmdir(path)

# 递归删除，删除文件夹及其子目录
shutil.rmtree("d:\\test01")

