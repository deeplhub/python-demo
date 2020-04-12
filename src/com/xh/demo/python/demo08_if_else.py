'''
Title: 
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''
from builtins import str, int
num = None
if num is None:
    print("1. is None")

# 判断变量是否为 python
num = "python"
if num == "python":
    print("2. num is python")

num = input("请输入内容：")
print("type：" + str(type(num)))
print("num：" + num + "")

# 判断字符串num为空
if len(num) == 0:
    print("3. num 为空，长度为0 ")
#     return

num = int(num)
if num == 3:
    print("3. num == 3")
elif num == 2:
    print("3. num ==2")
elif num == 1:
    print("3. num == 1")
elif num < 0:
    print("3. num < 0")
else:
    print("3. 条件均不成立")
