'''
Title: 返回文件指针当前位置。
Description: 

tell() 方法返回文件的当前位置，即文件指针当前位置。

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

# 在文件末尾添加
with open(file="D:/python_test.log", mode="w", encoding="GBK") as file:
    file.write("今天")
    print(file.tell())  # 返回文件当前位置。
    file.write("明天")
    print(file.tell())
    
with open(file="D:/python_test.log", mode="r") as file:
    # 读取所有内容
    content = file.read()
print("content:")
print(content) 
print()

with open(file="D:/python_test.log", mode="r") as file:
    # 读取所有内容
    content = file.read(1)
    print("content:", content)
    print(file.tell()) 
    # 从头开始读
    file.seek(0)
    print(file.tell())
    
