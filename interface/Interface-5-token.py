#coding=utf-8

import  requests
import  unittest
import  time as t

class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.url='https://ecapi.parkingwang.com/v4/'
        self.headers={'Content-Type':'application/json;charset=UTF-8','Parkingwang-Client-Source':'ParkingWangAPIClientWeb'}
        self.timeout=5

    def tearDown(self):
        t.sleep(1)

    def getToken(self):
        r = requests.post(
            url=self.url+'login',
            json={"username": "autoapi", "password": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92","role": 2},
            headers=self.headers, timeout=self.timeout)
        return r.json()['data']['token']

    def test_infoGet(self):
        '''验证:测试infoGet接口是否正确'''
        r = requests.post(
            url=self.url+'infoGet',json={"token": self.getToken()},headers=self.headers, timeout=self.timeout)
        self.assertEqual(r.json()['status'],0)
        self.assertEqual(r.json()['data']['username'],'autoapi')

    def test_isSoonExpire(self):
        '''验证：测试isSoonExpire接口是否正确'''
        r = requests.post(
            url='https://ecapi.parkingwang.com/v4/isSoonExpire',json={"token":self.getToken()},headers=self.headers, timeout=5)
        self.assertEqual(r.json()['status'],0)
        self.assertEqual(r.json()['data']['expire'],False)

if __name__ == '__main__':
    unittest.main(verbosity=2)
