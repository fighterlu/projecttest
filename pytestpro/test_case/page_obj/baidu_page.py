# coding=utf-8
try:
    from base import Pyse
except ImportError:
    from .base import Pyse
from time import sleep


class BaiduPage(Pyse):
    '''
    百度首页
    '''
    url = '/'

    # 百度输入框
    def search_input(self,searchkey):
        self.type("id=>kw", searchkey)

    # 百度按钮
    def search_button(self):
        self.click("id=>su")
        sleep(1)

    # 搜索标题
    def search_title(self):
        return self.get_title()

    # 设置
    def setings(self):
        self.click("link_text=>设置")

    # 搜索设置
    def search_setting(self):
        self.click("class=>setpref")

    # 保存设置
    def save_seting(self):
        self.click("class=>prefpanelgo")
        self.accept_alert()






