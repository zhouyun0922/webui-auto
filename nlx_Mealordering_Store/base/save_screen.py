#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：save_screen.py
@Author  ：周云
@Date    ：2022/3/4 13:51 
'''
import allure
import pytest
from selenium import webdriver

# 添加报错截图到allure报告里
@pytest.hookimpl(tryfirst=True, hookwrapper=True)  #钩子函数，可以获取到测试用例不同执行阶段的结果
def pytest_runtest_makereport(self):
    '''
　　每个测试用例执行后，制作测试报告
　　:param item:测试用例对象
　　:param call:测试用例的测试步骤
            先执行when=’setup’ 返回setup 的执行结果
            然后执行when=’call’ 返回call 的执行结果
            最后执行when=’teardown’返回teardown 的执行结果
　　:return:

    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        img = self.driver.get_screenshot_as_png()
        allure.attach(img, "失败截图", allure.attachment_type.PNG)
    '''
    img = self.driver.get_screenshot_as_png()
    allure.attach(img, "用例执行截图", allure.attachment_type.PNG)