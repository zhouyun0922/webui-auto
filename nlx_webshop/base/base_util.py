'''
@auth:zhouyun
@time:2021-12-27
'''
#encoding=UTF-8
import time
import unittest
from selenium import webdriver

class base_util(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        # 打开浏览器
        self.driver = webdriver.Chrome()
        # 加载网页
        self.driver.get("http://192.168.2.92:8098/login")
        # 全屏显示
        self.driver.maximize_window()
        time.sleep(1)

    def tearDown(self) -> None:
        pass