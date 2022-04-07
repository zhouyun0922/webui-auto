#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：nlx_Mealordering_Store 
@File    ：seat_manage.py
@Author  ：周云
@Date    ：2022/2/21 10:31 
'''
import time
import pytest
from base.base_page import basepage
from selenium.webdriver.common.by import By
import re
import datetime
from pathlib import Path
import os
import os.path

class Seat_manage(basepage):
    # 页面元素
    # 创建区域、座位
    seat_loc = (By.XPATH, "//span[2][text()='座位']")
    seat_manage_loc = (By.XPATH, "//span[2][text()='座位管理']")
    create_seat_button_loc =(By.XPATH,"//span[text()='新建座位']")
    area_name_loc =(By.ID,"basic_areaId")
    area_nmae_select_loc =(By.XPATH,"//div[1]/div[text()='区域测试']")
    seat_num_loc = (By.ID,"basic_seatNo")
    seat_persons_loc = (By.ID,"basic_contain")
    save_loc = (By.XPATH,"//span[text()='保 存']")
    # 校验创建座位成功元素
    assert_create_seat_loc = (By.XPATH, "//*[text()='已保存']")
    assert_seat_loc = (By.XPATH,"//div[2][text() ='test01']")
    # 删除座位
    name_seat_loc =(By.XPATH, "//div[2][text() ='test01']")
    delete_seat_loc =(By.XPATH,"//div/div/div[1]/div/span[2][@class='anticon icon___OTcLH']")
    confirm_seat_loc =(By.XPATH,"//span[text() ='确 认']")
    #校验删除结果
    assert_delete_seat_loc =(By.XPATH,"//span[2][text() = '已删除']")
    #下载单个座位二维码
    download_seat_loc =(By.XPATH,"//div/div/div[1]/div/span[1][@class='anticon icon___OTcLH']")
    #批量下载座位二维码
    download_seats_loc =(By.XPATH,"//span[text()='批量导出二维码']")
    #批量下载座位二维码编码
    download_seatcodes_loc =(By.XPATH,"//span[text()='Excel导出二维码编号']")
    # 页面操作
    # 新建座位
    def create_seat(self,seat_num,seat_persons):
        #self.locator_click(Seat_manage.seat_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.seat_manage_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.create_seat_button_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.area_name_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.area_nmae_select_loc)
        time.sleep(2)
        self.locator_value(Seat_manage.seat_num_loc,seat_num)
        time.sleep(2)
        self.locator_value(Seat_manage.seat_persons_loc,seat_persons)
        time.sleep(2)
        self.locator_click(Seat_manage.save_loc)
        time.sleep(2)
    # 校验新建座位
    def assert_create_seat(self):
        messg =[self.get_value(Seat_manage.assert_create_seat_loc),self.get_value(Seat_manage.assert_seat_loc)]
        return messg

    # 删除座位
    def delete_seat(self):
        time.sleep(2)
        self.locator_click(Seat_manage.seat_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.seat_manage_loc)
        time.sleep(2)
        seat_name_list = self.locator_elements(Seat_manage.name_seat_loc)
        if len(seat_name_list)>0:
            delete_seat_list = self.locator_elements(Seat_manage.delete_seat_loc)
            delete_seat_list[0].click()
        else:
            print("座位不存在")
        time.sleep(2)
        self.locator_click(Seat_manage.confirm_seat_loc)

    # 校验删除座位
    def assert_delete_seat(self):
        return self.get_value(Seat_manage.assert_delete_seat_loc)

    # 下载单个座位二维码
    def download_seat(self):
        time.sleep(2)
        self.locator_click(Seat_manage.seat_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.seat_manage_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.download_seat_loc)

    # 校验下载单个座位二维码
    def assert_download_seat(self):
        time.sleep(2)
        # 谷歌的默认的下载地址
        result_dir = "C:\\Users\\周云\\Downloads"
        list = os.listdir(result_dir)
        # 重新按时间对目录下的文件进行排序 获取最新下载文件的名字
        list.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
        # list[-1]的这个地方需要拿的是最后一个文件，也就是时间最新的文件
        file = os.path.join(result_dir, list[-1])
        # 这个是获取下载文件的名字，下载时候如果有相同文件 就会带上（1.2....)情况，因此用正则表达式进行去掉括号以及括号的内容
        name = re.sub('\\(.*?\\)', "", list[-1]).strip()
        result_name = re.sub('\\s+', '', name).strip()
        # 此处是对于名字的一个判断
        try:
            assert os.path.splitext(result_name)[1] == u".png"
            print("test pass.")
        except Exception as e:
            print("test fail:文字名称不正确,当前没有下载成功", format(e))
        # 获取文件的时间：年月日，与当前的年月日进行比较判断是不是已经下载了
        time1 = datetime.date.fromtimestamp(os.path.getmtime(result_dir + "\\" + list[-1]))
        time2 = time1.strftime('%Y%m%d')
        timestr1 = time.strftime('%Y%m%d', time.localtime(time.time()))
        try:
            assert time2 == timestr1
            print("test pass.")
        except Exception as e:
            print("test fail:时间对比不正确，可能就没有下载成功噢", format(e))
        # print(type(list[-1]))
        try:
            # 删除文件
            os.remove(Path(file))
        except:
            print("没有出现文件")

    #批量下载座位二维码
    def download_seats(self):
        time.sleep(2)
        self.locator_click(Seat_manage.seat_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.seat_manage_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.download_seats_loc)

    # 校验批量下载座位二维码
    def assert_download_seats(self):
        time.sleep(2)
        # 谷歌的默认的下载地址
        result_dir = "C:\\Users\\周云\\Downloads"
        list = os.listdir(result_dir)
        # 重新按时间对目录下的文件进行排序 获取最新下载文件的名字
        list.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
        # list[-1]的这个地方需要拿的是最后一个文件，也就是时间最新的文件
        file = os.path.join(result_dir, list[-1])
        # 这个是获取下载文件的名字，下载时候如果有相同文件 就会带上（1.2....)情况，因此用正则表达式进行去掉括号已经括号的内容
        name = re.sub('\\(.*?\\)', "", list[-1]).strip()
        result_name = re.sub('\\s+', '', name).strip()
        # 此处是对于名字的一个判断
        try:
            assert os.path.splitext(result_name)[1] == u".pdf"
            print("test pass.")
        except Exception as e:
            print("test fail:文字名称不正确,当前没有下载成功", format(e))
        # 获取文件的时间：年月日，与当前的年月日进行比较判断是不是已经下载了
        time1 = datetime.date.fromtimestamp(os.path.getmtime(result_dir + "\\" + list[-1]))
        time2 = time1.strftime('%Y%m%d')
        timestr1 = time.strftime('%Y%m%d', time.localtime(time.time()))
        try:
            assert time2 == timestr1
            print("test pass.")
        except Exception as e:
            print("test fail:时间对比不正确，可能就没有下载成功噢", format(e))
        # print(type(list[-1]))
        try:
            # 删除文件
            os.remove(Path(file))
        except:
            print("没有出现文件")

    #批量下载座位二维码编码
    def download_seatcodes(self):
        time.sleep(2)
        self.locator_click(Seat_manage.seat_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.seat_manage_loc)
        time.sleep(2)
        self.locator_click(Seat_manage.download_seatcodes_loc)

    # 校验批量下载座位二维码
    def assert_download_seatcodes(self):
        time.sleep(2)
        # 谷歌的默认的下载地址
        result_dir = "C:\\Users\\周云\\Downloads"
        list = os.listdir(result_dir)
        # 重新按时间对目录下的文件进行排序 获取最新下载文件的名字
        list.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
        # list[-1]的这个地方需要拿的是最后一个文件，也就是时间最新的文件
        file = os.path.join(result_dir, list[-1])
        # 这个是获取下载文件的名字，下载时候如果有相同文件 就会带上（1.2....)情况，因此用正则表达式进行去掉括号已经括号的内容
        name = re.sub('\\(.*?\\)', "", list[-1]).strip()
        result_name = re.sub('\\s+', '', name).strip()
        # 此处是对于名字的一个判断
        try:
            assert os.path.splitext(result_name)[1] == u".xls"
            print("test pass：文件下载成功")
        except Exception as e:
            print("test fail:文字名称不正确,当前没有下载成功", format(e))
        # 获取文件的时间：年月日，与当前的年月日进行比较判断是不是已经下载了
        time1 = datetime.date.fromtimestamp(os.path.getmtime(result_dir + "\\" + list[-1]))
        time2 = time1.strftime('%Y%m%d')
        timestr1 = time.strftime('%Y%m%d', time.localtime(time.time()))
        try:
            assert time2 == timestr1
            print("test pass.")
        except Exception as e:
            print("test fail:时间对比不正确，可能就没有下载成功噢", format(e))
        # print(type(list[-1]))
        try:
            # 删除文件
            os.remove(Path(file))
        except:
            print("没有出现文件")
