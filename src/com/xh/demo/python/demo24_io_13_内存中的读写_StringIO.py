'''
Title: 内存中的读写StringIO
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
from _io import StringIO

# 创建对象
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
ret = f.getvalue()
print(ret)
print()

f = StringIO("abcdefghijk")
print(f.read(2))
print(f.readline())
