'''
@auth:zhouyun
@time:2021-12-27
'''
#encoding=UTF-8
import time
import unittest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class base_util(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        self.options = Options()
        # self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.binary_location = '/usr/bin/google-chrome-stable'
        # self.options.add_argument('--window-size=1420,1080')
        # self.options.add_argument("--disable-notifications")
        # self.options.add_experimental_option('useAutomationExtension', False)
        # 打开浏览器
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver', chrome_options=self.options)
        time.sleep(2)
        # 加载网页
        self.driver.get("http://192.168.2.92:8098/login")
        time.sleep(1)
        # 全屏显示
        self.driver.maximize_window()

    def tearDown(self) -> None:
        time.sleep(1)
        img = self.driver.get_screenshot_as_png()
        allure.attach(img, "用例执行截图", allure.attachment_type.PNG)