'''
@TIME:2021-12-27
@AUTH:ZHOUYUN
'''
from selenium.webdriver.common.by import By
from base.base_page import basepage
from pageobject.login_manage_page import login_manage_page
import time
import selenium

class set_sale_page(basepage):
    # 页面元素
    # 首页点击导航栏商品管理按钮
    navigation_loc = (By.XPATH, "//span[text() ='商品管理']")
    goods_list_loc = (By.XPATH, "//span[text() ='商品列表']")
    # 商品列表界面元素
    # 1.上下架按钮元素
    sale_button_loc = (By.CLASS_NAME, "el-switch__core")
    # 2.上下架校验
    sale_status_loc = (By.XPATH, "//div[2]/p[text() ='修改成功']")
    #强制上下架
    #1.强制下架
    sale_out_loc = (By.XPATH, "//span[text() ='强制下架']")
    #2.确认下架
    reason_loc = (By.XPATH, "//input[@placeholder='请输入下架原因']")
    confirm_sale_out_loc = (By.XPATH, "//div[3]/button[2]/span[contains(text(),'确 定')]")
    #3.校验下架
    confirm_sale_status_loc = (By.XPATH, "//button[4]/span[contains(text(),'解除强制下架')]")
    #4.强制上架
    sale_on_loc = (By.XPATH, "//button[4]/span[contains(text(),'解除强制下架')]")
    #5.确认强制上架
    confirm_sale_on_loc = (By.XPATH, "//div[2]/button[2]/span[contains(text() ,'确 定')]")

    # 页面操作
    #上架操作
    def set_sale_status(self):
        # 登录
        lp = login_manage_page(self.driver)
        lp.login_manage("zytest", "zytest123")
        time.sleep(2)
        self.locator_click(set_sale_page.navigation_loc)
        time.sleep(2)
        self.locator_click(set_sale_page.goods_list_loc)
        time.sleep(2)
        set_sale_list =self.locator_elements(set_sale_page.sale_button_loc)
        print(len(set_sale_list))
        print(set_sale_list[0].text)
        if len(set_sale_list) > 0:
            set_sale_list[0].click()
        else:
            print("商品无法进行上/下架操作！")

    #上架校验
    def assert_sale_status(self):
        return self.get_value(set_sale_page.sale_status_loc)

    #强制下架
    def confirm_sale_out(self,reason):
        self.locator_click(set_sale_page.navigation_loc)
        time.sleep(2)
        self.locator_click(set_sale_page.goods_list_loc)
        time.sleep(2)
        confirm_sale_out_list =self.locator_elements(set_sale_page.sale_out_loc)
        self.execute_down()
        time.sleep(2)
        print(len(confirm_sale_out_list))
        print(confirm_sale_out_list[0].text)
        if len(confirm_sale_out_list) > 0:
            time.sleep(2)
            confirm_sale_out_list[0].click()
            time.sleep(2)
        else:
            print('页面列表不存在已上架的商品')
        self.locator_value(set_sale_page.reason_loc,reason)
        time.sleep(2)
        self.locator_click(set_sale_page.confirm_sale_out_loc)
        time.sleep(5)

    #强制下架后校验
    def assert_confirm_sale_out(self):
        return self.locator_element(set_sale_page.confirm_sale_status_loc).text

    #强制上架
    def confirm_sale_on(self):
        self.locator_click(set_sale_page.navigation_loc)
        time.sleep(2)
        self.locator_click(set_sale_page.goods_list_loc)
        time.sleep(2)
        confirm_sale_on_list = self.locator_elements(set_sale_page.sale_on_loc)
        print(len(confirm_sale_on_list))
        print(confirm_sale_on_list[0].text)
        if len(confirm_sale_on_list) > 0:
            confirm_sale_on_list[0].click()
            time.sleep(2)
        else:
            print('页面列表不存在强制下架的商品')
        self.locator_click(set_sale_page.confirm_sale_on_loc)
    #强制上架后校验
    def assert_confirm_sale_on(self):
        return self.locator_element(set_sale_page.sale_out_loc).text