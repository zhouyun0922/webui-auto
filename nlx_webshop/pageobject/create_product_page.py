'''
@TIME:2021-12-27
@AUTH:ZHOUYUN
'''
from selenium.webdriver.common.by import By
from base.base_page import basepage
from pageobject.login_page import login_page
from pageobject.uplaod import uplaod_file
import time
import selenium

class create_product_page(basepage):
    # 页面元素
    # 首页点击导航栏商品按钮
    navigation_button_loc = (By.XPATH, "//span[text()='商品']")
    # 商品创建界面元素
    # 1.商品创建按钮
    creat_loc = (By.XPATH, "//li[text()='商品创建']")
    # 2.点击商品分类栏选择按钮
    select_loc = (By.XPATH, "//div[1]/div/div/div[1]/input[@placeholder='请选择']")
    # 3.选择商品分类
    select_category_loc = (By.XPATH, "//span[text()= '牛肉类']")
    # 4.#填写商品名称
    product_name_loc = (By.XPATH, "//input[@placeholder ='请输入商品名称']")
    product_subname_loc = (By.XPATH, "//input[@placeholder ='请输入副标题']")
    # 5.点击商品品牌栏选择按钮
    brand_loc = (By.XPATH, "//input[@placeholder='请选择品牌']")
    select_brand_loc = (By.XPATH, "//span[text()= '周云专用品牌']")
    # 6.选中运费模块
    freight_loc = (By.XPATH, "//input[@placeholder ='请选择运费模版']")
    select_freight_loc = (By.XPATH, "//span[text()= '公共模板包邮']")
    # 7.设置发货地址信息
    province_loc = (By.XPATH, "//input[@placeholder ='请选择省']")
    select_province_loc = (By.XPATH, "//div[7]/div[1]/div[1]/ul/li[1]/span['北京市']")
    city_loc = (By.XPATH, "//input[@placeholder ='请选择自治州/市']")
    select_city_loc = (By.XPATH, "//div[8]/div[1]/div[1]/ul/li/span['北京市']")
    district_loc = (By.XPATH, "//input[@placeholder ='请选择区/县']")
    select_district_loc = (By.XPATH, "//span[text()='东城区']")
    street_loc = (By.XPATH, "//input[@placeholder ='请选择街道']")
    select_street_loc = (By.XPATH, "//span[text()='交道口街道办事处']")
    detail_add_loc = (By.XPATH, "//input[@placeholder ='请输入详细地址']")
    # 7.选中商品规格
    select_product_spec_loc = (By.XPATH, "//span[@class ='el-checkbox__inner']")
    # 8.填写规格信息
    sale_price_loc = (By.XPATH, "//div[4]/div[2]/table/tbody/tr/td[2]/div/div/div/div[1]/input[@type='text']")
    product_stock_loc = (By.XPATH, "//div[4]/div[2]/table/tbody/tr/td[3]/div/div/div/div[1]/input[@type='text']")
    stocks_forewarn_loc = (By.XPATH, "//div[4]/div[2]/table/tbody/tr/td[4]/div/div/div/div[1]/input[@type='text']")
    product_code_loc = (By.XPATH, "//div[4]/div[2]/table/tbody/tr/td[5]/div/div/div/div[1]/input[@type='text']")
    # 9.上传商品规格图片
    product_spec_pic_loc = (By.XPATH, "//td[6]/div/div/input[@type ='file']")
    # 10.商品售价
    product_prices_loc = (By.XPATH, "//input[@placeholder='请输入商品售价']")
    # 11.上传商品图片
    product_pic_loc = (By.XPATH, "//div[12]/div/div/div/div[1][@class='uploadBox']/input[@type='file']")
    # 12.上传第二张图片
    secend_pic_loc = (By.XPATH, "//div[12]/div/div/div/div[2]/div/span[2][text()='上传']")
    # 13.上传商品标签图片
    product_tag_loc = (By.XPATH, "//div[13]/div/div/div/div/div/span[2]['上传']")
    # 14.点击许可证选择按钮
    licence_loc = (By.XPATH, "//div[14]/div/div/div/input[@placeholder ='请选择']")
    select_licence_loc = (By.XPATH, "//span[text()='食品生产许可证']")
    # 15.填写食品许可证编码
    food_licence_loc = (By.XPATH, "//input[@placeholder='请输入证书编号']")
    # 16.点击提交按钮
    product_submit_loc = (By.XPATH, "//div[18]/div/button/span['提 交']")
    #17.获取商品名称
    good_manage_loc =(By.XPATH, "//ul/li[2][text() ='商品管理']")
    good_list_loc =(By.XPATH, "//main/div[@class='goodsList']")
    product_list_name_loc =(By.XPATH,"//div[2][text() ='web自动化测试商品']")
    # 页面操作
    def add_product(self, product_name, sub_name, detail_add, sale_price,product_stock, stocks_forewarn, product_code, product_prices, food_licence, product_spec_pic,product_pic):
        #登录
        lp = login_page(self.driver)
        lp.login_nlxshop("zytest123", "zytest123")
        time.sleep(2)
        #创建商品
        self.locator_click(create_product_page.navigation_button_loc)
        time.sleep(2)
        self.locator_click(create_product_page.creat_loc)
        time.sleep(2)
        self.locator_click(create_product_page.select_loc)
        time.sleep(3)
        self.locator_click(create_product_page.select_category_loc)
        time.sleep(2)
        self.locator_value(create_product_page.product_name_loc, product_name)
        time.sleep(2)
        self.locator_value(create_product_page.product_subname_loc, sub_name)
        time.sleep(2)
        self.locator_click(create_product_page.brand_loc)
        time.sleep(2)
        self.locator_click(create_product_page.select_brand_loc)
        time.sleep(2)
        self.locator_click(create_product_page.freight_loc)
        time.sleep(2)
        self.locator_click(create_product_page.select_freight_loc)
        time.sleep(2)
        self.locator_click(create_product_page.province_loc)
        time.sleep(2)
        self.locator_click(create_product_page.select_province_loc)
        time.sleep(2)
        self.locator_click(create_product_page.city_loc)
        time.sleep(2)
        self.locator_click(create_product_page.select_city_loc)
        time.sleep(2)
        self.locator_click(create_product_page.district_loc)
        time.sleep(2)
        self.locator_click(create_product_page.select_district_loc)
        time.sleep(2)
        self.locator_click(create_product_page.street_loc)
        time.sleep(2)
        self.locator_click(create_product_page.select_street_loc)
        time.sleep(2)
        self.locator_value(create_product_page.detail_add_loc, detail_add)
        time.sleep(2)
        self.locator_click(create_product_page.select_product_spec_loc)
        time.sleep(2)
        self.locator_value(create_product_page.sale_price_loc, sale_price)
        time.sleep(2)
        self.locator_value(create_product_page.product_stock_loc, product_stock)
        time.sleep(2)
        self.locator_value(create_product_page.stocks_forewarn_loc, stocks_forewarn)
        time.sleep(2)
        self.locator_value(create_product_page.product_code_loc, product_code)
        time.sleep(2)
        self.locator_value(create_product_page.product_spec_pic_loc, product_spec_pic)
        time.sleep(2)
        self.locator_value(create_product_page.product_prices_loc, product_prices)
        time.sleep(2)
        self.locator_value(create_product_page.product_pic_loc, product_pic)
        time.sleep(3)
        self.locator_click(create_product_page.secend_pic_loc)
        time.sleep(3)
        uplaod_file('2.jpg')
        time.sleep(3)
        self.locator_click(create_product_page.product_tag_loc)
        time.sleep(3)
        uplaod_file('3.jpg')
        time.sleep(3)
        self.locator_click(create_product_page.licence_loc)
        time.sleep(2)
        self.locator_click(create_product_page.select_licence_loc)
        time.sleep(2)
        self.locator_value(create_product_page.food_licence_loc, food_licence)
        time.sleep(3)
        self.locator_click(create_product_page.product_submit_loc)
        time.sleep(2)
    def assert_product(self):
        self.locator_click(create_product_page.good_manage_loc)
        time.sleep(3)
        find_product_list =self.locator_elements(create_product_page.product_list_name_loc)
        print(len(find_product_list))
        print(find_product_list[0].text)
        if len(find_product_list) > 0:
            return find_product_list[0].text
        else:
            print("商品不存在")

