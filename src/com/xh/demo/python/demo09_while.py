'''
Title: 
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''

count = 0
while count < 10 :
    print("The count is：", count)
    count = count + 1

print("\n########################################\n")

count = 1
while count < 10:
    count += 1
    # 非双数时跳过输出
    if count % 2 > 0:
        continue
    # 输出双数2、4、6、8、10
    print(count)

print("\n########################################\n")

count = 1
# 循环条件为1必定成立
while count:
    # 输出1~10
    print(count)
    # 当i大于10时跳出循环
    count += 1
    if count > 10:
        break

print("\n########################################\n")

print("循环使用 else 语句")
count = 0
while count < 5:
    print("count", count, "is less than 5")
    count = count + 1
else:
    print("count", count, "is not less than 5")
