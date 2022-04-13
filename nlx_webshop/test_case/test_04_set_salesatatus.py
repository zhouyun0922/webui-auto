#encoding=UTF-8
'''
@auth:zhouyun
@time:2021-12-27
'''

import time
import testrun
from base.base_manage_util import base_manage_util
from pageobject.set_sale_page import set_sale_page
from pageobject.login_manage_page import login_manage_page


class Test_set_sale_status(base_manage_util):
    @testrun.story("上架商品")  # 模块名称
    @testrun.title("上架商品")  # 用例名称
    @testrun.severity("normal")  # 用例等级
    #商品上架
    def test_03_set_onsale(self):
        pm =set_sale_page(self.driver)
        pm.set_sale_status()
        time.sleep(0.5)
        self.assertEqual(pm.assert_sale_status(), "修改成功")
    #商品强制下架
    @testrun.story("强制下架商品")  # 模块名称
    @testrun.title("强制下架商品")  # 用例名称
    @testrun.severity("normal")  # 用例等级
    def test_04_confirm_set_offsale(self):
        lp=login_manage_page(self.driver)
        lp.login_manage("zytest", "zytest123")
        time.sleep(2)
        pm =set_sale_page(self.driver)
        pm.confirm_sale_out("商品信息错误，需强制下架！")
        time.sleep(2)
        self.assertEqual(pm.assert_confirm_sale_out(), "解除强制下架")
    #商品强制上架
    @testrun.story("强制上架商品")  # 模块名称
    @testrun.title("强制上架商品")  # 用例名称
    @testrun.severity("normal")  # 用例等级
    def test_05_confirm_set_onsale(self):
        lp=login_manage_page(self.driver)
        lp.login_manage("zytest", "zytest123")
        time.sleep(2)
        pm = set_sale_page(self.driver)
        pm.confirm_sale_on()
        time.sleep(2)
        self.assertEqual(pm.assert_confirm_sale_on(), "强制下架")
'''
    if __name__ == "__main__":
        unittest.main(['-s', '-v'])  # -s输出打印信息
'''