#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:wuya

from other import read_json

'''
序列化可以理解为：把python的对象编码转换为json格式的字符串
序列化：就是把python内置数据类型(list,tuple,dict)转为str(json格式)
json--->dump  dumps


json格式的字符串：格式--->json   类型:str

反序列化可以理解为：把json格式字符串解码为python数据对象。
反序列化：就是把str(json格式)转为python内置数据类型(list,dict)
json--->load loads

'''

# dict1={"status":0,"msg":"",
#        "data":{"tn":100,"records":[{"id":12963,"type":0,"face_value":60,"vpl":"\u9655AJ8888","status":2,"ctime":1526529511,"ex_type":1,"stime":1526529511,"etime":1526615911,"in_time":1526529441,"out_time":1526529449,"stay_time":8,"charge":1,"derate":8,"memo1":"","memo2":"","memo3":"","send_people":"\u81ea\u52a8\u5316\u6d4b\u8bd5","send_status":0,"mode":0,"seller":""},{"id":12962,"type":0,"face_value":60,"vpl":"\u9655AJ8888","status":2,"ctime":1526529484,"ex_type":1,"stime":1526529484,"etime":1526615884,"in_time":1526529415,"out_time":1526529421,"stay_time":6,"charge":1,"derate":6,"memo1":"","memo2":"","memo3":"","send_people":"\u81ea\u52a8\u5316\u6d4b\u8bd5","send_status":0,"mode":0,"seller":""},{"id":12961,"type":0,"face_value":60,"vpl":"\u9655AJ8888","status":2,"ctime":1526529459,"ex_type":1,"stime":1526529459,"etime":1526615859,"in_time":1526529390,"out_time":1526529396,"stay_time":6,"charge":1,"derate":6,"memo1":"","memo2":"","memo3":"","send_people":"\u81ea\u52a8\u5316\u6d4b\u8bd5","send_status":0,"mode":0,"seller":""},{"id":12960,"type":0,"face_value":60,"vpl":"\u9655AJ8888","status":2,"ctime":1526529434,"ex_type":1,"stime":1526529434,"etime":1526615834,"in_time":1526529364,"out_time":1526529372,"stay_time":8,"charge":1,"derate":8,"memo1":"","memo2":"","memo3":"","send_people":"\u81ea\u52a8\u5316\u6d4b\u8bd5","send_status":0,"mode":0,"seller":""},{"id":12959,"type":0,"face_value":60,"vpl":"\u9655AJ8888","status":2,"ctime":1526529341,"ex_type":1,"stime":1526529341,"etime":1526615741,"in_time":1526529272,"out_time":1526529278,"stay_time":6,"charge":1,"derate":6,"memo1":"","memo2":"","memo3":"","send_people":"\u81ea\u52a8\u5316\u6d4b\u8bd5","send_status":0,"mode":0,"seller":""},{"id":12958,"type":0,"face_value":60,"vpl":"\u9c81BD12368","status":2,"ctime":1526529321,"ex_type":1,"stime":1526529321,"etime":1526615721,"in_time":1526529251,"out_time":1526529258,"stay_time":7,"charge":1,"derate":7,"memo1":"","memo2":"","memo3":"","send_people":"\u81ea\u52a8\u5316\u6d4b\u8bd5","send_status":0,"mode":0,"seller":""},{"id":12957,"type":0,"face_value":60,"vpl":"\u9c81BD12368","status":2,"ctime":1526529296,"ex_type":1,"stime":1526529296,"etime":1526615696,"in_time":1526529225,"out_time":1526529234,"stay_time":9,"charge":1,"derate":9,"memo1":"","memo2":"","memo3":"","send_people":"\u81ea\u52a8\u5316\u6d4b\u8bd5","send_status":0,"mode":0,"seller":""},{"id":12956,"type":2,"face_value":1,"vpl":"\u9655AJ8888","status":2,"ctime":1526529206,"ex_type":1,"stime":1526529206,"etime":1526615606,"in_time":1526529136,"out_time":1526529143,"stay_time":7,"charge":1,"derate":7,"memo1":"","memo2":"","memo3":"","send_people":"\u81ea\u52a8\u5316\u6d4b\u8bd5","send_status":0,"mode":0,"seller":""},{"id":12955,"type":2,"face_value":1,"vpl":"\u9655AJ8888","status":2,"ctime":1526529183,"ex_type":1,"stime":1526529183,"etime":1526615583,"in_time":1526529114,"out_time":1526529121,"stay_time":7,"charge":1,"derate":7,"memo1":"","memo2":"","memo3":"","send_people":"\u81ea\u52a8\u5316\u6d4b\u8bd5","send_status":0,"mode":0,"seller":""},{"id":12954,"type":2,"face_value":1,"vpl":"\u9655AJ8888","status":2,"ctime":1526529159,"ex_type":1,"stime":1526529159,"etime":1526615559,"in_time":1526529090,"out_time":1526529096,"stay_time":6,"charge":1,"derate":6,"memo1":"","memo2":"","memo3":"","send_people":"\u81ea\u52a8\u5316\u6d4b\u8bd5","send_status":0,"mode":0,"seller":""}]}}
#
# print dict1['data']['records'][0]['id']


u'''字典进行序列化与反序列化'''

# print u'对字典进行序列化的处理:\n'
#
# dict1={'name':'wuya','address':'xian'}
#
# print u'字典未序列化之前的内容：{0}，数据类型：{1}\n'.format(dict1,type(dict1))
#
# #对字典进行序列化
# dict_str=json.dumps(dict1)
#
# print u'字典dict1序列化后内容：{0}，类型：{1}\n'.format(dict_str,type(dict_str))
#
# print u'对字典进行反序列化的处理:\n'
#
# dict3=json.loads(dict_str)
#
# print u'字符串dict_str反序列化后的内容：{0}，类型：{1}'.format(dict3,type(dict3))



u'''对列表进行序列化与反序列化'''
# list1=[1,2,3,4,5]
#
# print u'没有序列化之前内容：{0}，类型：{1}'.format(list1,type(list1))
# print u'对列表list1进行序列化的处理：'
#
# #对列表进行序列化的处理
# list_str=json.dumps(list1)
# print u'列表list1经过序列化之后内容：{0},类型：{1}'.format(list_str,type(list_str))
#
# #对列表进行反序列化的处理
# list3=json.loads(list_str)
# print u'字符串list_str经过反序列化之后内容：{0},类型：{1}'.format(list3,type(list3))

u'''对元组进行序列化与反序列化'''
# tuple1=(1,2,3,4,5)
#
# print u'元组序列化之前的内容：{0}，类型：{1}'.format(tuple1,type(tuple1))
#
# #对元组进行序列化
# tuple_str=json.dumps(tuple1)
#
# print u'元组tuple1序列化之后的内容：{0}，类型：{1}'.format(tuple_str,type(tuple_str))
#
# #对元组进行反序列化
# tuple3=json.loads(tuple_str)
#
# print u'字符串tuple_str反序列化之后的内容：{0}，类型：{1}'.format(tuple3,type(tuple3))



u'''序列化与反序列化的案例介绍'''

data = {"username": "", "password": ""}

print type(data)
# r = requests.post(
#     url='http://180.97.80.42:9090/v4/login',
#     headers={'Parkingwang-Client-Source': 'ParkingWangAPIClientWeb',
#              'Content-Type': 'application/json;charset=UTF-8'},
#     # 对data进行序列化的处理-->字典转为str类型
#     data=json.dumps(data))

#
# print json.loads(str(r.text))['msg']

u'''文件的序列化与反序列化:
序列化：就是把内容写到文件中
反序列化：读取文件中的数据
'''

import  requests

r=requests.get(url='https://www.amazon.cn/gp/navigation/ajax/dynamic-menu.html?primeContent=prime&metricKey=primeMetric&rid=VM9V73SCYCWZDWS2XND8&isFullWidthPrime=0&isPrime=0&dynamicRequest=1&weblabs=&isFreshRegionAndCustomer=&primeMenuWidth=310&_=1526048424170',
               headers={'Cookie':'x-wl-uid=1azzbZ/Chwg4eL0XCHh0zIvHwkZVpHXZdAlsjSlM0ZXPj2xMwHvxtOL+iepkIsasvx9zPsr81C7vEwfYstHFyihrkiWVxkjRxEG23TxC0bCamtlJKGo5DhwQLcCl+EhXhy4P81d2VEOs=; at-main=Atza|IwEBIJvSlQ-Ptdgh-9HpOwEno2eWONGs4ooDBS1bSjoZf6R3pqiRKHzf6xPdxER7yQKG6eBu_AmUXHXQP-1Bi0UPCHOKeoCD8ASe0eCrksn-1Xr3DlEZdKPX7Ht9_nYw9egT8o-ZcEDjyq8GJ6m2Ig1qFnvpwir6sL35X8vi7NfWaO9MAq4_Vj_46vPgiWXZTmARQplMdfD8TTOPpW8lROk02vlW0IsCgmBOyYXngUjsh-nbCmtmM8YH0y69130Pw8k6u4COJD8JnL9P5dykIWgug2cejkGNk1po0wk0l-kxyFKNykGW8BGmSadxkFomFgKdZsEMPU2uniNLo3Ge0pcqcuVrDXBypXTB2rL2nnTSg3z_-n0ZDPMwT3CCUp4siLBSkc-o0e7dGKhl-6uA0vRGz3TJ; sess-at-main="XQ7X4ehxIwU2AH15SdJTmSbMZ2fMK9hPrm4ynZoeC9M="; sst-main=Sst1|PQHcm0EcXFq-MzDeEYNkZQf1C2hw6auGBQYruCdmhtLx-FB8l-l3Ebr8LWwp1Vahw0-8BMJ3tEf-5oyDSF3gH4Vt8-2KeWbcrNhXAuKh4ZL3stHKYxcWNB9T3K1Yb74DzThm7JGYNA5DXdHeR17DmX_bfEPC-m6H6yBCxCMFUBsBnqbog_WCYVhhhLcEKngaUWMI1-WVYkoRfX_t5PeleJBftwZp7s5VGGWpqOjGJwUYXM0BZHlUCxM1lEMR5xzickpBGDeAWwaY7UcblLEZCkwcQ8WWPWZnQpj_9KXq78sQOIkuyVPEgmWwHsX1C45O2Lgz-dZCo91s3UWVv7DrV-WYMg; x-acbcn="YHr@jetPGmzH7TlwwlX9QQKsWHWre2jlaCiOoYubtuMSFDporwvUMtBp?5cgTNbK"; lc-acbcn=zh_CN; session-token=GolQttxXDREZ5cnnvVuNfaeHZNglTTT79Q5/YsS2j6bV26pgys0Zd7ZQGMTsyNvQxbNl5Q0U66MSg8d3oP6iUT00WNpz4gCB2OUtrMmuP2IHYn13iWxrSxls423grBva/6A9YuGuSmQ0hX4HSN3rECiC/sc7Op1NAEAxhf1Ed5+jaQRpiN9pgICgWDXu8FN7l/UM0tkCDIb+CsXoSU4ETZ/5XFEJ4/AbdPKeYIdQpt07jimJBxs+fEP9XGhVTrZcPvukVbhmR+M=; csm-hit=s-Q7CN1EB13R3T7CQ39VKX|1526048280570; ubid-acbcn=461-4957819-3544458; session-id-time=2082729601l; session-id=462-4869566-9334243'})
#对文件进行序列化( 把内容写到文件中)
read_json.dump(r.json(), open('am', 'w'))

#对文件进行反序列化
print  read_json.load(open('am', 'r'))['cart']['fresh']['count']