'''
Title: 查找字符串
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/05
'''
print("== str 查找 ==")
str1 = "123567590dhgj散热污染123"

# 检测是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
index = str1.find("3")  # 包含字符串中
print("1. exist : ", str(index))

index = str1.find("4")  # 不包含字符串中
print("2. not exist : ", str(index))

# 指定开始位置
index = str1.find("3", 10)
print("begin with index 10:", str(index))

# 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
index = str1.index("3")
print("exist : ", str(index))

index = str1.index("63")
print("not exist : ", index)
