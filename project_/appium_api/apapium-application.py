#coding=utf-8

from appium import webdriver
import  time

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '3.8.3.1',
    'deviceName': '127.0.0.1:62001',
    'appPackage': 'com.shanjian.originaldesign',
    'appActivity':'.activity.other.Activity_In'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.wait_activity('.activity.other.Activity_In',50)  # 等待app首页出现
sleep(30)

# 安装应用
driver.install_app(r'D:\android\apk\yungyc.apk')
sleep(20)
# 关闭应用
driver.close_app()
sleep(8)
# 关闭应用。这个方法与quit()有所不同，quit()是在结果测试时执行的，这个方法并非真正的关闭应用，相当于按home 键将应用置于后台，可以通过launch_app()再次启动。
# 卸载应用
# driver.remove_app('com.shanjian.originaldesign')

# 检查应用是否安装
print (driver.is_app_installed('com.shanjian.originaldesign'))
sleep(8)
# 如果安装就返回True
# 启动应用
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(8)


# 将应用置于后台
driver.background_app('com.shanjian.originaldesign')

# 注：脚本在初始化的时候就已经启动了APP，我们可以先关闭这个APP，然后在启动APP
driver.close_app()
driver.launch_app()

