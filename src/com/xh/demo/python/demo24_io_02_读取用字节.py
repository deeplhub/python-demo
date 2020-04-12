'''
Title: 读取用字节
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
file = None
try:
    # 读取文件, 获取文件流对象
    file = open(file="D:\\tmp\\test.txt", mode="rb")
    # 读取所有内容
    content = file.read()
    print("content:")
    print(content.decode("UTF-8"))
except Exception as es:
    print(es)
finally:
    # 关闭文件
    if file != None:
        file.close()
