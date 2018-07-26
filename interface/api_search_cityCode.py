#使用unittest单元测试框架进行接口测试

import unittest,requests
from other import read_json
import HTMLTestRunner,time

class Search_API(unittest.TestCase):
    def setUp(self):
        url = 'http://www.pingan.com/cms-tmplt/pinganlife/synShopList.do'

    def test_courrect_successful(self):
        '''接口测试用例1'''
        date_list = {'dateUpdated':'2018-03-04'}
        url = 'http://www.pingan.com/cms-tmplt/pinganlife/synShopList.do'
        r = requests.post(url,params=date_list)
        self.assertEqual(str(0), read_json.loads(r.text)['resultCode'])
        self.assertEqual(200, r.status_code)

    def test_courrect_failed(self):
        '''接口测试用例2'''
        date_list = {'dateUpdated':'20180304'}
        url = 'http://www.pingan.com/cms-tmplt/pinganlife/synShopList.do'
        r = requests.post(url,params=date_list)
        self.assertEqual(str(1), read_json.loads(r.text)['resultCode'])
        self.assertEqual(200, r.status_code)

    def test_courrect_failed02(self):
        '''接口测试用例3'''
        date_list = {'dateUpdated':''}
        url = 'http://www.pingan.com/cms-tmplt/pinganlife/synShopList.do'
        r = requests.post(url,params=date_list)
        self.assertEqual(str(1), read_json.loads(r.text)['resultCode'])
        self.assertEqual(200, r.status_code)

    def test_courrect_failed03(self):
        '''接口测试用例4'''
        date_list = {'dateUpdated':'2018nuimin'}
        url = 'http://www.pingan.com/cms-tmplt/pinganlife/synShopList.do'
        r = requests.post(url,params=date_list)
        self.assertEqual(str(1), read_json.loads(r.text)['resultCode'])
        self.assertEqual(200, r.status_code)

    def tearDown(self):
        pass

if  __name__ =="__main__":
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    report_dir = now + r'result.html'
    re_open = open(report_dir, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(Search_API)
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=re_open,
        title=u'API接口测试报告',
        description=u'API接口测试报告---接口测试详情')
    runner.run(suite)





# url = 'http://www.pingan.com/cms-tmplt/pinganlife/synShopList.do'
# date_list = {'dateUpdated':'2018-03-04'}
# r = requests.post(url,params=date_list)
# print(r.url)
# print(r.text)
# json_r = r.json()
# print(json_r['resultCode'])






