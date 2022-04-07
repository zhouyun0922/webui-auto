#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：run.py
@Author  ：周云
@Date    ：2022/2/17 16:27 
'''
import os
import pytest
import time
#完善后的allure执行脚本
class allurerun():
    test_path = "test_case/test_*.py"
    report_path = "./report/AllureReport"
    now = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    htmlreport = 'nlx_webshop' + now + '_result.html'
    try:
        print("开始执行脚本")
        #运行 cases下所有测试用例
        args = ['-s', '-v', "--alluredir={}".format(report_path), test_path,"--clean-alluredir"]
        pytest.main(args)
        result = os.system("allure generate report\AllureReport -o report\AllureReport\Allure --clean")
        open = os.system("allure open -h 192.168.14.161 -p 8883 ./report/AllureReport/Allure")
        print("脚本执行完成")
    except Exception as e:
        print("脚本批量执行失败！", e)
