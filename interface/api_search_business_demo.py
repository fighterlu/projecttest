#coding=utf-8


# url = 'http://183.62.167.17:10158/CyzgMobileConfigService/GetDataInfo'
# headers = {'Content-Type': 'application/json;charset=UTF-8'}
# payload = {'CommandCode': 'GetAllCityData', 'Marker': '1482738389646',"TransferData": "{\'CityId\':432322mn}"}
#
# r = requests.post(url,headers=headers,data=json.dumps(payload)).json()
# print(r)

#430100   'ErrorInfo': '城市信息获取成功'
#      'ResultCode': 20104
#4301001111111    'ErrorInfo': '未找到数据源'
#432322mn    'ResultCode': 20104

import  requests,unittest


class Runmain(unittest.TestCase):

    def setUp(self):
        self.url =  'http://183.62.167.17:10158/CyzgMobileConfigService/GetDataInfo'
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}

    def test1(self):
        payload = {'CommandCode': 'GetAllCityData',
                   'Marker': '1482738389646', "TransferData": "{\'CityId\':430100}"}
        r = requests.post(url=self.url,headers=self.headers,json=payload)
        # print(r.json())
        self.assertIn('获取成功',r.json()['ErrorInfo'])
        self.assertEqual(200,r.status_code)

    def test2(self):
        try:
            payload = {'CommandCode': 'GetAllCityData',
                       'Marker': '1482738389646', "TransferData": "{\'CityId\':}"}
            r = requests.post(url=self.url,headers=self.headers,json=payload)
            self.assertEqual(20104,r.json()['ResultCode'])
            self.assertEqual(200,r.status_code)
        except Exception as meg:
            print('请求错误，信息如下：{a}'.format(a=meg))

    def test3(self):
        try:
            payload = {'CommandCode': 'GetAllCityData',
                       'Marker': '1482738389646', "TransferData": "{\'CityId\':4301001111111}"}
            r = requests.post(url=self.url,headers=self.headers,json=payload)
            self.assertEqual('未找到数据源',r.json()['ErrorInfo'])
            self.assertEqual(200,r.status_code)
        except Exception as meg:
            print('请求错误，信息如下：{a}'.format(a=meg))

    def test4(self):
        try:
            payload = {'CommandCode': 'GetAllCityData',
                       'Marker': '1482738389646', "TransferData": "{\'CityId\':432322mn}"}
            r = requests.post(url=self.url,headers=self.headers,json=payload)
            self.assertEqual(20104,r.json()['ResultCode'])
            self.assertEqual(200,r.status_code)
        except Exception as meg:
            print('请求错误，信息如下：{a}'.format(a=meg))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=6)

