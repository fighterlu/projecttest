#coding=utf-8

#7. 序列化和反序列化  json.dumps(a)  json.loads(a)
import requests
from other import read_json

print(read_json.__all__)

dict1 = {'name':'luruifeng','age':28,'address':'深圳'}
print("未序列化之前的数据类型是：",type(dict1))
print('序列化前的数据是：',dict1)

print('-'*30)

#对dict1进行序列化操作
str1 = read_json.dumps(dict1)
print('序列化后的数据类型是：',type(str1))
print('序列化后的数据为：',str1)

print('-'*30)

#对str1进行返序列化
str = read_json.loads(str1)
print('返序列化后的数据类型是：',type(str))
print('返序列化后的数据为：',str)

print('-'*30)

#又或者：
r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=北京")
print(r.text)
print(type(r.text))  #json字符串
result = read_json.loads(r.text)
print(read_json.dumps(result, ensure_ascii=False))  #字典
print(type(result))
