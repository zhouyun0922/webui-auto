#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：dishes_manage.py
@Author  ：周云
@Date    ：2022/2/25 11:52 
'''
import time
from base.base_page import basepage
from selenium.webdriver.common.by import By
from base.uplaod import uplaod_file

class dishes_manage(basepage):
    # 页面元素
    # 创建菜品分类元素
    dishes_loc = (By.XPATH, "//span[2][text()='菜品']")
    classify_loc = (By.XPATH, "//span[2][text()='菜品分类']")
    create_classify_loc = (By.XPATH, "//span[text()='新建分类']")
    classify_name_loc = (By.XPATH,"//*[@id='basic_name']")
    save_loc = (By.XPATH, "//span[text()='保 存']")
    #校验菜品分类添加成功元素
    assert_create_classify_loc = (By.XPATH,"//span[2][text()='增加菜品分类成功']")
    assert_classify_name_loc = (By.XPATH, "//tr[2]/td[2][text()='菜品分类测试']")
    #删除分类元素
    delete_classify_name_loc = (By.XPATH, "//tr[2]/td[2][text()='菜品分类测试']")
    delete_classify_loc = (By.XPATH, "//tr[2]/td[2][text()='菜品分类测试']/../td[3]/div/div[2]/span[@class='anticon icon___2Mb1s']")
    confirm_delete_loc = (By.XPATH,"//div[2]/button[2]/span[text()='确 认']")
    #校验删除分类成功元素
    assert_delete_classify_loc = (By.XPATH, "//span[2][text()='删除菜品分类成功']")
    #新建菜品元素
    dishes_manage_loc = (By.XPATH, "//span/span[2][text()='菜品管理']")
    create_dishes_loc = (By.XPATH, "//button/span[text()='新建菜品']")
    dishes_classify_loc = (By.XPATH, "//div[1]/div[2]/div/div/div/div/div[@class='ant-select-selection-overflow']")
    select_dishes_classify_loc = (By.XPATH,"//div[1]/div[text()='菜品分类测试']")
    dishes_name_loc = (By.XPATH,"//*[@placeholder='请输入菜品名称']")
    upload_pic01_loc = (By.XPATH, "//div[text()='上传头图']")
    upload_pic02_loc = (By.XPATH, "//div[text()='上传']")
    dishes_price_loc = (By.XPATH,"//*[@placeholder='请输入菜品价格']")
    add_spec_loc = (By.XPATH, "//button/span[text()='添 加']")
    spec_name_loc = (By.XPATH, "//*[@id='specName']/div[1]/input[@value='规格1']")
    spec_attribute_loc = (By.XPATH, "//div/div/div/div/div[1]/div/div[1]/input[@class ='ant-input']")
    spec_price_loc = (By.XPATH, "//div/div/div/div/div[1]/div/div[2]/input[@class ='ant-input']")
    spec_submit_loc = (By.XPATH, "//button[2]/span[text()='提 交']")
    submit_loc = (By.XPATH, "//button/span[text()='提 交']")
    #校验菜品添加成功元素
    assert_create_dishes_loc = (By.XPATH,"//span[2][text()='增加菜品成功']")
    paging_loc = (By.XPATH, "//div/div/ul/li[3][@title ='2']")
    assert_dishes_loc = (By.XPATH, "//div[text()='菜品测试']")
    assert_dishes_name_loc = (By.XPATH, "//div[text()='菜品测试']/../../../..//td[4]/div/div[2]/div[text()='菜品测试']")
    #菜品下架元素
    dishes_list_loc = (By.XPATH,"//div[text()='菜品测试']")
    pull_off_loc = (By.XPATH, "//div[text()='菜品测试']/../../../../td[10]/div/div[2]/button/span[text()='下架']")
    confirm_pull_off_loc = (By.XPATH, "//div[2]/button[2]/span[text()='确 认']")
    # 校验菜品下架结果
    off_tab_loc = (By.CSS_SELECTOR, "div.ant-tabs-tab:nth-child(2)")
    off_dishes_name_loc = (By.XPATH, "//div[text()='菜品测试']")
    assert_off_dishes_status_loc = (By.XPATH, "//div[text()='菜品测试']/../../../../td[6][text()='下架']")
    assert_off_dishes_loc = (By.XPATH, "//div/span[2][text()='菜品下架成功']")
    # 菜品上架元素
    put_on_loc = (By.XPATH, "//div[text()='菜品测试']/../../../../td[10]/div/div[3]/button/span[text()='上架']")
    confirm_put_on_loc = (By.XPATH, "//div[2]/button[2]/span[text()='确 认']")
    # 校验菜品上架结果
    on_tab_loc = (By.CSS_SELECTOR, "div.ant-tabs-tab:nth-child(1)")
    on_dishes_name_loc = (By.XPATH, "//div[text()='菜品测试']")
    assert_on_dishes_status_loc = (By.XPATH, "//div[text()='菜品测试']/../../../../td[6][text()='上架']")
    assert_on_dishes_loc = (By.XPATH, "//div/span[2][text()='菜品上架成功']")
    # 菜品售罄元素
    sale_out_loc = (By.XPATH, "//div[text()='菜品测试']/../../../../td[10]/div/div[1]/button/span[text()='售罄']")
    set_sale_out_loc = (By.XPATH, "//div/div[2][text()='设为售罄']")
    confirm_sale_out_loc = (By.XPATH, "//div[2]/button[2]/span[text()='确 认']")
    confirm_01_loc = (By.XPATH, "//div[3]/button[2]/span[text()='确 定']")
    # 校验菜品售罄结果元素
    assert_sale_out_loc = (By.XPATH, "//div/span[2][text()='编辑菜品成功']")
    assert_sale_out_status_loc = (By.XPATH, "//div[text()='菜品测试']/../../../../td[10]/div/div[1]/button/span[text()='可售']")
    # 恢复可售元素
    sale_on_loc = (By.XPATH, "//div[text()='菜品测试']/../../../../td[10]/div/div[1]/button/span[text()='可售']")
    set_sale_on_loc = (By.XPATH, "//div/div[2][text()='设为可售']")
    confirm_sale_on_loc = (By.XPATH, "//div[2]/button[2]/span[text()='确 认']")
    confirm_02_loc = (By.XPATH, "//div[3]/button[2]/span[text()='确 定']")
    # 校验恢复可售结果元素
    assert_sale_on_loc = (By.XPATH, "//div/span[2][text()='编辑菜品成功']")
    assert_sale_on_status_loc = (By.XPATH, "//div[text()='菜品测试']/../../../../td[10]/div/div[1]/button/span[text()='售罄']")
    # 删除菜品元素
    delete_dishes_loc = (By.XPATH, "//div[text()='菜品测试']/../../../../td[10]/div/div[4]/button/span[text()='删除']")
    confirm_delete_dishes_loc = (By.XPATH, "//div[2]/button[2]/span[text()='确 认']")
    # 校验删除结果元素
    assert_delete_dishes_loc = (By.XPATH, "//div/span[2][text()='删除菜品成功']")
    # 创建菜品分类
    def create_classify(self,classify_name):
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_loc)
        time.sleep(2)
        self.locator_click(dishes_manage.classify_loc)
        time.sleep(2)
        self.locator_click(dishes_manage.create_classify_loc)
        time.sleep(2)
        self.locator_value(dishes_manage.classify_name_loc, classify_name)
        time.sleep(2)
        self.locator_click(dishes_manage.save_loc)
        time.sleep(1)
    # 校验菜品分类
    def assert_create_classify(self):
        messg =[self.get_value(dishes_manage.assert_create_classify_loc),self.get_value(dishes_manage.assert_classify_name_loc)]
        return messg
    # 删除菜品分类
    def delete_classify(self):
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_loc)
        time.sleep(2)
        self.locator_click(dishes_manage.classify_loc)
        time.sleep(2)
        classify_list = self.locator_elements(dishes_manage.delete_classify_name_loc)
        print(len(classify_list))
        if len(classify_list) > 0:
            self.locator_click(dishes_manage.delete_classify_loc)
            time.sleep(2)
            self.locator_click(dishes_manage.confirm_delete_loc)
        else:
            print("分类不存在！")

    # 校验删除分类成功元素
    def assert_delete_classify(self):
        return self.get_value(dishes_manage.assert_delete_classify_loc)

    # 新建菜品
    def create_dishes(self,dishes_name,dishes_price,spec_name,spec_attribute,spec_price):
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_loc)
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_manage_loc)
        time.sleep(2)
        self.locator_click(dishes_manage.create_dishes_loc)
        time.sleep(4)
        self.locator_click(dishes_manage.dishes_classify_loc)
        time.sleep(2)
        self.locator_click(dishes_manage.select_dishes_classify_loc)
        time.sleep(2)
        self.locator_value(dishes_manage.dishes_name_loc, dishes_name)
        time.sleep(4)
        self.locator_click(dishes_manage.upload_pic01_loc)
        time.sleep(8)
        uplaod_file('1.jpg')
        time.sleep(8)
        self.locator_click(dishes_manage.upload_pic02_loc)
        time.sleep(10)
        uplaod_file('2.jpg')
        time.sleep(10)
        self.locator_value(dishes_manage.dishes_price_loc, dishes_price)
        time.sleep(4)
        self.locator_click(dishes_manage.add_spec_loc)
        time.sleep(4)
        self.locator_value(dishes_manage.spec_name_loc, spec_name)
        time.sleep(4)
        self.locator_value(dishes_manage.spec_attribute_loc, spec_attribute)
        time.sleep(4)
        self.locator_value(dishes_manage.spec_price_loc, spec_price)
        time.sleep(4)
        self.locator_click(dishes_manage.spec_submit_loc)
        time.sleep(4)
        self.locator_click(dishes_manage.submit_loc)

    # 校验新建菜品结果
    def assert_create_dishes(self):
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_manage_loc)
        time.sleep(5)
        self.locator_click(dishes_manage.paging_loc)
        time.sleep(5)
        dishes_list = self.locator_elements(dishes_manage.assert_dishes_loc)
        print(len(dishes_list))
        if len(dishes_list) > 0:
            return self.get_value(dishes_manage.assert_dishes_name_loc)
        else:
            print("菜品新建失败！")

    # 下架菜品
    def pull_off_dishes(self):
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_loc)
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_manage_loc)
        time.sleep(3)
        self.locator_click(dishes_manage.paging_loc)
        time.sleep(3)
        dishes_list = self.locator_elements(dishes_manage.dishes_list_loc)
        print(len(dishes_list))
        if len(dishes_list) > 0:
            self.locator_click(dishes_manage.pull_off_loc)
            time.sleep(2)
            self.locator_click(dishes_manage.confirm_pull_off_loc)
        else:
            print("菜品不存在！")

    # 校验下架菜品结果
    def assert_pull_off_dishes(self):
        assert_messg01 = self.get_value(dishes_manage.assert_off_dishes_loc)
        time.sleep(5)
        self.locator_click(dishes_manage.off_tab_loc)
        time.sleep(3)
        assert_dishes_list =self.locator_elements(dishes_manage.dishes_list_loc)
        if len(assert_dishes_list) > 0:
            assert_messg02 = self.get_value(dishes_manage.assert_off_dishes_status_loc)
            messg = [assert_messg01, assert_messg02]
            return messg
        else:
            print("菜品下架失败！")

    # 上架菜品
    def put_on_dishes(self):
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_loc)
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_manage_loc)
        time.sleep(3)
        self.locator_click(dishes_manage.off_tab_loc)
        time.sleep(3)
        dishes_list = self.locator_elements(dishes_manage.dishes_list_loc)
        print(len(dishes_list))
        if len(dishes_list) > 0:
            self.locator_click(dishes_manage.put_on_loc)
            time.sleep(2)
            self.locator_click(dishes_manage.confirm_put_on_loc)
        else:
            print("菜品不存在！")

    # 校验上架菜品结果
    def assert_put_on_dishes(self):
        assert_messg01 = self.get_value(dishes_manage.assert_on_dishes_loc)
        time.sleep(3)
        self.locator_click(dishes_manage.on_tab_loc)
        time.sleep(3)
        self.locator_click(dishes_manage.paging_loc)
        time.sleep(3)
        assert_dishes_list = self.locator_elements(dishes_manage.on_dishes_name_loc)
        if len(assert_dishes_list) > 0:
            assert_messg02 = self.get_value(dishes_manage.assert_on_dishes_status_loc)
            messg = [assert_messg01, assert_messg02]
            return messg
        else:
            print("菜品上架失败！")

    # 设置菜品售罄
    def sale_out_dishes(self):
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_loc)
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_manage_loc)
        time.sleep(3)
        self.locator_click(dishes_manage.paging_loc)
        time.sleep(3)
        dishes_list = self.locator_elements(dishes_manage.dishes_list_loc)
        print(len(dishes_list))
        if len(dishes_list) > 0:
            self.locator_click(dishes_manage.sale_out_loc)
            time.sleep(2)
            self.locator_click(dishes_manage.set_sale_out_loc)
            time.sleep(2)
            self.locator_click(dishes_manage.confirm_sale_out_loc)
            time.sleep(3)
            self.locator_click(dishes_manage.confirm_01_loc)
        else:
            print("菜品不存在！")

    # 校验售罄菜品结果
    def assert_sale_out_dishes(self):
        time.sleep(2)
        assert_messg01 = self.get_value(dishes_manage.assert_sale_out_loc)
        time.sleep(3)
        assert_messg02 = self.get_value(dishes_manage.assert_sale_out_status_loc)
        messg = [assert_messg01, assert_messg02]
        return messg

    # 设置菜品可售
    def sale_on_dishes(self):
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_loc)
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_manage_loc)
        time.sleep(3)
        self.locator_click(dishes_manage.paging_loc)
        time.sleep(3)
        dishes_list = self.locator_elements(dishes_manage.dishes_list_loc)
        print(len(dishes_list))
        if len(dishes_list) > 0:
            self.locator_click(dishes_manage.sale_on_loc)
            time.sleep(2)
            self.locator_click(dishes_manage.set_sale_on_loc)
            time.sleep(2)
            self.locator_click(dishes_manage.confirm_sale_on_loc)
            time.sleep(5)
            self.locator_click(dishes_manage.confirm_02_loc)
        else:
            print("菜品不存在！")

    # 校验可售菜品结果
    def assert_sale_on_dishes(self):
        assert_messg01 = self.get_value(dishes_manage.assert_sale_on_loc)
        time.sleep(2)
        assert_messg02 = self.get_value(dishes_manage.assert_sale_on_status_loc)
        messg = [assert_messg01, assert_messg02]
        return messg

    # 删除菜品
    def delete_dishes(self):
        time.sleep(2)
        self.locator_click(dishes_manage.dishes_manage_loc)
        time.sleep(3)
        self.locator_click(dishes_manage.off_tab_loc)
        time.sleep(3)
        dishes_list = self.locator_elements(dishes_manage.dishes_list_loc)
        print(len(dishes_list))
        if len(dishes_list) > 0:
            self.locator_click(dishes_manage.delete_dishes_loc)
            time.sleep(2)
            self.locator_click(dishes_manage.confirm_delete_dishes_loc)
            time.sleep(2)
        else:
            print("菜品不存在！")

    # 校验删除菜品结果
    def assert_delete_dishes(self):
        messg = self.get_value(dishes_manage.assert_delete_dishes_loc)
        return messg












