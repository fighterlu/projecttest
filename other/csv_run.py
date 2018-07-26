#coding=utf-8

# def txt_writer():
#     '''写文件'''
#     with open('database.txt','w',encoding='utf-8') as f:
#         f.write('博客地址 \n')
#         lines = [
#             '地址：京基一百 \n',
#             'qq:2393989903 \n',
#             '网址：www.cnblogs.com/fighter007'
#         ]
#         f.writelines(lines)
#
# def txt_read():
#     '''读文件'''
#     with open('database.txt',encoding='utf-8') as f:
#         for line in f:
#             print(line,end='')
#
# if __name__ == '__main__':
#     txt_writer()
#     txt_read()



import csv

def csv_reader():
    '''写入csv文件'''
    headers = ['编号','课程','讲师']

    rows = [
        (1,'[Python','fighter.Lu'),
        (2,'C#','fighter.Lu'),
        (3,'.Net','fighter.Lu')
    ]

    with open('my_course.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
#
# if __name__ == '__main__':
#     csv_reader()


def csv_writer():
    '''读取csv文件'''
    with open('my_course.csv',encoding='utf-8') as f:
        reader  = csv.DictReader(f) #字典表 DictReader  列表读取  reader
        headers = next(reader)  #迭代一次
        print(headers)
        for row in reader:
            print(row)
            # print(row['编号'])

if __name__ == '__main__':
    csv_writer()
    csv_reader()



# def csv_writer_dict():
#     '''以dict形式写入csv'''
#     headers =  ['ID','Title','Org','Url']
#     rows = [
#         {'ID': 1, 'Title': 'python', 'Org': 'python', 'Url': 'http://www.fighter.com'},
#         {'ID': 2, 'Title': 'python', 'Org': 'python', 'Url': 'http://www.fighter.com'},
#         {'ID': 3, 'Title': 'python', 'Org': 'python', 'Url': 'http://www.fighter.com'},
#         {'ID': 4, 'Title': 'python', 'Org': 'python', 'Url': 'http://www.fighter.com'},
#         {'ID': 5, 'Title': 'python', 'Org': 'python', 'Url': 'http://www.fighter.com'},
#         {'ID': 6, 'Title': 'python', 'Org': 'python', 'Url': 'http://www.fighter.com'},
#         dict(ID=5, Title='C#',Org='python',Url='http://www.cnblogs.com/fighter007'),
#         dict(ID=6, Title='C#',Org='python',Url='http://www.cnblogs.com/fighter007'),
#         dict(ID=7, Title='C#',Org='python',Url='http://www.cnblogs.com/fighter007')
#     ]
#     with open('my_course2.csv','w',encoding='utf-8',newline='') as f:
#         writer = csv.DictWriter(f,headers)
#         writer.writeheader()
#         writer.writerows(rows)
#
# def csv_dict_read():
#     '''读取csv_writer_dict文件'''
#     with open('my_course2.csv',encoding='utf-8') as f:
#         reader  = csv.DictReader(f) #字典表 DictReader  列表读取  reader
#         headers = next(reader)  #迭代一次
#         print(headers)
#         for row in reader:
#             print(row)
#             # print(row['编号'])
#
# if __name__ == '__main__':
#     csv_writer()
#     csv_reader()
#     csv_writer_dict()
#     csv_dict_read()
#
#


