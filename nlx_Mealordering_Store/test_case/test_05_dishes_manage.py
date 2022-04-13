#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：test_dishes_manage_05.py
@Author  ：周云
@Date    ：2022/2/28 16:00 
'''
import time
import pytest
from base.base_util import Baseutil
from pageobject.login_page import login_page
from pageobject.dishes_manage import dishes_manage
import allure

class Test_dishes_manage(Baseutil):
    @allure.story("菜品管理")  # 模块名称
    @allure.title("创建菜品分类")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_10_create_classify(self):
        #登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        #创建菜品分类
        ln = dishes_manage(self.driver)
        ln.create_classify("菜品分类测试")
        time.sleep(2)
        # 断言
        assert_messg = ln.assert_create_classify()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'增加菜品分类成功'
            assert assert_messg[1] == u'菜品分类测试'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(4)

    @allure.story("菜品管理")  # 模块名称
    @allure.title("删除菜品分类")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_11_delete_classify(self):
        #登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        #删除菜品分类
        lm = dishes_manage(self.driver)
        lm.delete_classify()
        time.sleep(2)
        # 断言
        assert_messg = lm.assert_delete_classify()
        print(assert_messg)
        try:
            assert assert_messg == u'删除菜品分类成功'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(4)

    @allure.story("菜品管理")  # 模块名称
    @allure.title("新建菜品")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_12_create_dishes(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 创建菜品
        lq = dishes_manage(self.driver)
        lq.create_dishes("菜品测试","0.1","规格测试","属性测试","0.1")
        time.sleep(2)
        # 断言
        assert_messg = lq.assert_create_dishes()
        print(assert_messg)
        try:
            assert assert_messg == u'菜品测试'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(4)

    @allure.story("菜品管理")  # 模块名称
    @allure.title("下架菜品")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_13_pull_off_dishes(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 下架菜品
        la = dishes_manage(self.driver)
        la.pull_off_dishes()
        time.sleep(2)
        # 断言
        assert_messg = la.assert_pull_off_dishes()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'菜品下架成功'
            assert assert_messg[1] == u'下架'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(2)

    @allure.story("菜品管理")  # 模块名称
    @allure.title("上架菜品")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_14_put_on_dishes(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 下架菜品
        lb = dishes_manage(self.driver)
        lb.put_on_dishes()
        time.sleep(2)
        # 断言
        assert_messg = lb.assert_put_on_dishes()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'菜品上架成功'
            assert assert_messg[1] == u'上架'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(2)

    @allure.story("菜品管理")  # 模块名称
    @allure.title("售罄菜品")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_15_sale_out_dishes(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 售罄菜品
        lc = dishes_manage(self.driver)
        lc.sale_out_dishes()
        time.sleep(0.5)
        # 断言
        assert_messg = lc.assert_sale_out_dishes()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'编辑菜品成功'
            assert assert_messg[1] == u'可售'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(5)

    @allure.story("菜品管理")  # 模块名称
    @allure.title("可售菜品")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_16_sale_on_dishes(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 可售菜品
        lc = dishes_manage(self.driver)
        lc.sale_on_dishes()
        time.sleep(2)
        # 断言
        assert_messg = lc.assert_sale_on_dishes()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'编辑菜品成功'
            assert assert_messg[1] == u'售罄'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(5)

    @allure.story("菜品管理")  # 模块名称
    @allure.title("删除菜品")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_17_delete_dishes(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 下架菜品
        le = dishes_manage(self.driver)
        le.pull_off_dishes()
        time.sleep(2)
        # 删除菜品
        ld = dishes_manage(self.driver)
        ld.delete_dishes()
        time.sleep(0.5)
        # 断言
        assert_messg = ld.assert_delete_dishes()
        print(assert_messg)
        try:
            assert assert_messg == u'删除菜品成功'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(5)