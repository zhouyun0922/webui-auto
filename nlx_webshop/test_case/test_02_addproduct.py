#encoding=UTF-8
'''
@auth:zhouyun
@time:2021-12-27
'''
import time
import allure
from base.base_util import base_util
from pageobject.create_product_page import create_product_page
import testrun

class Testcase_product_add(base_util):
    @allure.story("添加商品")  # 模块名称
    @allure.title("添加商品")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_01_addproduct(self):
        ''' 商品创建 '''
        #商品创建
        product_name ="web自动化测试商品"
        sub_name ="web自动化测试商品"
        detail_add ="测试地址"
        sale_price ='0.01'
        product_stock ='1000'
        stocks_forewarn ='100'
        product_code ='1202633'
        product_prices =''
        food_licence ='sc101010101'
        product_spec_pic =r"C:\Users\周云\Desktop\测试图片\1.jpg"
        product_pic =r"C:\Users\周云\Desktop\测试图片\1.jpg"

        #点击导航栏商品按钮

        pm = create_product_page(self.driver)
        pm.add_product(product_name,sub_name,detail_add,sale_price,product_stock,
                       stocks_forewarn,product_code,product_prices,food_licence,product_spec_pic,product_pic)
        '''
        lp = login_page(self.driver)
        lp.login_nlxshop("zytest123", "zytest123")
        '''
        time.sleep(3)
        self.assertEqual(pm.assert_product(),"web自动化测试商品")



'''
    if __name__ == "__main__":
        unittest.main(['-s', '-v',test_addproduct_01()])  # -s输出打印信息
'''