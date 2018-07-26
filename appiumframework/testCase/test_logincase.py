#coding=utf-8

from appiumframework.pages.loginpage import Airen_Login_Page
from appiumframework.PO.base_page import Action
import unittest
import time
from appium import webdriver

class TestAirenLogin(unittest.TestCase):

    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        'deviceName': '127.0.0.1:62001',
                        'platformVersion': '3.8.3.1',
                        'appPackage': 'com.juyang.mall',
                        'appActivity': 'com.shanjian.juyang.activity.home.Activity_Home'
                        }
        desired_caps["unicodeKeyboard"] = "True"  #使用unicode编码方式发送字符串
        desired_caps["resetKeyboard"] = "True"   #将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.wait_activity('.activity.other.Activity_In', 10)  # 等待app首页出现
        self.verificationErrors = u'商城'

    def tearDown(self):
        time.sleep(4)
        self.driver.close_app()

    def test_aiRenLogin(self):
        '''PO设计登陆功能实战'''
        aiRen = Airen_Login_Page(self.driver)
        aiRen.login_airen_appproject('18665100958','123456')
        #断言：实际结果  预期结果  错误信息
        self.assertEqual(self.verificationErrors,aiRen.get_finish_button_text(),msg=u'验证失败！')


