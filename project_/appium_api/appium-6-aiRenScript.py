#coding=utf-8

from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {'platformName':'Android',
                'deviceName':'127.0.0.1:21503',
                'platformVersion':'3.8.3.1',
                'appPackage':'com.juyang.mall',
                'appActivity':'com.shanjian.juyang.activity.home.Activity_Home'
                }

desired_caps["unicodeKeyboard"] = "True"  #使用unicode编码方式发送字符串
desired_caps["resetKeyboard"] = "True"    #将键盘隐藏起来

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps) #链接app
sleep(4)
driver.find_element(By.ID,'com.juyang.mall:id/rb_Mine').click()  #点击我的
sleep(4)
driver.find_element(By.ID,'com.juyang.mall:id/edit_Tel').clear()
driver.find_element(By.ID,'com.juyang.mall:id/edit_Tel').send_keys("18665100958")
driver.find_element(By.ID,'com.juyang.mall:id/edit_Pwd').send_keys("123456")
driver.find_element(By.ID,"com.juyang.mall:id/tv_Login").click()
sleep(8)
sum = 0
search = ['艾灸按摩椅','十年艾灸']
while  sum < 2 :
    driver.find_element(By.ID,"com.juyang.mall:id/rb_ShoppingMall").click() #点击商城
    sleep(4)
    driver.find_element(By.ID,'com.juyang.mall:id/tv_rightL').click()   #点击搜索
    sleep(4)
    driver.find_element(By.NAME,u"请输入关键词").send_keys(u'艾灸')
    sleep(4)
    driver.press_keycode(66) #模拟回车按键
    sleep(4)
    driver.find_element(By.NAME,search[sum]).click()
    sleep(4)
    driver.find_element(By.NAME,u"立即购买").click()
    sleep(4)
    driver.find_element(By.NAME,u"立即支付").click()
    #确认支付断言
    contain = driver.find_element(By.ID,"com.juyang.mall:id/tv_ToPay").text
    try:
        if u'确认' in contain:
            print "testcase is pass!"
    except Exception,msg:
        print msg
    finally:
        driver.close_app()   #关闭应用
        sleep(3)
        driver.launch_app()  #开启应用
        name = driver.is_app_installed("com.juyang.mall")
        print name
        sleep(3)
    sum = sum + 1
else:
    print "end---------->"

