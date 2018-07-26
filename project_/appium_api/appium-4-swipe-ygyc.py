#coding=utf-8

from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.0.0.0',
    'deviceName': '127.0.0.1:62001',
    'appPackage': 'com.shanjian.originaldesign',
    'appActivity':'.activity.other.Activity_In'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#登录
sleep(5)
driver.find_element(By.ID,"com.shanjian.originaldesign:id/edit_Tel").clear()
driver.find_element_by_android_uiautomator('new UiSelector().text("输入手机号码")').send_keys("15817252876")
driver.find_element_by_id("com.shanjian.originaldesign:id/edit_Pwd").send_keys("123456")
driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
sleep(5)

#点击不参加
# driver.find_element_by_name("不参加").click()
#点击我的

driver.find_element_by_name("我的").click()
sleep(5)
#获得手机屏幕大小x，y
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']

#屏幕向上滑动

# x1 = int(x * 0.5)    #x坐标
# y1 = int(y * 0.75)   #起始y坐标
# y2 = int(y * 0.25)   #终点y坐标
# driver.swipe(x1, y1, x1, y2,t=3000)

def swipeUp(t=None,n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] *  0.5  # x 坐标
    y1 = l['height'] * 0.75 # 起始 y 坐标
    y2 = l['height'] * 0.25 # 终点 y 坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

#执行向上滑动屏幕的方法
swipeUp(1000)
sleep(5)
#点击退出登录系统
driver.find_element_by_name("退出登录").click()
driver.find_element_by_id("com.shanjian.originaldesign:id/confirm").click()

# def swipeup(t=None,n=1):
#      '''向上滑动'''
#     l  = driver.get_window_size()
#     x1 = l['weight'] * 0.5
#     y1 = l['height'] * 0.75
#     y2 = l['height'] * 0.25
#     for i in range(n):
#         driver.swipe(x1,y1,x1,y2,t)
#
# def swipeidown(t=1000,n=1):
#     '''向下滑动'''
#     l  = driver.get_window_size()
#     x1 = l['weight'] * 0.5
#     y1 = l['height'] * 0.25
#     y2 = l['height'] * 0.75
#     for i in range(n):
#         driver.swipe(x1,y1,x1,y2,t)
#
