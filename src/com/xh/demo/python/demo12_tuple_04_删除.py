'''
Title: 元组删除
Description: 
    元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''

print("删除元组")
# 元组中的元素是不能删除的,但我们可以使用del语句来删除整个元组
tup = ('physics', 'chemistry', 1997, 2000)
print("tup1:", tup)
    
try:
    del tup
    print("del tup:", tup)
except Exception as ex:
    print(ex)
