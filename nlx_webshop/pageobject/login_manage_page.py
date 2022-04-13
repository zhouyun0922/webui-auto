'''
@TIME:2021-12-28
@AUTH:ZHOUYUN
'''
import time

from selenium.webdriver.common.by import By
from base.base_page import basepage


class login_manage_page(basepage):
    # 页面元素
    # 登录界面元素
    username_loc = (By.XPATH, "//input[@placeholder='请输入用户名']")
    password_loc = (By.XPATH, "//input[@placeholder='请输入密码']")
    submit_loc = (By.XPATH, "//span[contains(text(),'登录')]")
    #校验登录元素
    nickname_loc = (By.XPATH, "//span[@class ='user-name']")
    assert_loc = (By.XPATH, "//span[contains(text(), '退出')]")
    # 页面操作
    def login_manage(self, username, password):
        self.locator_value(login_manage_page.username_loc, username)
        self.locator_value(login_manage_page.password_loc, password)
        self.locator_click(login_manage_page.submit_loc)
        time.sleep(3)

    def assert_login(self):
        self.locator_click(login_manage_page.nickname_loc)
        return self.get_value(login_manage_page.assert_loc)

