#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：test_area_manage_03.py
@Author  ：周云
@Date    ：2022/2/17 11:06 
'''
import time
import pytest
from base.base_util import Baseutil
from pageobject.login_page import login_page
from pageobject.seat_area_manage import Seat_area_manage
import allure

#@pytest.mark.usefixtures('base_util')
class Test_area_case(Baseutil):
    @allure.story("座位")  # 模块名称
    @allure.title("创建区域")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_03_create_area(self):
        ''' 登录 '''
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        ''' 创建区域 '''
        lm = Seat_area_manage(self.driver)
        lm.create_area("区域测试")
        # 断言
        assert_messg = lm.assert_create_area()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'已保存'
            assert assert_messg[1] == u'区域测试'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))

    @allure.story("座位")  # 模块名称
    @allure.title("删除区域")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_04_delete_area(self):
        ''' 登录 '''
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(0.5)
        ''' 删除区域 '''
        lm = Seat_area_manage(self.driver)
        lm.delete_area()
        time.sleep(0.5)
        # 断言
        assert_messg = lm.assert_delete_area()
        print(assert_messg)
        try:
            assert assert_messg == u'已删除'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))

if __name__ == "__main__":
        pytest.main(['-s', '-v'])  # -s输出打印信息


