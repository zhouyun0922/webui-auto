#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：base_util.py
@Author  ：周云
@Date    ：2022/3/3 11:35 
'''
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Baseutil(object):

	def setup(self) -> None:
		global driver
		self.options = Options()
		#self.options.add_argument('--headless')
		self.options.add_argument('--no-sandbox')
		self.options.add_argument('--disable-gpu')
		self.options.add_argument('--disable-dev-shm-usage')
		self.options.binary_location = '/usr/bin/google-chrome-stable'
		#self.options.add_argument('--window-size=1420,1080')
		#self.options.add_argument("--disable-notifications")
		#self.options.add_experimental_option('useAutomationExtension', False)
		# 打开浏览器
		self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver', chrome_options=self.options)
		time.sleep(2)
		# 加载网页
		self.driver.get("http://192.168.2.92:8083/login")
		time.sleep(0.5)
		# 全屏显示
		self.driver.maximize_window()


	def teardown(self) -> None:
		time.sleep(1)
		img = self.driver.get_screenshot_as_png()
		allure.attach(img, "用例执行截图", allure.attachment_type.PNG)


'''
    # 添加报错截图到allure报告里
   @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self):

        #hook pytest失败
        #:param item:
        #:param call:
        #:return:

        outcome = yield
        rep = outcome.get_result()
        # we only look at actual failing test calls, not setup/teardown
        if rep.when == "call" and rep.failed:
            img = self.driver.get_screenshot_as_png()
            allure.attach(img, "失败截图", allure.attachment_type.PNG)
'''

