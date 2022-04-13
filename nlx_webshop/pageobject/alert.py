#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
def alert():

    # 定义浏览器
    browser = webdriver.Chrome()
    # 打开url
    #browser.get(url)
    # 切换至消息框，适用于alert/confirm/prompt
    alert_box = browser.switch_to.alert
    # 点击消息框的确认按钮，返回值为true。适用于alert/confirm/prompt
    alert_box.accept()
    # 点击消息框的取消按钮，返回值为False。适用于confirm/prompt
    alert_box.dismiss()
    # 向输入框发送内容，适用于prompt
    alert_box.send_keys("msg")
    # 获取输入框内容，适用于prompt
    alert_box.text