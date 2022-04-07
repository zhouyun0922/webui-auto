#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：login_page.py
@Author  ：周云
@Date    ：2022/2/15 14:41 
'''
import time

import allure
import pytest
from selenium.webdriver.common.by import By
from base.base_page import basepage


class login_page(basepage):
    # 页面元素
    # 登录界面元素
    username_loc = (By.ID, "username")
    password_loc = (By.ID, "password")
    submit_loc = (By.CLASS_NAME, "ant-btn.ant-btn-primary.ant-btn-lg.ant-btn-block")
    #校验登录元素
    click_loc = (By.XPATH, " //span[1][text() ='13601455223']")
    assert_loc = (By.XPATH, "//*[text()='退出']")

    # 页面操作
    def login_mealordering_store(self, username, password):
        self.locator_value(login_page.username_loc,username)
        self.locator_value(login_page.password_loc, password)
        self.locator_click(login_page.submit_loc)

    def assert_login(self):
        time.sleep(2)
        self.locator_click(login_page.click_loc)
        time.sleep(2)
        messag = self.get_value(login_page.assert_loc)
        return messag

'''

    if __name__ == "__main__":
        pytest.main(['-s', '-v',assert_login])  # -s输出打印信息
'''
