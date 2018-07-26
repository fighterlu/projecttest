#coding=utf-8


import time

#登录模块化设计
def  Login(self,username,passwd):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//*[@id='ECS_MEMBERZONE']/a[1]/img").click() #登录
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(passwd)
        driver.find_element_by_name('submit').click()


#挑选手机
def  Gouwu(self):
        driver=self.driver
        driver.find_element_by_link_text(u"双模手机").click()
        driver.find_element_by_link_text(u'诺基亚N96').click()
        driver.find_element_by_xpath('//*[@id="ECS_FORMBUY"]/ul/li[8]/a[1]/img').click()
        driver.find_element_by_link_text(u'删除').click()  #删除商品
        time.sleep(4)
        driver.switch_to.alert.accept()      #接受弹窗
