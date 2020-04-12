"""
Title: 使用 opencv-python 生成验证码
Description:

使用opencv-python lib生成验证码（前提：pip install opencv-python）



参考地址:
    https://www.cnblogs.com/youmuchen/p/8300027.html

    numpy.random.randint:
        https://blog.csdn.net/u011851421/article/details/83544853?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1

    opencv画图功能
        https://www.jianshu.com/p/999e35fe5e60

@author H.Yang
@email xhaimail@163.com
@date 2020/4/7
"""
import os
import cv2
import numpy


class OpencvVerifyCode():

    def randcolor(self):
        """
        生成随机颜色
        :return:
        """
        return (numpy.random.randint(0, 255), numpy.random.randint(0, 255), numpy.random.randint(0, 255))

    def randchar(self):
        """
        根据 ASCII 码生成随机字符或数字
        :return:
        """
        return numpy.random.choice([chr(numpy.random.randint(65, 90)), chr(numpy.random.randint(97, 122)), numpy.random.randint(0, 9)])

    def randpos(self, x_start, x_end, y_start, y_end):
        return (numpy.random.randint(x_start, x_end), numpy.random.randint(y_start, y_end))

    def image_setting(self, img_rand, char_count):
        code = ""
        for i in range(char_count):
            char = self.randchar()
            # 各参数依次是：图片，添加的文字，左上角坐标(x,y)，字体，字体大小，颜色，字体粗细
            cv2.putText(
                img_rand,
                char,
                (numpy.random.randint(4, 25) + i * 25, numpy.random.randint(4, 10) + 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                self.randcolor(),
                2
            )
            code += char
        #
        return code

    def line(self, img_rand, max_line, img_width, img_heigth):
        # 添加直线
        for i in range(max_line):
            cv2.line(
                img_rand,
                self.randpos(0, img_heigth, 0, img_width),  # 直线起点坐标
                self.randpos(0, img_heigth, 0, img_width),  # 直线终点坐标
                self.randcolor(),  # 当前绘画的颜色
                numpy.random.randint(1, 3)  # 画笔的粗细，线宽
            )
        #

    def generateVerifyCode(self, file_path, img_heigth, img_width):
        # 生成一个随机矩阵，randint(low[, high, size, dtype])
        # img_rand = numpy.random.randint(
        #     numpy.random.randint(50, 100),  # 生成的数值最低要大于等于low。（hign = None时，生成的数值要在[0, low)区间内）
        #     numpy.random.randint(100, 150),  # (可选)如果使用这个值，则生成的数值在[low, high)区间。
        #     (img_heigth, img_width, 3),  # (可选)输出随机数的尺寸，比如size = (m * n* k)则输出同规模即m * n* k个随机数。默认是None的，仅仅返回满足要求的单一随机数。
        #     numpy.uint8  # (可选)想要输出的格式。
        # )
        img_rand = numpy.random.randint(
            80, # 生成的数值最低要大于等于low。（hign = None时，生成的数值要在[0, low)区间内）
            180,  # (可选)如果使用这个值，则生成的数值在[low, high)区间。
            (img_heigth, img_width, 3),  # (可选)输出随机数的尺寸，比如size = (m * n* k)则输出同规模即m * n* k个随机数。默认是None的，仅仅返回满足要求的单一随机数。
            numpy.uint8  # (可选)想要输出的格式。
        )
        code = self.image_setting(img_rand, 4)
        print(code)
        self.line(img_rand, 6, img_heigth, img_width)
        file_name = os.path.join(file_path, "{}.{}".format(code, "png"))
        cv2.imwrite(file_name, img_rand)


if __name__ == '__main__':
    code = OpencvVerifyCode()
    for i in range(10):
        code.generateVerifyCode("C:/Users/Administrator/Desktop/VerifyCode/temp/", 60, 240)

    # print(code.randchar())
