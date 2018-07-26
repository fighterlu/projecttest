#coding=utf-8

import unittest
import sys,time,os
from HTMLTestRunner import HTMLTestRunner
reload(sys)
sys.setdefaultencoding('utf-8')


path = os.path.dirname(os.path.realpath(__file__))
case = os.path.join(path,'case')
report =  os.path.join(path,'report')
test_list = unittest.defaultTestLoader.discover(case,pattern='test*.py')


if __name__ == '__main__':
    now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = report + '\\' + now_time + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'appium运行测试报告',
                            description=u'appium使用夜神模拟器登录芸归原创')
    runner.run(test_list)
    fp.close()