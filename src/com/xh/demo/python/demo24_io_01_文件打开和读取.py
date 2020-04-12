'''
Title: 文件打开和读取
Description: 

1. 文件的目的:
    - 存储信息和读取信息
2. 参数
    - file: 文件的路径
    - mode: 读写模式
    - encoding: 编码格式
3. 读写模式
    - 字符
    1). r 读            从开始读
    2). w 写            从开始写
    3). a 续写        从末尾写
    - 字节
    1). rb 读         从开始读
    2). wb 写         从开始写
    3). ab 续写     从末尾写
    - 符号 + 完成另外的读写
    r+, w+

参考地址：
    https://www.runoob.com/python3/python3-file-methods.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
file = None
try:
    # 读取文件, 获取文件流对象
    file = open(file="D:/python_test.log", mode="r", encoding="UTF-8")
    # 读取所有内容
    content = file.read()
    print(content)
except Exception as ex:
    print(ex)
finally:
    if file != None:
        file.close()
