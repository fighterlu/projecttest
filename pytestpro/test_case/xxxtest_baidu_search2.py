# coding=utf-8
from time import sleep
import pytest
try:
    from page_obj.baidu_page import BaiduPage
except ImportError:
    from .page_obj.baidu_page import BaiduPage



def test_baidu_a_setting(browser):
    bd  = BaiduPage(browser)
    bd.open()
    bd.setings()
    bd.search_setting()
    bd.save_seting()

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


# this is test test_case.
#def test_close_browser(browser):
#    browser.quit()



if __name__ == "__main__":
    pytest.main("-s test_baidu_search.py")
