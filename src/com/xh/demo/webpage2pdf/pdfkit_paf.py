"""
Title: 网页保存PDF文件
Description:

通过 pdfkit 模块把 HTML 转换成 PDF文件
需要安装 wkhtmltopdf 工具，有绿色版的

参考地址：
    http://keejo.coding.me/%E4%BD%BF%E7%94%A8selenium%E6%8A%8A%E7%BD%91%E9%A1%B5%E4%BF%9D%E5%AD%98%E4%B8%BAPDF.html
    https://blog.csdn.net/u012561176/article/details/83655247
    https://juejin.im/post/5c6d2591e51d457fd033e305
    https://www.jianshu.com/p/44ec7a83adcb
    https://blog.csdn.net/qq_14873105/article/details/51394026

@author H.Yang
@email xhaimail@163.com
@date 2020/4/11
"""
import time

import pdfkit
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.cnblogs.com/hong-fithing/p/9656221.html")

    # 网页转换 PDF 文件
    config = pdfkit.configuration(wkhtmltopdf="D:/Python/wkhtmltox/bin/wkhtmltopdf.exe")
    pdfkit.from_url("https://www.cnblogs.com/hong-fithing/p/9656221.html", "test_python.pdf", configuration=config)

    # 网页转换长图片文件
    # config = pdfkit.configuration(wkhtmltopdf="D:/Python/wkhtmltox/bin/wkhtmltoimage.exe")
    # pdfkit.from_url("https://www.cnblogs.com/hong-fithing/p/9656221.html", "test_python.png", configuration=config)

    time.sleep(10)
    driver.quit()
