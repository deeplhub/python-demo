"""
Title: 滚动截图
Description:

缺陷是截图后拼接时会出现偏差

@author H.Yang
@email xhaimail@163.com
@date 2020/4/11
"""

import time

import numpy
from PIL import Image
from selenium import webdriver


def screenshot(driver):
    window_height = driver.get_window_size()['height']  # 窗口高度
    page_height = driver.execute_script('return document.documentElement.scrollHeight')  # 页面高度
    driver.save_screenshot('image/temp/qq.png')
    if page_height > window_height:
        n = page_height // window_height  # 需要滚动的次数
        base_mat = numpy.atleast_2d(Image.open('image/temp/qq.png'))  # 打开截图并转为二维矩阵

        for i in range(n):
            driver.execute_script(f'document.documentElement.scrollTop={window_height * (i + 1)};')
            driver.save_screenshot(f'image/temp/qq_{i}.png')  # 保存截图
            mat = numpy.atleast_2d(Image.open(f'image/temp/qq_{i}.png'))  # 打开截图并转为二维矩阵
            base_mat = numpy.append(base_mat, mat, axis=0)  # 拼接图片的二维矩阵
        Image.fromarray(base_mat).save('image/hao123.png')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.cnblogs.com/hong-fithing/p/9656221.html")
    screenshot(driver)
    time.sleep(10)
    driver.quit()
