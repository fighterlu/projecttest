#coding=utf-8

'''
import requests

requests.get('https://github.com/timeline.json')
requests.put('http://httpbin.org/put')
requests.post('http://httpbin.org/post')
requests.delete('http://httpbin/ddelete')

'''

import requests
from other import read_json

data ={'username':'18513600235','password':'123456'}
r = requests.post('http://m.cyw.com/index.php?m=api&c=login&a=authorized',data=data)

#反序列化
print(read_json.dumps(r.text))
print(r.json())
print(r.json()['code'])
