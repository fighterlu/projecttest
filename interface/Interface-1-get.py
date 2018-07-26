#coding=utf-8

'''
	1.get请求示例
'''
'''
r = requests.get(url='http://www.baidu.com',timeout=1) # 最基本的 GET 请求,timeout 请求超时时间
print(r.status_code)  # 获取返回状态
print(r.text)
'''

'''
	2.get请求带参数示例
'''
'''
r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'}) # 带参数的 GET 请求
print(r.url)  # 请求的 url
print(r.text) # 解码后的返回数据
'''


'''
	3.get请求带参数示例(将一个列表作为值传入)
'''
'''
payload = {'key1': 'value1', 'key2': ['value2', 'value3']} # 可以将一个列表作为值传入
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url) # 会重复拼接 url
'''

'''
	4.get请求定制请求头信息 headers 
'''

'''
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.text)
'''



















