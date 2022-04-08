#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：test_logout_02.py
@Author  ：周云
@Date    ：2022/2/17 10:27 
'''
import time
import pytest
from base.base_util import Baseutil
from pageobject.login_page import login_page
from pageobject.logout_page import logout_page
import allure
class Test_logout_case(Baseutil):
    @allure.story("退出")  # 模块名称
    @allure.title("退出成功")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_02_logout_sucess(self):
        ''' 登录 '''
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        ''' 退出 '''
        lm = logout_page(self.driver)
        lm.logout_mealordering_store()
        # 断言
        assert_messg = lm.assert_logout()
        print(assert_messg)
        try:
            assert assert_messg == u'登录'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
'''

if __name__ == "__main__":
    pytest.main(['-s', '-v'])  # -s输出打印信息
'''