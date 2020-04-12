'''
Title: json操作
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
'''
import json
from datetime import datetime, date


class JsonUtils:

    @classmethod
    def toJsonString(cls, obj, sort=False, sindent=4):
        '''
        @note: 对象转字符串
        @param obj: 转换对象
        @param sort: 是否排序
        @param sindent: 缩减
        '''

        def to_dict(obj):
            dict1 = {}
            for attr in dir(obj):
                # obj.columns()是实体类中的 columns()
                if attr not in obj.columns():
                    continue
                # getattr()：函数用于返回一个对象属性值。
                value = getattr(obj, attr)
                # isinstance()：函数来判断一个对象是否是一个已知的类型，类似 type()。
                if value is not None and isinstance(value, datetime):
                    value = str(value)
                if value is not None and isinstance(value, date):
                    value = str(value)
                dict1[attr] = value

            return dict1

        if obj is None:
            return ""
        if sort == False:
            sindent = 0
        if sindent == 0:
            json_string = json.dumps(obj, default=to_dict, ensure_ascii=False, sort_keys=sort)
        else:
            json_string = json.dumps(obj, default=to_dict, ensure_ascii=False, sort_keys=sort, indent=sindent)
        return json_string

    @classmethod
    def toObject(cls, obj, json_str):
        '''
        @note: 字符串转对象
        @param obj: 转换对象
        @param json_str: 字符串
        '''
        dict1 = json.loads(json_str)
        obj.__dict__ = dict1;
        return obj


if __name__ == '__main__':
    sdict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    print(JsonUtils.toJsonString(sdict, True))
    print(JsonUtils.toJsonString(sdict))
