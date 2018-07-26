#coding=utf-8

from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait


class Airen_Login(unittest.TestCase):

    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        'deviceName': '127.0.0.1:62001',
                        'platformVersion': '3.8.3.1',
                        'appPackage': 'com.juyang.mall',
                        'appActivity': 'com.shanjian.juyang.activity.home.Activity_Home'
                        }
        desired_caps["unicodeKeyboard"] = "True"  # 使用unicode编码方式发送字符串
        desired_caps["resetKeyboard"] = "True"  # 将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.wait_activity('.activity.other.Activity_In',10)  # 等待app首页出现

    def login(self,username,passoword):
        '''封装登录'''
        self.driver.find_element(By.ID,'com.juyang.mall:id/edit_Tel').clear()
        self.driver.find_element(By.ID,'com.juyang.mall:id/edit_Tel').send_keys(username)
        self.driver.find_element(By.ID,'com.juyang.mall:id/edit_Pwd').send_keys(passoword)
        self.driver.find_element(By.ID,"com.juyang.mall:id/tv_Login").click()
        sleep(5)

    def test_login_out(self):
        driver = self.driver
        WebDriverWait(driver,50).until(lambda dr: dr.find_element_by_id('com.juyang.mall:id/rb_Mine')) #等待元素加载稳定
        driver.find_element(By.ID, 'com.juyang.mall:id/rb_Mine').click()  # 点击我的
        self.login('18665100958', '123456')
        WebDriverWait(driver,50).until(lambda dr: dr.find_element_by_name('退出登录')) #等待元素加载稳定
        driver.find_element_by_name('退出登录').click()
        WebDriverWait(driver,50).until(lambda dr: dr.find_element_by_id('com.juyang.mall:id/dialog_base_btn_confirm')) #等待元素加载稳定
        driver.find_element_by_id('com.juyang.mall:id/dialog_base_btn_confirm').click()
        sleep(3)
        self.assert_result()

    def assert_result(self):
        '''验证购买成功'''
        contain = self.driver.find_element(By.NAME,u"商城").text        #确认支付断言
        try:
            if u'商' in contain:
                print ("testcase is pass!")
        except Exception as msg:
            print (msg)

    def tearDown(self):
        driver = self.driver
        driver.close_app()

if __name__ == '__main__':
    unittest.main(verbosity=2)
