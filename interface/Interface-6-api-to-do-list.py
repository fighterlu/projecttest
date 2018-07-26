#coding=utf-8

import requests
from other import read_json

'''
    1.注册接口
'''

url ='http://www.imsam.cn:3000'
r = requests.post(url=url+'/register',
                  data={'username':'username','password':'password',
                        'password_confirmation':'password'},
                  timeout=1)
print (r.json()['id'])


'''
    2.登陆接口
'''

url ='http://www.imsam.cn:3000'
data={'username':'username',
      'password':'password',
      'password_confirmation':'password'}

def getToken(url,data):
    r = requests.post(
        url=url+'/login',data=data,timeout=2)
    token = r.json()['token']
    return token

print (getToken(url,data))




'''
    3.获取所有任务api
'''

import requests

#获取token
api_url = 'http://www.imsam.cn:3000'
payload = {'username':'username',
              'password':'password',
              'password_confirmation':'password'}
def getToken():
    r = requests.post(
        url = api_url + '/login',
        data=payload,
        timeout=2)
    return 'Bearer ' + r.json()['token']

#获取所有任务
r = requests.get(
    url=api_url + '/api/tasks',
    headers={'Authorization':getToken()},timeout=5)

print(r.status_code)
print(r.json())



'''
    4.创建任务api
'''

api_url = 'http://www.imsam.cn:3000'
payload = {'username':'username',
              'password':'password','password_confirmation':'password'}
#获取token
def getToken():
    r = requests.post(
        url = api_url + '/login',
        data=payload,
        timeout=2)
    return 'Bearer ' + r.json()['token']

#创建任务api
def createTask():
    r = requests.post(
        url = api_url + '/api/tasks',
        headers = {'Authorization':getToken()},
        data = {'title':str(uuid.uuid4()),'desc':str(uuid.uuid4())})
    return r.json()
    # return r.json()
    # return json.loads(r.text)['id']
print(createTask())


'''
    5.删除任务api
'''

api_url = 'http://www.imsam.cn:3000'
payload = {'username':'username',
              'password':'password',
              'password_confirmation':'password'}
#获取token
def getToken():
    r = requests.post(
        url = api_url + '/login',
        data=payload,
        timeout=2)
    return 'Bearer ' + r.json()['token']

#创建任务api
def createTask():
    r = requests.post(
        url = api_url + '/api/tasks',
        headers = {'Authorization':getToken()},
        data = {'title':str(uuid.uuid4()),'desc':str(uuid.uuid4())})
    return read_json.loads(r.text)['id']

#删除任务api
def delteApiTask():
    r = requests.delete(
        url=api_url + '/api/tasks/:' + str(createTask()),
        headers={'Authorization':getToken()},
    timeout=2)
    return r.json()

print(delteApiTask())



'''
    6.完成任务 
'''

import requests, uuid

api_url = 'http://www.imsam.cn:3000'
payload = {'username':'username','password':'password','password_confirmation':'password'}

#获取token
def getToken():
    r = requests.post(
        url = api_url + '/login',
        data=payload,
        timeout=2)
    return 'Bearer ' + r.json()['token']

#创建任务api
def createTask():
    r = requests.post(
        url = api_url + '/api/tasks',
        headers = {'Authorization':getToken()},
        data = {'title':str(uuid.uuid4()),'desc':str(uuid.uuid4())})
    return read_json.loads(r.text)['id']

#完成任务api
def pullTask():
    r = requests.put(url=api_url + '/api/tasks/' + str(createTask()),
        headers={'Authorization':getToken()},timeout=3)
    return r.json()

print(pullTask())
















