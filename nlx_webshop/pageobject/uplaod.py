#encoding=UTF-8
#import pywinauto
#import unittest
import time
from pywinauto.keyboard import send_keys
def uplaod_file(filename):
    # 选择文件
    send_keys(r"/home/zhouyun")
    time.sleep(2)
    # 确定
    send_keys('{ENTER}')
    #上传文件
    send_keys(filename)
    # 确定
    send_keys('{ENTER}')
    '''
    # 使用pywinauto来选择文件
    app = pywinauto.Desktop()
    # 选择文件上传的窗口
    dlg = app["打开"]

    # 选择文件地址输入框，点击**
    dlg["Toolbar3"].click()
    # 键盘输入上传文件的路径
    send_keys(r'C:/Users/周云/Desktop/测试图片')
    # 键盘输入回车，打开该路径
    send_keys("{VK_RETURN}")

    # 选中文件名输入框，输入文件名
    dlg["文件名(&N):Edit"].type_keys(filename)

    # 点击打开
    dlg["打开(&O)"].click()
    '''
'''
if __name__ == "__main__":
    filename = "1.jpg"
    unittest.main(['-s', '-v',uplaod_file])  # -s输出打印信息
'''
