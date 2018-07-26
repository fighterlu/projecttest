#coding=utf-8

from appium import webdriver
from time import sleep

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.0.0.0',
                'deviceName': '127.0.0.1:62001',
                'appPackage': 'com.shanjian.originaldesign',
                'appActivity':'.activity.other.Activity_In'
                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(10)

# 多个元素进行定位
buttons = driver.find_elements_by_class_name("android.widget.EditText")
print len(buttons)
# 1.通过 elements + for循环  定位登陆界面
for button in range(len(buttons)):
    data = ['15817252876','123456']
    element = driver.find_elements_by_class_name('android.widget.EditText')[button]
    element.send_keys(data[button])

# 或者 class name定位  但是class name属性值是不唯一的 要考虑
# driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys('12123333')
# driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys('12123333')

# 或者通过 id 定位  用户名文本框和密码文本框
# driver.find_element_by_id('com.shanjian.originaldesign:id/edit_Tel').send_keys('15817252876')
# driver.find_element_by_id('com.shanjian.originaldesign:id/edit_Pwd').send_keys('123456')


# 或者通过 name 定位登陆按钮 （注意：name定位就是定的text对应的属性值）
# driver.find_element_by_name('登录').click()


# 通过 uiautomator 定位 new UiSelector().text("text文本") 登陆功能


# 用于清除历史记录
# ndroid_uiautomator('new UiSelector()定位
# driver.find_element_by_id("com.shanjian.originaldesign:id/edit_Tel").clear()
# driver.find_element_by_android_uiautomator('new UiSelector().text("输入手机号码")').send_keys('15817252876')
# driver.find_element_by_id("com.shanjian.originaldesign:id/edit_Pwd").send_keys("123456")
# driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()


# 使用 xpath 定位登陆功能  注意：标签名就是class的值
# driver.find_element_by_id("com.shanjian.originaldesign:id/edit_Tel").clear()

# xpath层级和属性结合定位
# driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.shanjian.originaldesign:id/edit_Tel']").send_keys('15817252876')
# driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.shanjian.originaldesign:id/edit_Pwd']").send_keys('123456')

# xpath文本定位
# driver.find_element_by_xpath("//android.widget.TextView[@text='登录']").click()












