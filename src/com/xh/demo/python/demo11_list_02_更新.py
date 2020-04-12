'''
Title: 列表更新
Description: https://www.runoob.com/python3/python3-list.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/04
'''

print("== 更新列表 ==")
list = []
list.append("Goodle")  # 使用append()方法来添加列表项
print(list)
list.append("FaceBook")
print(list)

iterable = ["baidu", "360"]
list.extend(iterable)  # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print(list)

iterable = ('ali', 'taobao')
list.extend(iterable)
print(list)

iterable = {'QQ': 0, 'weixin': 0}
list.extend(iterable)
print(list)
