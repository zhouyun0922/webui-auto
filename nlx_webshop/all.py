'''
@auth:zhouyun
@time:2021-12-27
'''
#coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":
    #执行需要的用例，并且生成html格式的自动化的测试报告
    #使用unittest默认的测试用例的加载器去发现testcase目录下以py结尾的所有测试用例
    suite = unittest.defaultTestLoader.discover("test_case", "test_01_login.py")
    #生成html报告文件
    report_file = open("./report/reports.html","wb")
    #生成一个htmltestrunner运行器对象（必须下载一个文件HTMLTestRunner.py,放到python的lib目录下）
    runner = HTMLTestRunner(stream=report_file,title="nlx_webshop自动化测试报告",description ="具体见生成的测试报告")
    #通过运行器运行测试用例
    runner.run(suite)
    report_file.close()  # 写完后关闭HTML报告




