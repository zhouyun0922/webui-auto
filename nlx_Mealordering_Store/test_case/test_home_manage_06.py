#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：test_home_manage_06.py
@Author  ：周云
@Date    ：2022/3/2 9:29 
'''
import time
import pytest
from base.base_util import Baseutil
from pageobject.home_manage import home_manage
from pageobject.login_page import login_page
from pageobject.seat_area_manage import Seat_area_manage
from pageobject.seat_manage import Seat_manage
from pageobject.dishes_manage import dishes_manage
import allure

class Test_home_manage(Baseutil):
    '''预置步骤'''
    '''
    @allure.story("首页")  # 模块名称
    @allure.title("预置条件：创建座位")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_05_create_seat(self):
        #登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(0.5)
        #创建区域
        lm = Seat_area_manage(self.driver)
        lm.create_area("区域测试")
        time.sleep(0.5)
        #创建座位
        ln = Seat_manage(self.driver)
        ln.create_seat("test01", "10")
        time.sleep(0.5)
        # 断言
        assert_messg = ln.assert_create_seat()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'已保存'
            assert assert_messg[1] == u'test01'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
    
    @allure.story("首页")  # 模块名称
    @allure.title("预置条件：新建菜品分类")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_create_classify(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(0.5)
        #创建菜品分类
        la = dishes_manage(self.driver)
        la.create_classify("菜品分类测试")
        time.sleep(0.5)
        # 断言
        assert_messg = la.assert_create_classify()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'增加菜品分类成功'
            assert assert_messg[1] == u'菜品分类测试'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(2)

    @allure.story("首页")  # 模块名称
    @allure.title("预置条件：新建菜品")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_create_dishes(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(0.5)
        # 创建菜品
        lb = dishes_manage(self.driver)
        lb.create_dishes("菜品测试", "0.1", "规格测试", "属性测试", "0.1")
        time.sleep(0.5)
        # 断言
        assert_messg = lb.assert_create_dishes()
        print(assert_messg)
        try:
            assert assert_messg == u'菜品测试'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(2)
    '''
    @allure.story("首页")  # 模块名称
    @allure.title("商家端添加购物车并下单")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_18_order_store(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 商家端添加购物车并下单
        lc = home_manage(self.driver)
        lc.order_store()
        time.sleep(2)
        # 断言
        assert_messg = lc.assert_order_store()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'已保存'
            assert assert_messg[1] == u'就餐'
            assert assert_messg[2] == u'已下单'
            assert assert_messg[3] == u'未支付'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(2)

    @allure.story("首页")  # 模块名称
    @allure.title("修改订单")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_19_edit_order(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 修改订单
        lc = home_manage(self.driver)
        lc.edit_order()
        time.sleep(2)
        # 断言
        assert_messg = lc.assert_edit_order()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'已保存'
            assert assert_messg[1] == u'就餐'
            assert assert_messg[2] == u'已下单'
            assert assert_messg[3] == u'未支付'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(2)

    @allure.story("首页")  # 模块名称
    @allure.title("订单加菜")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_20_add_food(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 加菜
        ld = home_manage(self.driver)
        ld.add_food()
        time.sleep(2)
        # 断言
        assert_messg = ld.assert_add_food()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'已保存'
            assert assert_messg[1] == u'加菜'
            assert assert_messg[2] == u'菜品测试 属性测试'
            assert assert_messg[3] == u'打印全部小票'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(2)

    @allure.story("首页")  # 模块名称
    @allure.title("订单结账")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_21_check_order(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 结账
        le = home_manage(self.driver)
        le.check_order("0.3","线下支付")
        time.sleep(2)
        # 断言
        assert_messg = le.assert_check_order()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'已保存'
            assert assert_messg[1] == u'已支付'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(2)

    @allure.story("首页")  # 模块名称
    @allure.title("订单线下退款")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_22_refund_order(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 订单线下退款
        lf = home_manage(self.driver)
        lf.refund_order("0.1","线下退款")
        time.sleep(2)
        # 断言
        assert_messg = lf.assert_refund_order()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'退款金额：'
            assert assert_messg[1] == u'0.10'
            assert assert_messg[2] == u'退款原因：'
            assert assert_messg[3] == u'线下退款'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(2)

    @allure.story("首页")  # 模块名称
    @allure.title("座位翻台")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_23_rockover_table(self):
        # 登录
        lp = login_page(self.driver)
        lp.login_mealordering_store("13601455223", "zytest123")
        time.sleep(2)
        # 翻台
        lg = home_manage(self.driver)
        lg.rockover_table()
        time.sleep(2)
        # 断言
        assert_messg = lg.assert_rockover_table()
        print(assert_messg)
        try:
            assert assert_messg[0] == u'已保存'
            assert assert_messg[1] == u'可供'
            print("test pass.")
        except Exception as e:
            print("test fail.", format(e))
        time.sleep(2)