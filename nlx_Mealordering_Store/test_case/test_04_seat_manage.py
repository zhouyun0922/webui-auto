#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：test_seat_manage_04.py
@Author  ：周云
@Date    ：2022/2/21 10:03 
'''
import time
import pytest
from base.base_util import Baseutil
from pageobject.login_page import login_page
from pageobject.seat_area_manage import Seat_area_manage
from pageobject.seat_manage import Seat_manage
import allure

#@pytest.mark.usefixtures('base_util')
class Test_seat_case(Baseutil):
    @allure.story("座位")  # 模块名称
    @allure.title("创建座位")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_05_create_seat(self):
        ''' 登录 '''
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        '''创建区域'''
        lm = Seat_area_manage(self.driver)
        lm.create_area("区域测试")
        time.sleep(2)
        '''创建座位'''
        ln = Seat_manage(self.driver)
        ln.create_seat("test01","10")
        time.sleep(2)
        # 断言
        assert_messg = ln.assert_create_seat()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'已保存'
            assert assert_messg[1] == u'test01'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))

    @allure.story("座位")  # 模块名称
    @allure.title("删除座位")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_06_delete_seat(self):
        ''' 登录 '''
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        '''删除座位'''
        lw = Seat_manage(self.driver)
        lw.delete_seat()
        time.sleep(2)
        # 断言
        assert_messg = lw.assert_delete_seat()
        print(assert_messg)
        try:
            assert assert_messg == u"已删除"
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))

    @allure.story("座位")  # 模块名称
    @allure.title("下载单个座位二维码")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_07_download_seat(self):
        '''登录'''
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        '''下载单个座位二维码'''
        lc = Seat_manage(self.driver)
        lc.download_seat()
        time.sleep(2)
        # 断言
        lc.assert_download_seat()

    @allure.story("座位")  # 模块名称
    @allure.title("批量下载座位二维码")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_08_download_seats(self):
        '''登录'''
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        '''批量下载座位二维码'''
        ld = Seat_manage(self.driver)
        ld.download_seats()
        time.sleep(2)
        # 断言
        ld.assert_download_seats()

    @allure.story("座位")  # 模块名称
    @allure.title("批量下载座位二维码编码")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_09_download_seatcodes(self):
        '''登录'''
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        '''批量下载座位二维码编码'''
        ln = Seat_manage(self.driver)
        ln.download_seatcodes()
        time.sleep(2)
        # 断言
        ln.assert_download_seatcodes()

if __name__ == "__main__":
    pytest.main(['-s', '-v'])  # -s输出打印信息
