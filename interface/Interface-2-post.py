#coding=utf-8

'''
	1.带参数的post请求示例 
'''

'''
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
'''

'''
	2.发送json参数格式的post请求
'''
'''
r = requests.post('https://api.github.com/some/endpoint',data=json.dumps({'some': 'data'}))
print(r.json())
url = 'https://api.github.com/some/endpoint'
# 或者2.4.2 版的新加功能,可以使用 json 参数直接传递，然后它就会被自动编码
payload = {'some': 'data'}
r = requests.post(url, json=payload)
print(r.json())
'''


'''
	3.post请求定制headers 
'''
'''
data = {'some': 'data'}
headers = {'content-type': 'application/json',
		  'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
r = requests.post(url='https://api.github.com/some/endpoint', data=data, headers=headers)
print(r.text)
print(r.json()['documentation_url'])
'''

'''
	5.post请求带form表单数据 
'''
'''
# 带一个参数
r=requests.post('http://fanyi.baidu.com/langdetect',data={'query': 'python'})
print(r.text)
# 带多个参数
r=requests.post('http://fanyi.baidu.com/v2transapi',data={'query': 'python','from':'en','to':'zh'})
print(r.text)
'''




















