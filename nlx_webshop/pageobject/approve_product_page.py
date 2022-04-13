'''
@TIME:2021-12-27
@AUTH:ZHOUYUN
'''
from selenium.webdriver.common.by import By
from base.base_page import basepage
from pageobject.login_manage_page import login_manage_page
import time


class approve_product_page(basepage):
    # 页面元素
    # 首页点击导航栏商品管理按钮
    navigation_loc = (By.XPATH, "//span[text() ='商品管理']")
    goods_list_loc = (By.XPATH, "//span[text() ='商品列表']")
    # 商品列表界面元素
    # 1.商品名称
    goods_name_loc = (By.XPATH, "//p[text() ='web自动化测试商品']")
    # 2.审核按钮
    approve_loc = (By.XPATH, "//button[4]/span[contains(text(),'审核')]")
   #3.审核确认
    confirm_loc = (By.CLASS_NAME, "el-form-item__content")
    select_confirm_loc = (By.XPATH,"//div[3]/div/button[2]/span[contains(text(),'确 定')]")
    #4.审核校验
    assert_loc = (By.XPATH,"//p[1][contains(text(), '审核通过')]")

    # 页面操作
    def approve_product(self):
        #登录
        lp = login_manage_page(self.driver)
        lp.login_manage("zytest", "zytest123")
        time.sleep(2)
        self.locator_click(approve_product_page.navigation_loc)
        time.sleep(2)
        self.locator_click(approve_product_page.goods_list_loc)
        time.sleep(2)
        approve_list =self.locator_elements(approve_product_page.approve_loc)
        #print(len(approve_list))
        #print(approve_list[0].text)
        if len(approve_list) > 0:
            approve_list[0].click()
        else:
            print("商品已完成审核！")
        time.sleep(2)
        self.locator_element(approve_product_page.confirm_loc)
        self.locator_click(approve_product_page.select_confirm_loc)
        time.sleep(2)

    def assert_approve_product(self):
        time.sleep(3)
        product_value_list =self.locator_elements(approve_product_page.assert_loc)
        #print(len(product_value_list))
        #print(product_value_list[0].text)
        if len(product_value_list) > 0:
            return product_value_list[0].text
        else:
            print("商品未审核")
