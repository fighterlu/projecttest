#coding=utf-8

from  selenium  import  webdriver
from  public.common import Login,Gouwu
import unittest

class Test_Ecshop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://192.168.1.104:8011/ecshop/"

    def Login(self,username,passwd):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//*[@id='ECS_MEMBERZONE']/a[1]/img").click() #登录
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(passwd)
        driver.find_element_by_name('submit').click()

    def test_delete(self):
        self.Login('luruifeng','123456')
        Gouwu(self)
        text=self.driver.find_element_by_xpath('//*[@id="formCart"]/table[2]/tbody/tr/td[1]').text
        self.assertEqual(text,u'购物金额小计 ￥0.00元，比市场价 ￥0.00元 节省了 ￥0.00元 (0)')


    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()













