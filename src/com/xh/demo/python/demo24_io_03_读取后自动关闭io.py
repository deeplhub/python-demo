'''
Title: 读取后自动关闭io
Description: 

文件读取后自动关闭, 使用: with open() as

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
# 读取文件, 获取文件流对象
with open(file="D:/python_test.log", mode="rb") as file:
    print("file.closed:", file.closed)
    # 读取所有内容
    content = file.read()
    
print(content.decode("UTF-8"))
print("file.closed:", file.closed)
