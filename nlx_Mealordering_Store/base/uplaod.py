#encoding=UTF-8
import pywinauto
import pyautogui
import time
from pywinauto.keyboard import send_keys
def uplaod_file(filename):
    # 使用pywinauto来选择文件
    app = pywinauto.Desktop()
    # 选择文件上传的窗口
    dlg = app["打开"]
    # 选择文件地址输入框，点击**
    dlg["Toolbar3"].click()
    # 键盘输入上传文件的路径
    send_keys(r"/home/zhouyun/")
    # 键盘输入回车，打开该路径
    send_keys("{VK_RETURN}")
    time.sleep(1)
    # 选中文件名输入框，输入文件名
    dlg["文件名(&N):Edit"].type_keys(filename)
    time.sleep(2)
    # 点击打开
    dlg["打开(&O)"].click()
    '''
    # 输入文件名
    pyautogui.write(r"/home/zhouyun/" + filename)
    # 输入回车键，注意要按2次
    pyautogui.press('enter', presses=2)
    '''
'''
if __name__ == "__main__":
    filename = "1.jpg"
    unittest.main(['-s', '-v',uplaod_file])  # -s输出打印信息
'''
