'''
Title: 文件写入
Description: 

参考地址：
    https://www.runoob.com/python3/python3-file-methods.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

print(1, "从头开始编辑，会原删除原有内容")
with open(file="D:/python_test.log", mode="w", encoding="GBK") as file:
    file.write("今天")
#     file.write("明天", "UTF-8")
    
print("读取所有内容")

with open(file="D:/python_test.log", mode="r") as file:
    # 读取所有内容
    content = file.read()
print("content:")
print(content) 
print()

print(2, "在文件末尾添加")
# 在文件末尾添加
with open(file="D:/python_test.log", mode="a", encoding="GBK") as file:
    file.write("明天")

with open(file="D:/python_test.log", mode="r") as file:
    # 读取所有内容
    content = file.read()
print("content:")
print(content) 
