# coding=utf-8
from time import sleep
import pytest
try:
    from page_obj.baidu_page import BaiduPage
except ImportError:
    from .page_obj.baidu_page import BaiduPage


def test_baidu_a_setting(browser):
    bd = BaiduPage(browser)
    bd.open()
    bd.search_input("pytest")
    bd.search_button()


def test_baidu_a_setting2(browser):
    bd = BaiduPage(browser)
    bd.open()
    bd.search_input("python")
    bd.search_button()


def test_baidu_a_setting3(browser):
    bd = BaiduPage(browser)
    bd.open()
    bd.search_input("selenium")
    bd.search_button()



'''
# 参数化
@pytest.mark.parametrize(
    ("searchkey"),
    ["python", "pytest","pytest-html","selenium","unittest"]
    )
def test_baidu_search(searchkey, browser):
    bd= BaiduPage(browser)
    bd.open()
    bd.search_input(searchkey)
    bd.search_button()
    sleep(1)
    title = bd.search_title()
    assert title == searchkey+"_百度搜索"
'''

# this is test test_case.
#def test_close_browser(browser):
#    browser.quit()



if __name__ == "__main__":
    pytest.main(["-s","test_baidu_search.py"])
