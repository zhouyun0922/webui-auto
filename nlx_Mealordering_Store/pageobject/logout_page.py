#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：logout_page.py
@Author  ：周云
@Date    ：2022/2/16 17:28 
'''
import time
import pytest
from selenium.webdriver.common.by import By
from base.base_page import basepage


class logout_page(basepage):
    # 页面元素
    #退出登录
    click_loc = (By.CLASS_NAME, "ant-dropdown-trigger.ant-dropdown-link")
    logout_loc = (By.XPATH, "//*[text()='退出']")
    #校验登录元素
    assert_login_loc = (By.XPATH, "//*[text()='登 录']")

    # 页面操作
    def logout_mealordering_store(self):
        self.locator_click(logout_page.click_loc)
        time.sleep(0.5)
        self.locator_click(logout_page.logout_loc)
        time.sleep(0.5)
    def assert_logout(self):
        return self.get_value(logout_page.assert_login_loc)