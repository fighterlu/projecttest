#coding=utf-8


import unittest
import sys,time,os
from public import HTMLTestRunner

path = os.path.dirname(os.path.realpath(__file__))
case = os.path.join(path,'case')
report =  os.path.join(path,'report')
test_list = unittest.defaultTestLoader.discover(case,pattern='test*.py')

if __name__ == '__main__':
    now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = report + '\\' + now_time + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                            title=u'UI自动化测试运行报告',
                            description=u'B2C电商系统项目实战')
    runner.run(test_list)
    fp.close()



















