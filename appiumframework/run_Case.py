#coding=utf-8


import unittest,os,time
from Public import HTMLTestRunner

cur_path = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(cur_path,'testCase')
report_path = os.path.join(cur_path,'Result')

if __name__ == '__main__':
    testlist = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    report_name = report_path + '\\' + now_time + 'result.html'
    fp = HTMLTestRunner.HTMLTestRunner(stream=open(report_name,'wb'),
                                       title='appium-po设计模式自动化测试报告',
                                       description='window7 夜神模拟器艾人针灸')
    fp.run(testlist)



