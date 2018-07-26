#coding:utf-8

'''
:Args:
- start_x - 开始滑动的 x 坐标
- start_y - 开始滑动的 y 坐标
- end_x  - 结束点 x 坐标
- end_y - 结束点 y 坐标
- duration - 持续时间，单位毫秒

:Usage:
driver.swipe(100, 100, 100, 400)

'''

from appium import webdriver
from time import sleep

desired_caps = {
                'platformName': 'Android',
                'deviceName': '30d4e606',
                'platformVersion': '4.4.2',
                'appPackage': 'com.taobao.taobao',
                'appActivity': 'com.taobao.tao.welcome.Welcome'
                }
'''
参数 1：driver
参数 2：t 是持续时间
参数 3：滑动次数
'''

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
sleep(8)

def swipeUp(driver, t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] *  0.5  # x 坐标
    y1 = l['height'] * 0.75 # 起始 y 坐标
    y2 = l['height'] * 0.25 # 终点 y 坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width']  * 0.5 # x 坐标
    y1 = l['height'] * 0.25 # 起始 y 坐标
    y2 = l['height'] * 0.75 # 终点 y 坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, 1)


def swipLeft(driver, t=500, n=1):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width']  * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width']  * 0.05
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


def swipRight(driver, t=500, n=1):
    '''向右滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width']  * 0.05
    y1 = l['height'] * 0.5
    x2 = l['width']  * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

if __name__ == "__main__":
    print(driver.get_window_size())
    sleep(8)
    swipeUp(driver,n=1)
    sleep(8)
    swipeDown(driver,n=1)