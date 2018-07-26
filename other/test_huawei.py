#coding=utf-8

import json,unittest,requests,os
from tokena import getToken
import time
print(getToken())
class INterfaceTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://api.qa.97ting.com"
        self.headers= {"did": "28C3058C9EFB2CC8935C19444FD6B9AE",
                      "uid": "EE7CB17609E92711",
                      "ua": "XMAndroidClient"}

    def tearDown(self):
        time.sleep(2)

    def test_login(self):
        '''获取华为登录接口'''
        path = "/tango-saa/login/loginByToken"
        payload = {"accessToken":"hwdddddddd"}
        # self.headers["oauth_token"] = getToken()
        r = requests.post(url=self.url+path,
                          json=payload,
                          headers={"did": "28C3058C9EFB2CC8935C19444FD6B9AE",
                                   "uid": "EE7CB17609E92711",
                                   "ua": "XMAndroidClient","oauth_token":getToken()})
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
