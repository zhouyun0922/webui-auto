'''
@TIME:2021-12-27
@AUTH:ZHOUYUN
'''
import time,unittest
from selenium.webdriver.common.by import By
from base.base_page import basepage


class login_page(basepage):
    # 页面元素
    # 登录界面元素
    button_loc = (By.CLASS_NAME, "el-button")
    username_loc = (By.XPATH, "//input[@placeholder ='手机号/企业账号']")
    password_loc = (By.XPATH, "//input[@placeholder ='密码']")
    submit_loc = (By.XPATH, "//span[text()='登录']")
    #校验登录元素
    nickname_loc = (By.XPATH, "//span[1][@class ='nickName']")
    assert_loc = (By.XPATH, "//div[2][text() ='退出登录']")

    # 页面操作
    def login_nlxshop(self, username, password):
        self.locator_click(login_page.button_loc)
        time.sleep(2)
        self.locator_value(login_page.username_loc, username)
        time.sleep(2)
        self.locator_value(login_page.password_loc, password)
        time.sleep(2)
        self.locator_click(login_page.submit_loc)
        time.sleep(3)

    def assert_login(self):
        self.locator_click(login_page.nickname_loc)
        return self.get_value(login_page.assert_loc)