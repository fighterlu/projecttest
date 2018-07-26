#coding=utf-8


from selenium import webdriver
import unittest

class  Info(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('http://www.baidu.com')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


def text_create(name,msg):
    # 创建文件，写入信息
    desktop_path = '/Users/duwangdan/Desktop/'
    # 桌面路径
    full_path = desktop_path + name + '.txt'
    # 桌面路径+文件名+文件后缀
    file = open(full_path,'w')
    # 'w'参数指写入
    file.write(msg)
    # 文件中写入信息
    file.close()
    # 写入后关闭文件


def text_filter(word,censored_word='Awesome',change_word=''):
     # 文本过滤函数
     return word.replace(censored_word,change_word)
     # 用replace()方法替换敏感词


def censored_text_create(name,msg):
    # 创建删除敏感词后的文本函数
    clean_msg = text_filter(msg)
    # 过滤掉msg中的敏感词
    text_create(name,clean_msg)
    # 传入name和clean_msg到text_create函数中
censored_text_create('test','Math is Awesome!')






































