#coding=utf-8

import xlrd

def read_excel():
    '''excel读取'''
    book = xlrd.open_workbook('xxx.xls')
    for sheet in book.sheets():
        print(sheet)
        # print(sheet.name)

def xl_read_data():
    '''excel数据读取'''
    book = xlrd.open_workbook('xxxx.xls')
    sheet = book.sheet_by_index(0)  # 找第一个工作目录 或者用name
    # sheet = book.sheet_by_name('工作名字')
    print('工作目录：{}'.format(sheet))
    print('数据行数：{}'.format(sheet.nrows)) #文件行数
    print('产品数据')
    print('='*50)
    for  i  in range(sheet.nrows):  #循环行数 第一行做什么
        print(sheet.row_values(i))  #row_values()是那一行？ 获取索引数据行

if __name__ == '__main__':
    read_excel
    xl_read_data()

