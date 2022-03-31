#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：base_util.py
@Author  ：周云
@Date    ：2022/3/3 11:35 
'''
# 写在conftest.py
import os
import allure
import unittest
from selenium import webdriver
import pytest


class base_util(unittest.TestCase):

    def setUp(self) -> None:
        # 打开浏览器
        global driver
        self.driver = webdriver.Chrome()
        # 加载网页
        self.driver.get("http://192.168.2.92:8083/login")
        # 全屏显示
        self.driver.maximize_window()

    def tearDown(self) -> None:
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
#def adb_screen_shot():
    # driver.get_screenshot_as_png()
    # driver.get_screenshot_as_base64()
    # driver.get_screenshot_as_file("122.jpg")
    # os.popen("adb screen -p testfailue.jpg")
