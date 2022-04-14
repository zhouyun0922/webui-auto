#encoding=UTF-8
'''
@auth:zhouyun
@time:2021-12-27
'''
import allure
from base.base_manage_util import base_manage_util
from pageobject.approve_product_page import approve_product_page

class Test_approveproduct(base_manage_util):
    @allure.story("审批商品")  # 模块名称
    @allure.title("审批商品")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_03_approveproduct(self):
        pm =approve_product_page(self.driver)
        pm.approve_product()
        self.assertEqual(pm.assert_approve_product(), "审核通过")

'''
    if __name__ == "__main__":
        unittest.main(['-s', '-v'])  # -s输出打印信息
'''