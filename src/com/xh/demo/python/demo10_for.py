'''
Title: 
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''

for letter in "Python":
    print("当前字母：", letter)
    
print("\n#####################################\n")

fruits = ["banana", "apple", "mango"]
for fruit in fruits:
    print("当前水果：", fruit)

print("\n#####################################\n")

print("通过序列索引迭代")
fruits = ["banana", "apple", "mango"]
for index in range(len(fruits)):
    print("当前水果：", fruits[index])

print("\n#####################################\n")

print("循环使用 else 语句")
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num): # 根据因子迭代
        if num%i ==0:       # 确定第一个因子
            j =num/i        # 计算第二个因子
            print('%d 等于  %d * %d' % (num, i, j))
            break           # 跳出当前循环
        else:
            print(num, '是一个质数')
            break
else:
    print("没有循环数据!")
