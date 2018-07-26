#coding=utf-8

import os,requests,json

def tokenpath():
    '''
    定义token地址
    :return:
    '''
    cur = os.path.abspath(".")
    print(cur)
    return  os.path.join(cur,"token.md")

def getToken():
    '''读取存储在文件中的token'''
    with open(tokenpath(),"r") as  f:
        return f.read()

def gettoken():
    url = "http://api.qa.97ting.com"
    path = "/tango-oauth/oauth/getAccessTokenSig"
    payload = {"oauth_consumer_key": "HWAndroidClient",
               "oauth_consumer_sig": "28C3058C9EFB2CC8935C19444FD6B9AE",
               "clientid": "AndroidClient", "clientsecret": 1}
    headers = {"did": "28C3058C9EFB2CC8935C19444FD6B9AE",
               "uid": "EE7CB17609E92711",
               "ua": "XMAndroidClient"}
    '''把token写入文件中'''
    r = requests.post(url=url+path,data=payload,headers=headers)
    with open(tokenpath(),"w") as  f:
        f.write(r.json()["data"]["access_token"])
gettoken()
