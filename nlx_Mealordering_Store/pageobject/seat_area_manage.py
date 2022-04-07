#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：seat_area_manage.py
@Author  ：周云
@Date    ：2022/2/17 10:42 
'''
import time
import pytest
from base.base_page import basepage
from selenium.webdriver.common.by import By

class Seat_area_manage(basepage):
    # 页面元素
    # 创建区域
    set_loc = (By.XPATH, "//span[2][text()='座位']")
    area_loc = (By.XPATH, "//span[2][text()='区域划分']")
    create_area_button_loc =(By.XPATH,"//span[text()='新建区域']")
    area_name_loc =(By.ID,"basic_name")
    save_loc = (By.XPATH,"//button/span[text()='保 存']")
    # 校验登录元素
    assert_create_area_loc = (By.XPATH, "//*[text()='已保存']")
    assert_area_loc = (By.XPATH, "//*[text()='区域测试']")
    # 删除区域
    name_area_loc =(By.XPATH,"//td[2][text() = '区域测试']")
    delete_area_loc =(By.XPATH,"//div[2][@class ='ant-space-item']")
    confirm_area_loc =(By.XPATH,"//span[text() ='确 认']")
    #校验删除结果
    assert_delete_area_loc =(By.XPATH,"//span[text() = '已删除']")
    # 页面操作
    def create_area(self,area_name):
        time.sleep(2)
        self.locator_click(Seat_area_manage.set_loc)
        time.sleep(2)
        self.locator_click(Seat_area_manage.area_loc)
        time.sleep(2)
        self.locator_click(Seat_area_manage.create_area_button_loc)
        time.sleep(2)
        self.locator_value(Seat_area_manage.area_name_loc,area_name)
        time.sleep(2)
        self.locator_click(Seat_area_manage.save_loc)
        time.sleep(2)

    def assert_create_area(self):
        messg=[self.get_value(Seat_area_manage.assert_create_area_loc),self.get_value(Seat_area_manage.assert_area_loc)]
        return messg

    def delete_area(self):
        self.locator_click(Seat_area_manage.set_loc)
        time.sleep(0.5)
        self.locator_click(Seat_area_manage.area_loc)
        time.sleep(0.5)
        area_list =self.locator_elements(Seat_area_manage.name_area_loc)
        if len(area_list)>0:
            area_confirm_list = self.locator_elements(Seat_area_manage.delete_area_loc)
            #self.locator_click(area_confirm_list[0])
            area_confirm_list[0].click()
        else:
            print("区域不存在！")
        time.sleep(0.5)
        self.locator_click(Seat_area_manage.confirm_area_loc)

    def assert_delete_area(self):
        return self.get_value(Seat_area_manage.assert_delete_area_loc)
