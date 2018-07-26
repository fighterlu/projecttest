
import unittest
import requests
import time,HTMLTestRunner
from other import read_json


class Search_City(unittest.TestCase):
    def setUp(self):
        self.url = 'http://183.62.167.17:10158/CyzgMobileConfigService/GetDataInfo'
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}

    def tearDown(self):
        pass

    def test_success_info(self):
        '''接口测试用例1  '''
        payload = {'CommandCode': 'GetAllCityData', 'Marker': '1482738389646',"TransferData": "{\'CityId\':430100}"}
        r = requests.post(self.url, data=read_json.dumps(payload), headers=self.headers)
        print(r.status_code)
        assert '获取成功' in read_json.loads(r.text)["ErrorInfo"]

    def test_success_failed1(self):
        '''接口测试用例2 '''
        payload = {'CommandCode': 'GetAllCityData', 'Marker': '1482738389646',"TransferData": "{\'CityId\':43}"}
        r = requests.post(self.url, data=read_json.dumps(payload), headers=self.headers)
        print(r.status_code)
        assert '未找到' in read_json.loads(r.text)["ErrorInfo"]
        self.assertEqual(200,r.status_code)

    def test_success_failed2(self):
        '''接口测试用例3 '''
        payload = {'CommandCode': 'GetAllCityData', 'Marker': '1482738389646',"TransferData": "{\'CityId\':}"}
        r = requests.post(self.url, data=read_json.dumps(payload), headers=self.headers)
        print(r.status_code)
        assert '无效的 JSON 基元: 。' in read_json.loads(r.text)["ErrorInfo"]
        self.assertEqual(200,r.status_code)

    def test_success_failed3(self):
        '''接口测试用例4 '''
        payload = {'CommandCode': 'GetAllCityData', 'Marker': '1482738389646',"TransferData": "{\'CityId\':123456}"}
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        r = requests.post(self.url, data=read_json.dumps(payload), headers=self.headers)
        print(r.status_code)
        assert '未找到' in read_json.loads(r.text)["ErrorInfo"]
        self.assertEqual(200,r.status_code)

if __name__ == '__main__':
    # unittest.main(verbosity=4)
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    report_dir = now + r'result.html'
    re_open = open(report_dir, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(Search_City)
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=re_open,
        title=u' ---API接口测试报告---',
        description=u'API接口测试报告---接口测试详情'
    )
    runner.run(suite)



url = 'http://183.62.167.17:10158/CyzgMobileConfigService/GetDataInfo'
# payload ={'CommandCode':'GetAllCityData','Marker':'1482738389646',"TransferData":"{\'CityId\':430100}"}
# payload ={'CommandCode':'GetAllCityData','Marker':'1482738389646',"TransferData":"{\'CityId\':43}"}
payload ={'CommandCode':'GetAllCityData','Marker':'1482738389646',"TransferData":"{\'CityId\':123456}"}
headers = {'Content-Type':'application/json;charset=UTF-8'}

#把字典转换成json字符串 json.dumps(data)
#把json字符串转换为字典数据类型 json.loads(data)
# r = requests.post(url,data=json.dumps(payload),headers=headers)
# print(r.text)
# print(json.loads(r.text)["ErrorInfo"])
# assert  '获取成功' in json.loads(r.text)["ErrorInfo"]
# assert  '未找到' in json.loads(r.text)["ErrorInfo"]
# assert  '无效的 JSON 基元: 。' in json.loads(r.text)["ErrorInfo"]






