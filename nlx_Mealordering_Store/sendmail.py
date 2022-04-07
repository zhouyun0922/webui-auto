#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：mail.py
@Author  ：周云
@Date    ：2022/3/4 15:45 
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from email.utils import formataddr

def find_report_name():
    """查找最后生成的报告文件的路径"""
    result_dir = os.path.abspath('..') + "/nlx_Mealordering_Store/report/AllureReport/Allure"
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "/" + fn))
    file_name = os.path.join(result_dir, 'index.html')
    print(file_name)
    return file_name


def mail(find_report_name):
    my_sender = '835341066@qq.com'  # 发件人邮箱账号
    my_pass = 'ipfqldpsdhkybcfd'  # 发件人邮箱密码
    my_user = 'zhoubiao0922@126.com'  # 收件人邮箱账号，我这边发送给自己
    ret = True
    try:
        # 读取测试报告文件
        mail_body = open(find_report_name(), "r", encoding="utf-8").read()
        msg = MIMEMultipart()
        body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        # 定义邮件内容
        #msg = MIMEText('点餐系统商家端web自动化测试报告，具体见附件.', 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "周云web自动化测试报告"  # 邮件的主题，也可以说是标题
        msg.attach(body)
        # 定义附件内容
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "index.html"'
        msg.attach(att)
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as ex:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(ex)
        ret = False
    return ret

ret = mail(find_report_name)
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")

'''
if __name__ == "__main__":
    pytest.main(['-s', '-v',test_find_report_name()])  # -s输出打印信息
'''