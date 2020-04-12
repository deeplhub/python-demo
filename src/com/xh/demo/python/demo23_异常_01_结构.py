'''
Title: 异常
Description: 

处理异常:
    1. 代码异常
        - 异常模式    try...except... else... finally...
    2. 逻辑异常
        - 在设计上考虑更周全, 代码逻辑清晰明确

else：是没异常时执行的代码
raise：抛出一个指定的异常。

参考地址：
    https://www.runoob.com/python3/python3-errors-execptions.html
    
@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
print(1, "异常")
try:
    num = 1 / 0
    print('end  ...')
except:
    print('不能除0')   
print("\n\n")

print(1, "异常")
try:
    num = 1 / 0
    print('end  ...')
except (NameError, ZeroDivisionError) as ex:
    print('ERR:', ex)   
print("\n\n")

print(2, "异常")
try:
    num = 1 / 0
    print('end  ...')
except NameError as ex:
    print('ERR1:', ex)   
except ZeroDivisionError as ex:
    print('ERR2:', ex)   
print("\n\n")

print(3, "异常")
try:
    num = 1 / 1
    print('end  ...')
except ZeroDivisionError as ex:
    print('ERR2:', ex)
else:    
    print('else')
print("\n\n")

print(4, "异常")
try:
    num = 1 / 0
    print('end  ...')
except ZeroDivisionError as ex:
    print('ERR2:', ex)
else:    
    print('else')
finally:
    print('finally')    
