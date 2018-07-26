#coding=utf-8

import json
import json
# def json_basic():
#     data={
#         'ID':1,
#         "课程":'python',
#         "机构":'shenzhen',
#         "单价":'12.2',
#         "网址":'http://www.baidu.com'
#     }
#
#     print('原始数据')
#     print(data)
#     print('-'*20)
#     json_str = json.dumps(data)
#     print(json_str)
#     print('还原数据')
#     print('-'*20)
#     json_data = json.loads(json_str)
#     print(json_data)
#
# json_basic()


# import json
# def json_writer_file():
#     '''写json文档'''
#     data={
#         'ID':1,
#         "课程":'python精讲',
#         "机构":'深圳',
#         "单价":'12.2',
#         "网址":'http://www.baidu.com'
#         }
#     with open('data.json','w') as f:
#         json.dump(data, f)
#
# if __name__ == '__main__':
#     json_writer_file()

#
# def json_read_file():
#     '''读取json文件'''
#     with open('data.json') as f:
#         data = json.load(f)
#         print(data)
#
# if __name__ == '__main__':
#     json_read_file()
#
def json_type_diff():
    '''类型差异'''
    # print(json.dumps(False)) #false
    # print(json.dumps(None))  #null
    data = {
        'discontinued':False,
        'Title':'iphone7s',
        'Category':None,
        'Price':5999.0
    }
    print(json.dumps(data))

if __name__ == '__main__':
    json_type_diff()
# if __name__ == '__main__':
#     json_basic()
#     json_writer_file()
#     json_read_file()
#     json_type_diff()



