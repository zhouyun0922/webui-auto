#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：home_manage.py
@Author  ：周云
@Date    ：2022/3/2 9:28 
'''
import time
from base.base_page import basepage
from selenium.webdriver.common.by import By


class home_manage(basepage):
    # 页面元素
    # 首页座位添加购物车、下单元素
    home_loc = (By.XPATH, "//span[2][text() = '首页']")
    tale_no_loc = (By.XPATH, "//div[2]/div[2][text() = 'test01']")
    number_diners_loc = (By.CSS_SELECTOR, "div.num_unit___1onXj:nth-child(2)")
    spec_loc = (By.XPATH,"//span[text() = '选规格']")
    select_spec_loc = (By.XPATH, "//span[text() = '属性测试']")
    add_cart_loc = (By.XPATH, "//span[text() = '添 加']")
    order_loc = (By.XPATH, "//span[text() = '下单打印小票']")
    #校验下单成功元素
    assert_order_loc = (By.XPATH,"//span[2][text() = '已保存']")
    assert_order_table_status_loc = (By.XPATH, "//div[1][text() = '就餐']")
    assert_order_status_loc = (By.XPATH, "//div[2]/div[2][text() = 'test01']/../div[3]/span[2][text() = '已下单']")
    assert_pay_status_loc = (By.XPATH, "//div[2]/div[2][text() = 'test01']/../div[4]/span[2][text() = '未支付']")
    #修改已生成的订单元素
    edit_loc = (By.XPATH, "//button[2]/span[text() = '修 改']")
    edit_num_loc = (By.CSS_SELECTOR, ".anticon-plus-circle > svg:nth-child(1)")
    confirm_edit_loc = (By.XPATH,"//div[3]/div[2]/button/span[text() = '确认修改']")
    #校验订单修改成功元素
    assert_edit_order_loc = (By.XPATH,"//div/span[2][text() = '已保存']")
    assert_edit_num_loc = (By.XPATH, "//div[2]/div[2][text() = 'x ' and text() ='2']")
    assert_order_price_loc = (By.XPATH, "//div[1]/div[2][text() = '¥' and text() ='0.20']")
    #加菜元素
    add_food_loc = (By.XPATH, "//button[2]/span[text() = '加 菜']")
    #校验加菜元素
    assert_add_order_loc = (By.XPATH,"//div/span[2][text() = '已保存']")
    assert_add_tab_loc = (By.XPATH, "//span[text() = '加菜']")
    assert_add_dishes_loc = (By.XPATH, "//span[text() = '加菜']/../../div[3]/div[1]/div[1]/div[2]/div[1][text() = '菜品测试 属性测试']")
    assert_small_all_tickets_loc = (By.XPATH, "//span[text() = '打印全部小票']")
    # 打印小票元素
    small_all_tickets_loc = (By.XPATH, "//span[text() = '打印全部小票']")
    small_ticket_loc = (By.XPATH, "//span[text() = '打印小票']")
    confirm_small_loc = (By.XPATH, "//span[text() = '确 认']")
    # 结账元素
    check_loc = (By.XPATH, "//span[text() = '结 账']")
    pay_amount_loc = (By.CSS_SELECTOR, "#payAmount")
    remark_loc = (By.CSS_SELECTOR, "#remark")
    confirm_check_loc = (By.XPATH, "//span[text() = '提 交']")
    confirm01_loc = (By.XPATH, "//span[text() = '确 定']")
    # 校验结账元素
    assert_check_loc = (By.XPATH, "//span[2][text() = '已保存']")
    assert_check_status_loc = (By.XPATH, "//div[2]/div[2][text() = 'test01']/../div[4]/span[2][text() = '已支付']")
    # 发生退款元素
    refund_loc = (By.XPATH, "//span[text() = '发生退款']")
    refund_amount_loc = (By.CSS_SELECTOR, "#refundAmount")
    reason_loc = (By.CSS_SELECTOR, "#reason")
    confirm_refund_loc = (By.XPATH, "//span[text() = '提 交']")
    confirm02_loc = (By.XPATH, "//span[text() = '确 定']")
    # 校验退款元素
    assert_refund_amount_tab_loc = (By.XPATH, "//span[1][text() = '退款金额：']")
    assert_refund_amount_price_loc = (By.XPATH, "//span[2][text() = '0.10' ]")
    assert_refund_reason_tab_loc = (By.XPATH, "//span[1][text() = '退款原因：']")
    assert_refund_reason_loc = (By.XPATH, "//span[2][text() = '线下退款']")
    # 翻台元素
    rockover_table_loc = (By.XPATH, "//span[text() = '翻 台']")
    confirm_rockover_loc = (By.XPATH, "//button[2]/span[text() = '确 定']")
    # 校验翻台元素
    assert_rockover_table_loc = (By.XPATH, "//span[2][text() = '已保存']")
    assert_table_status_loc = (By.XPATH, "//div[1][text() = '可供']")

    # 商家端添加购物车并下单
    def order_store(self):
        time.sleep(3)
        self.locator_click(home_manage.home_loc)
        time.sleep(3)
        self.locator_click(home_manage.tale_no_loc)
        time.sleep(3)
        self.locator_click(home_manage.number_diners_loc)
        time.sleep(3)
        self.locator_click(home_manage.spec_loc)
        time.sleep(3)
        self.locator_click(home_manage.select_spec_loc)
        time.sleep(3)
        self.locator_click(home_manage.add_cart_loc)
        time.sleep(5)
        self.locator_click(home_manage.order_loc)
    # 校验商家端添加购物车并下单
    def assert_order_store(self):
        time.sleep(3)
        assert_messg01 = self.get_value(home_manage.assert_order_loc)
        time.sleep(2)
        assert_messg02 = self.get_value(home_manage.assert_order_table_status_loc)
        time.sleep(3)
        assert_messg03 = self.get_value(home_manage.assert_order_status_loc)
        time.sleep(3)
        assert_messg04 = self.get_value(home_manage.assert_pay_status_loc)
        messg =[assert_messg01,assert_messg02,assert_messg03,assert_messg04]
        return messg
    # 修改已生成的订单
    def edit_order(self):
        time.sleep(3)
        self.locator_click(home_manage.home_loc)
        time.sleep(3)
        self.locator_click(home_manage.tale_no_loc)
        time.sleep(3)
        self.locator_click(home_manage.edit_loc)
        time.sleep(3)
        self.locator_click(home_manage.edit_num_loc)
        time.sleep(3)
        self.locator_click(home_manage.confirm_edit_loc)
    # 校验修改已生成的订单
    def assert_edit_order(self):
        time.sleep(3)
        assert_messg01 = self.get_value(home_manage. assert_edit_order_loc)
        time.sleep(2)
        assert_messg02 = self.get_value(home_manage.assert_edit_num_loc)
        time.sleep(1)
        assert_messg03 = self.get_value(home_manage.assert_order_price_loc)
        messg =[assert_messg01,assert_messg02,assert_messg03]
        return messg
    # 加菜
    def add_food(self):
        time.sleep(3)
        self.locator_click(home_manage.home_loc)
        time.sleep(3)
        self.locator_click(home_manage.tale_no_loc)
        time.sleep(3)
        self.locator_click(home_manage.add_food_loc)
        time.sleep(3)
        self.locator_click(home_manage.spec_loc)
        time.sleep(3)
        self.locator_click(home_manage.select_spec_loc)
        time.sleep(3)
        self.locator_click(home_manage.add_cart_loc)
        time.sleep(3)
        self.locator_click(home_manage.order_loc)
    # 校验加菜
    def assert_add_food(self):
        time.sleep(3)
        assert_messg01 = self.get_value(home_manage. assert_add_order_loc)
        time.sleep(2)
        assert_messg02 = self.get_value(home_manage.assert_add_tab_loc)
        time.sleep(3)
        assert_messg03 = self.get_value(home_manage.assert_add_dishes_loc)
        time.sleep(3)
        assert_messg04 = self.get_value(home_manage.assert_small_all_tickets_loc)
        messg =[assert_messg01,assert_messg02,assert_messg03,assert_messg04]
        return messg
    # 结账
    def check_order(self,payamount,remark):
        time.sleep(3)
        self.locator_click(home_manage.home_loc)
        time.sleep(3)
        self.locator_click(home_manage.tale_no_loc)
        time.sleep(3)
        self.locator_click(home_manage.check_loc)
        time.sleep(3)
        self.locator_value(home_manage.pay_amount_loc,payamount)
        time.sleep(3)
        self.locator_value(home_manage.remark_loc,remark)
        time.sleep(3)
        self.locator_click(home_manage.confirm_check_loc)
        time.sleep(3)
        self.locator_click(home_manage.confirm01_loc)
    # 校验结账
    def assert_check_order(self):
        time.sleep(3)
        assert_messg01 = self.get_value(home_manage.assert_check_loc)
        time.sleep(2)
        assert_messg02 = self.get_value(home_manage.assert_check_status_loc)
        messg =[assert_messg01,assert_messg02]
        return messg
    # 发生退款
    def refund_order(self,refundamount,reason):
        time.sleep(3)
        self.locator_click(home_manage.home_loc)
        time.sleep(3)
        self.locator_click(home_manage.tale_no_loc)
        time.sleep(3)
        self.locator_click(home_manage.refund_loc)
        time.sleep(3)
        self.locator_value(home_manage.refund_amount_loc,refundamount)
        time.sleep(3)
        self.locator_value(home_manage.reason_loc,reason)
        time.sleep(3)
        self.locator_click(home_manage.confirm_refund_loc)
        time.sleep(3)
        self.locator_click(home_manage.confirm02_loc)
    # 校验发生退款
    def assert_refund_order(self):
        time.sleep(3)
        assert_messg01 = self.get_value(home_manage.assert_refund_amount_tab_loc)
        time.sleep(3)
        assert_messg02 = self.get_value(home_manage.assert_refund_amount_price_loc)
        time.sleep(3)
        assert_messg03 = self.get_value(home_manage.assert_refund_reason_tab_loc)
        time.sleep(3)
        assert_messg04 = self.get_value(home_manage.assert_refund_reason_loc)
        messg =[assert_messg01,assert_messg02,assert_messg03,assert_messg04]
        return messg
    # 翻台
    def rockover_table(self):
        time.sleep(3)
        self.locator_click(home_manage.home_loc)
        time.sleep(3)
        self.locator_click(home_manage.tale_no_loc)
        time.sleep(3)
        self.locator_click(home_manage.rockover_table_loc)
        time.sleep(3)
        self.locator_click(home_manage.confirm_rockover_loc)
    # 校验翻台
    def assert_rockover_table(self):
        time.sleep(3)
        assert_messg01 = self.get_value(home_manage.assert_rockover_table_loc)
        time.sleep(2)
        assert_messg02 = self.get_value(home_manage.assert_table_status_loc)
        messg =[assert_messg01,assert_messg02]
        return messg