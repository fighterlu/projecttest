#coding=utf-8


from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.0.0.0',
    'deviceName': '127.0.0.1:62001',
    'appPackage': 'com.baidu.yuedu',
    'appActivity':'.splash.SplashActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
sleep(10)
driver.find_element_by_id("com.baidu.yuedu:id/negativeUpgrade").click()
sleep(10)
driver.find_element_by_id("com.baidu.yuedu:id/btn_cancel").click()
sleep(10)
driver.find_element_by_id("com.baidu.yuedu:id/righttitle").click()
sleep(10)

#获取所有的上下文
views = driver.contexts
print (views)
#获取当前上下文
curview = driver.context
#切换到webview
driver.switch_to.context(views[2])
print (driver.context)


'''
2.切换上下文操作；
.switch_to.contexts          **获取所有上下文**
.switch_to.context(指定环境)   **切换到指定环境**
.switch_to.current_context    **获取当前环境信息**
'''


