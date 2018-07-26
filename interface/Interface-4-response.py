#coding=utf-8

import requests

'''
	4. Response 对象
'''

r=requests.get('https://httpbin.org/get')
print('HTTP状态码:',r.status_code)
print('返回原始响应体',r.raw)
print('请求的响应体',r.content)
print('响应内容',r.text)
print('获取headers',r.headers) #以字典对象存储服务器响应头
#*特殊方法*#
print(r.json())  #Requests 中内置的 JSON 解码器
print(r.raise_for_status()) #失败请求(非 200 响应)抛出异常

print('*'*100)
print('*'*100)
print('*'*100)

r=requests.get('http://www.bing.com')

print ('HTTP状态码:',r.status_code)
print ('请求的URL:',r.url)
print ('获取Headers:',r.headers)
print ('响应内容:',r.text)

