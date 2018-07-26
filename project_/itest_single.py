#coding=utf-8

from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# iflytek.testTech.propertytool/.activity.HomeActivity

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '4.4.2',
                'deviceName': 'http://127.0.0.1:4723/wd/hub',
                'appPackage': 'iflytek.testTech.propertytool',
                'appActivity': '.activity.BootActivity',
                'unicodeKeyboard': "True",
                'resetKeyboard': "True"
                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.wait_activity('.activity.HomeActivity', 20)  # 等待app首页出现


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


#添加应用
driver.find_element_by_id('iflytek.testTech.propertytool:id/app_icon').click()
time.sleep(2)
#输入Appium
driver.find_element_by_name('请输入需要监控的APP名称').send_keys('Appium')
#点击选择appium
driver.find_element_by_name('io.appium.android.ime').click()
time.sleep(3)
#点击选择
driver.find_element_by_name('io.appium.settings').click()
time.sleep(6)

#点击确认
driver.find_element_by_id('iflytek.testTech.propertytool:id/app_confirm').click()
#等待电量页面出现
WebDriverWait(driver,50).until(EC.visibility_of_element_located((By.NAME,'电量')))   #等待页面出现


#添加监控
checked = driver.find_element_by_name('电量').get_attribute('checked')
if checked == 'false':
    driver.find_element_by_name('电量').click()
if driver.find_element_by_name('CPU').get_attribute('checked') == 'false':
    driver.find_element_by_name('CPU').click()
time.sleep(3)
driver.find_element_by_name('启动监控').click()
time.sleep(3)
driver.find_element_by_name('停止监控').click()
time.sleep(3)


#关闭app
driver.close_app()







































