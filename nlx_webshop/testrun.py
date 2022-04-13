'''
@auth:zhouyun
@time:2021-12-27
'''
# coding=utf-8

import os
import pytest
import time
#简易allure执行脚本
#完善后的allure执行脚本
class testrun():

    test_path = "./test_case/test_01_login.py"
    report_path = "./report/AllureReport"
    now = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    htmlreport = 'nlx_webshop' + now + '_result.html' 
    try:
        print("开始执行脚本")
        #运行 cases下所有测试用例
        args = ['-s', '-v', "--alluredir={}".format(report_path), test_path]
        pytest.main(args)
        #pytest.main(["-s","--html=report/" + htmlreport, "--alluredir={}".format(report_path), test_path])
        result = os.system("allure generate report\AllureReport -o report\AllureReport\Allure --clean")
        open = os.system("allure open -h 192.168.14.117 -p 8883 ./report/AllureReport/Allure")
        print("脚本执行完成")
    except Exception as e:
        print("脚本批量执行失败！", e)
'''
#第一步：
pytest -s ./test_case/test_01_login.py --alluredir ./report/AllureReport

#第二步：
allure generate report\AllureReport -o report\AllureReport\Allure --clean

#第三步：
allure open -h 192.168.14.117 -p 8883 ./report/AllureReport/Allure
'''