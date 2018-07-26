#coding=utf-8

'''
所有用到的页面都定义成一个类，继承自基础的Page类
把页面中用到的元素定义成方法
把页面上一些操作定义成方法
'''

# 基础类 用于所有页面的继承
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Action(object):

    #初始化
    def __init__(self,driver):
        self.driver = driver
    #重新
    def by_id(self,loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print('未找到 {0}'.format(e))

    def by_name(self, loc):
        try:
            return self.driver.find_element_by_name(loc)
        except Exception as e:
            print('未找到 {0}'.format(e))

    def by_xpath(self, loc):
        try:
            return self.driver.find_element_by_xpath(loc)
        except Exception as e:
            print('未找到 {0}'.format(e))