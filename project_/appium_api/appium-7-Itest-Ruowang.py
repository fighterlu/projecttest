# coding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# appPackage：iflytek.testTech.propertytool      app首页： .activity.HomeActivity
desired_caps = {
		'platformName': 'Android',
		'platformVersion': '4.4.2',
		'deviceName': 'Android Emulator',
		'appPackage': 'iflytek.testTech.propertytool',
		'appActivity': '.activity.BootActivity',
		'unicodeKeyboard': "True",
		'resetKeyboard': "True"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.wait_activity('.activity.HomeActivity', 20)  # 等待app首页出现
# WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name('电量')) # 等待页面出现
locator = (By.NAME, u'电量')
WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locator))
driver.find_element_by_name('工具箱').click()
time.sleep(3)
driver.find_element_by_name("弱网工具(需要root)").click()
time.sleep(5)
driver.find_element_by_id('iflytek.testTech.propertytool:id/imageView_download').click()  #点击限制下载速度为0kB/s
s=driver.page_source
print(s)
driver.quit()