#encoding=UTF-8
'''
@auth:zhouyun
@time:2021-12-27
'''
import time,allure
from base.base_util import base_util
from pageobject.login_page import login_page


class Test_login_case(base_util):
    @allure.story("登录")  # 模块名称
    @allure.title("登录成功")  # 用例名称
    @allure.severity("normal")  # 用例等级
    def test_01_login(self):
        ''' 登录 '''
        lp = login_page(self.driver)
        lp.login_nlxshop("zytest123", "zytest123")
        time.sleep(3)
        assert_messg =lp.assert_login()
        print(assert_messg)
        self.assertEqual("退出登录",assert_messg)
'''
if __name__ == "__main__":
        unittest.main(['-s', '-v'])  # -s输出打印信息
'''
