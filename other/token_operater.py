#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import  unittest
import  time as t
import  os

def getHeaders():
    '''获取headers'''
    return {'Content-Type':'application/json;charset=UTF-8','Parkingwang-Client-Source':'ParkingWangAPIClientWeb'}

def tokenpath():
    '''
    定义token地址
    :return:
    '''
    cur = os.path.abspath('.')
    print(cur)
    return  os.path.join(cur,'token.md')


def login():
    url = 'http://www.imsam.cn:3000'
    '''把token写入到文件中'''
    r = requests.post(
        url=url+'/login',json={'username':'admin123',
                               'password':'admin123','password_confirmation':'admin123'})
    with open(tokenpath(),'w') as f:
        f.write(r.json()['token'])


def getToken():
    '''读取存储在文件中的token'''
    with open(tokenpath(),'r') as f:
        return f.read()


class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.url='http://www.imsam.cn:3000'
    def tearDown(self):
        t.sleep(1)

    def test_getApiTasks(self):
        '''验证:测试login接口是否正确'''
        r = requests.get(url=self.url + '/api/tasks',headers={'Authorization':'Bearer ' + getToken()})
        self.assertEqual(r.status_code,200)

    def test_getTasks(self):
        ''''验证：获取所有任务api接口是否正确'''
        r = requests.get(url=self.url + '/api/tasks',headers={'Authorization':'Bearer ' + getToken()})
        self.assertEqual(r.status_code,200)

if __name__ == '__main__':
    unittest.main(verbosity=2)