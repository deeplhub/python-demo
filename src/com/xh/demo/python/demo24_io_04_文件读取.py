'''
Title: 文件读取
Description: 

文件读取后自动关闭, 使用: with open() as


@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''

print(1, "读取所有内容")
with open(file="D:/python_test.log", mode="r", encoding="UTF-8") as file:
    content = ''
    print("file.closed:", file.closed)
    # 读取所有内容
    while True:
        line = file.readline()
        if line == '':
            break
        content = content + line
        
print("content:")
print(content) 
print("file.closed:", file.closed)
print("\n\n")

print(2, "读取所有内容")
with open(file="D:/python_test.log", mode="r", encoding="UTF-8") as file:
    content = ''
    # 读取所有内容
    line = file.readlines()
    for i in line:
        content = content + i
print("content:")
print(content) 
print("file.closed:", file.closed)

