#coding=utf-8

from appium import webdriver
from time import sleep
import unittest

class Login(unittest.TestCase):

    def setUp(self):
        sleep(30)
        desired_caps = {
                        'platformName': 'Android',
                        'platformVersion': '5.0.0.0',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.shanjian.originaldesign',
                        'appActivity':'.activity.other.Activity_In',
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.wait_activity('.activity.other.Activity_In', 30)  # 等待app首页出现

    def test_login(self):
        driver = self.driver
        sleep(5)
        driver.find_element_by_id('com.shanjian.originaldesign:id/edit_Tel').clear()
        driver.find_element_by_id('com.shanjian.originaldesign:id/edit_Tel').send_keys("15817252876")
        driver.find_element_by_id("com.shanjian.originaldesign:id/edit_Pwd").send_keys('123456')
        driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
        sleep(5)
        try:
            if driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').is_displayed():
                print ('Fail')
        except Exception as e:
            print (e)
            print ('pass')

    def tearDown(self):
        driver = self.driver
        driver.close_app()

if __name__ == '__main__':
    unittest.main(verbosity=2)
