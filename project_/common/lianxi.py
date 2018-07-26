#coding:utf-8


#coding=utf-8

from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# iflytek.testTech.propertytool/.activity.HomeActivity

# desired_caps = {
#                 'platformName': 'Android',
#                 'platformVersion': '4.4.2',
#                 'deviceName': 'http://127.0.0.1:4723/wd/hub',
#                 'appPackage': 'iflytek.testTech.propertytool',
#                 'appActivity': '.activity.BootActivity',
#                 'unicodeKeyboard': "True",
#                 'resetKeyboard': "True"
#                 }
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.wait_activity('.activity.HomeActivity', 20)  # 等待app首页出现


def delapp(driver):
    #删除以添加的监控应用
    eles = driver.find_elements_by_id('iflytek.testTech.propertytool:id/app_icon')
    #如果应用大于2 就点击编辑删除
    if len(eles) >2:
        #点击编辑按钮
        driver.find_element_by_id('iflytek.testTech.propertytool:id/monitor_del_icon').click()
        #等待红点出现
        time.sleep(3)
        # 获取红点个数
        elements = driver.find_elements_by_id('iflytek.testTech.propertytool:id/app_del')
        for ele in elements:
            driver.find_element_by_id('iflytek.testTech.propertytool:id/app_del').click() #循环删除
        driver.find_element_by_id('iflytek.testTech.propertytool:id/monitor_del_icon').click() #确认删除



def addapp(driver,appname,name1,name2):
    #添加应用
    driver.find_element_by_id('iflytek.testTech.propertytool:id/app_icon').click()
    time.sleep(5)
    #输入Appium
    driver.find_element_by_name('请输入需要监控的APP名称').send_keys(appname)
    #点击选择appium
    driver.find_element_by_name(name1).click()   #'io.appium.android.ime'
    time.sleep(5)
    #点击选择
    driver.find_element_by_name(name2).click()  #'io.appium.settings'
    time.sleep(6)
    #点击确认
    driver.find_element_by_id('iflytek.testTech.propertytool:id/app_confirm').click()



def jiankong(driver,name,bool):
    #等待电量页面出现
    WebDriverWait(driver,50).until(EC.visibility_of_element_located((By.NAME,'电量')))   #等待页面出现
    #添加监控
    checked = driver.find_element_by_name(name).get_attribute('checked')
    if bool:
        if checked == 'false':
            driver.find_element_by_name(name).click()
    else:
        if checked == 'false':
            driver.find_element_by_name(name).click()
    time.sleep(3)
    driver.find_element_by_name('启动监控').click()
    time.sleep(3)
    driver.find_element_by_name('停止监控').click()
    time.sleep(3)



def closeapp(driver):
    #关闭app
    driver.close_app()



def down_up(driver):
    '''封装向上滑动方法'''
    size = driver.get_window_size()    # 获取页面分辨率
    x1 = size['width']  * 0.5
    y1 = size['height'] * 0.75
    y2 = size['height'] * 0.25
    driver.swipe(x1,y1,x1,y2)    #向上滑动


def down_down(driver):
    '''封装向下滑动方法'''
    size = driver.get_window_size()    # 获取页面分辨率
    x1 = size['width']  * 0.5
    y1 = size['height'] * 0.25
    y2 = size['height'] * 0.75
    driver.swipe(x1,y1,x1,y2)    #向上滑动




























