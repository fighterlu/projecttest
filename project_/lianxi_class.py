#coding=utf-8

from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from common.lianxi import *

class Itest_Appium(unittest.TestCase):

    def setUp(self):
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.4.2',
            'deviceName': '127.0.0.1:62001',
            'appPackage': 'iflytek.testTech.propertytool',
            'appActivity': '.activity.BootActivity',
            # 'appWaitActivity':'.activity.HomeActivity',
            'unicodeKeyboard': "True",  #使用 Unicode 输入法
            'resetKeyboard': "True"}    #重置输入法到原有状态'udid':''

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.driver.wait_activity('.activity.HomeActivity',20)  # 等待app首页出现


    def tearDown(self):
        pass

    def test_addapp_jiankong(self):
        driver = self.driver
        delapp(driver)
        addapp(driver,'Appium','io.appium.android.ime','io.appium.settings')
        jiankong(driver,'电量',True)
        jiankong(driver,'CPU',True)
        closeapp(driver)

if __name__ == '__main__':
    unittest.main(verbosity=2)
