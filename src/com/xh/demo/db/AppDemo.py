"""
Title: 
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/4/11
"""
import time

from src.com.xh.demo.db.database import Database
from src.com.xh.demo.db.student import Student


class AppDemo():

    def save(self):
        stu = Student()
        stu.name = "张三"
        stu.age = 12
        stu.sex = "男"

        dao = Database()
        dao.save(stu)
        dao.transaction()

        args = {}
        rows = dao.load(Student, *args)
        print(rows)


if __name__ == '__main__':
    for i in range(10):
        app = AppDemo()
        app.save()
        time.sleep(1)
