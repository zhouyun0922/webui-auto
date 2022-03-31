#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：base_page.py
@Author  ：周云
@Date    ：2022/2/15 14:34 
'''
from selenium.webdriver.support.select import Select


class basepage():
    def __init__(self, driver):
        self.driver = driver

    # 定位元素的关键字
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    # 定位元素组的关键字
    def locator_elements(self, loc):
        return self.driver.find_elements(*loc)

    # 设置值的关键字
    def locator_value(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 设置单击的关键字
    def locator_click(self, loc):
        self.locator_element(loc).click()

    # 进入框架
    def goto_frame(self, fram_name):
        self.driver.switch_to.frame(fram_name)

    # 出框架
    def out_frame(self):
        self.driver.switch_to.default_content()

    # 下拉框关键字
    def choice_select(self, loc, value):
        sel = Select(self.locator_element(loc))
        sel.select_by_value(value)

    # 获取文本的值
    def get_value(self, loc):
        return self.locator_element(loc).text

    # 获取文本的第二种方法
    def get_attribute(self, loc):
        return self.locator_element(loc).is_displayed()

    # 滚动屏幕底部
    def execute_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
