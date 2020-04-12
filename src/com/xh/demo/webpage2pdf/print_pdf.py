"""
Title: 通过调用打印机服务保存 PDF 文件
Description: 

@author H.Yang
@email xhaimail@163.com
@date 2020/4/11
"""

import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    appState = {
        "recentDestinations": [
            {
                "id": "Save as PDF",
                "origin": "local"
            }
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
    profile = {
        'printing.print_preview_sticky_settings.appState': json.dumps(appState),
        'savefile.default_directory': 'C:/Users/Administrator/Documents'  # 文件路径
    }

    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', profile)
    chrome_options.add_argument('--kiosk-printing')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.cnblogs.com/hong-fithing/p/9656221.html")
    # 重要，只有调用打印时才能保存 PDF 文件
    driver.execute_script('window.print();')
    time.sleep(10)
    driver.quit()
