"""
Title: 使用 captcha 生成验证码
Description:

使用captcha lib生成验证码（前提：pip install captcha）

@author H.Yang
@email xhaimail@163.com
@date 2020/4/2
"""
import os
import random

from captcha.image import ImageCaptcha


class CaptchaVerifyCode():

    def __init__(self):
        self.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"  # 图片上显示的字符集
        self.width = 120  # 图片宽度
        self.height = 40  # 图片高度
        self.fonts = None  # 图片字体
        self.font_sizes = (20, 30)  # 图片字体大小

    def create_captcha_image(self, file_name, code):
        """
        创建验证码图片
        :param file_name:文件全名称
        :param code:验证码字符串
        :return:
        """
        assert (self.width or self.height), "未知的图片尺寸！！！"
        assert code, "未知的随机码！！！"
        assert file_name, "未知的文件路径！！！"

        # 生成img文件：指定图片大小、字体、字体样式
        # generator = ImageCaptcha(width=width, height=height, fonts=fonts, font_sizes=font_sizes)
        generator = ImageCaptcha(self.width, self.height, self.fonts, self.font_sizes)
        # 生成图片
        img = generator.generate_image(code)
        # 保存图片
        img.save(file_name)
        # 展示输出结果
        # img.show()

    def generate_verify_code(self, file_path, char_count, image_suffix="png"):
        """
        生成验证码图片
        :param file_path: 文件路径
        :param char_count: 字符个数
        :param image_suffix: 文件后缀
        :return:
        """

        assert (char_count > 1), "未知的字符个数！！！"
        assert file_path, "未知的文件路径！！！"

        # 随机选取设定字符个数
        code = "".join([random.choice(self.characters) for j in range(char_count)])
        # 拼装文件名及文件后缀
        file_name = os.path.join(file_path, "{}.{}".format(code, image_suffix))
        # 创建图片，将字符串转换为图片
        self.create_captcha_image(file_name, code)

    def generate_batch_verify_code(self, file_path, char_count, max_count, image_suffix="png"):
        """
        批量生成验证码图片
        :param file_path: 文件路径
        :param char_count: 字符个数
        :param max_count: 文件个数
        :param image_suffix: 文件后缀
        :return:
        """

        # 判断文件夹是否存在
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        for index, i in enumerate(range(max_count)):
            self.generate_verify_code(file_path, char_count, image_suffix)
            print("Generate captcha image => {}".format(index + 1))


if __name__ == '__main__':
    captchaCode = CaptchaVerifyCode()
    file_path = "C:/Users/Administrator/Desktop/VerifyCode/temp/"
    captchaCode.generate_verify_code(file_path, 6)
    # captchaCode.generateBatchVerifyCode(file_path, 4, 10)
