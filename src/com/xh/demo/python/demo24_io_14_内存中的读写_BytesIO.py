'''
Title: 内存中的读写BytesIO
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
from _io import BytesIO

# 创建对象
f = BytesIO()
f.write('hello'.encode(encoding='utf_8'))
f.write(' '.encode(encoding='utf_8'))
f.write('world'.encode(encoding='utf_8'))
f.write(' '.encode(encoding='utf_8'))
f.write('张三'.encode(encoding='utf_8'))
# 获取值
ret = f.getvalue()
print(ret)
print()

f = BytesIO('张三是程序员'.encode('utf-8'))
print(f.readline())
# 关闭
f.close()
