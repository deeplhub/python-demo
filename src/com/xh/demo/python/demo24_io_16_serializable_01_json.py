'''
Title: serializable_json
Description: 

json.dumps()：将 Python 对象编码成 JSON 字符串
json.loads()：将已编码的 JSON 字符串解码为 Python 对象

dumps是将dict转化成str格式；
loads是将str转化成dict格式。
dump和load也是类似的功能，只是与文件操作结合起来了。

参考地址：
    https://www.runoob.com/python/python-json.html
    https://www.cnblogs.com/fengff/p/11008353.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
import json

stu = {
    'sid': 10,
    'sname': '张三',
    'sage': 30
}
# serialize
ret1 = json.dumps(stu)
print(ret1)

# deserialize
ret2 = json.loads(ret1)
print(ret2)
