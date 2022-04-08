#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：test_login_01.py
@Author  ：周云
@Date    ：2022/2/15 15:02 
'''
import pytest
import time
from base.base_util import Baseutil
from pageobject.login_page import login_page
import allure


class Test_login_case(Baseutil):
    @allure.story("登录")  # 模块名称
    @allure.title("登录成功")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_01_login_sucess(self):
        ''' 登录 '''
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest1234")
        time.sleep(2)
        # 断言
        assert_messg = lp.assert_login()
        print(assert_messg)
        try:
            assert assert_messg == u'退出'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
'''
if __name__ == "__main__":
        pytest.main(['-s', '-v'])  # -s输出打印信息
'''
