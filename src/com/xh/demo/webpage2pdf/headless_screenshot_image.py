"""
Title: 无头生成图片
Description:

此方法不会打开浏览器，只是在后台进行，与 PhantomJS 类似（PhantomJS 已停止维护）

@author H.Yang
@email xhaimail@163.com
@date 2020/4/11
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.cnblogs.com/hong-fithing/p/9656221.html")

    # 接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("document.documentElement.scrollWidth")
    height = driver.execute_script("document.documentElement.scrollHeight")
    print(width, height)
    # 将浏览器的宽高设置成刚刚获取的宽高
    driver.set_window_size(width, height)
    # 截图
    driver.save_screenshot("image/test.png")

    time.sleep(10)
    driver.quit()
