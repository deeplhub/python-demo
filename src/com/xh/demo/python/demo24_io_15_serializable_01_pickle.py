'''
Title: serializable_pickle
Description: 

pickle 模块实现了用于序列化和反序列化Python对象结构的二进制协议

pickle 提供了一个简单的持久化功能。可以将对象以文件的形式存放在磁盘上。
pickle 序列化后的数据，可读性差，人一般无法识别。

pickle 协议和 JSON（JavaScript Object Notation）的区别 ：
    - JSON 是一种文本序列化格式（它输出 unicode 文本，虽然大部分时间它被编码 utf-8），而 pickle 是二进制序列化格式;
    - JSON 是人类可读的，而 pickle 则不是;
    - JSON 是可互操作的，并且在 Python 生态系统之外广泛使用，而 pickle 是特定于 Python 的;

默认情况下，JSON 只能表示 Python 内置类型的子集，而不能表示自定义类; 
pickle 可以表示极其庞大的 Python 类型（其中许多是自动的，通过巧妙地使用 Python 的内省工具;复杂的案例可以通过实现特定的对象API来解决）。

pickle可以存储的数据类型：
    - 所有python支持的原生类型：布尔值，整数，浮点数，复数，字符串，字节，None。
    - 由任何原生类型组成的列表，元组，字典和集合。
    - 函数，类，类的实例

pickle.dump()：将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
pickle.dumps()：将数据通过特殊的形式转换为只有python语言认识的字符串
pickle.load()：从数据文件中读取数据，并转换为python的数据结构
pickle.loads()：将pickle数据转换为python的数据结构

参考地址：
    https://www.cnblogs.com/lincappu/p/8296078.html
    https://www.cnblogs.com/baby-lily/p/10990026.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/07
'''
import pickle

stu = {
    'sid': 10,
    'sname': '张三',
    'sage': 30
}
# serialize
# 序列化对象，并将结果数据流写入到文件对象中。
ret1 = pickle.dumps(stu)
print(ret1)
# deserialize
# 反序列化对象。从bytes对象读取pickle对象层次结构并返回其中指定的重构对象层次结构。
ret2 = pickle.loads(ret1)
print(ret2)
print()

# 持久化到文件
with open(file="D:/python_test.log", mode="wb") as file:
    file.write(ret1)

with open(file="D:/python_test.log", mode="rb") as file:
    ret1 = file.read();
    print(ret1)

# deserialize
ret2 = pickle.loads(ret1)
print(ret2)
    
