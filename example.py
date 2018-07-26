#coding=utf-8


#if 语句

'''
a = 10
b = 50
if a > b:
    print('a is max')
else:
    print('b is max')
'''


'''
score = 100
if   score > 600:
    print('你可以读清华了！')
    print('你好6！')
elif score < 300:
    print('你也就只能读个本科了！')
    print('读个本科也不错！')
else:
    if score == 100:
        print('只能读一个大专！')
    else:
        print('重新读大学！！')
'''


'''
import random
number = random.randint(1,5)
print(number)
guess_number = input('请输入一个数字：')
if number == int(guess_number):
    print('猜对了！666')
    print('猜对了，也没有奖励！！')
else:
    if int(guess_number) > number:
        print('猜大了！！！')
    else:
        print('猜小了！！！')
'''

'''
练习：玩个游戏动手写个猜数字的游戏，假设答案是8，
现在让用户输入一个数字，来猜大小，猜对了告诉用户猜对了，
否则就告诉用户猜错了。
'''


'''
练习：
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算
他的BMI指数，并根据BMI指数：
	低于18.5：过轻
	18.5-25：正常
	25-28：过重
	28-32：肥胖
	高于32：严重肥胖
'''

#while循环

'''
基本实例
递增
递减
实例
编程题
'''
'''
while True:
    print('死循环！')
'''
'''
a = None
b = True
a = b
while a:
    print('----->死循环！')
    pass

'''

#递增

'''
a = 1
while a < 100:
    print('当前打印的是：',a,end='->')
    a = a+1
print('\n')
'''


#递减

'''
b = 10
while b > 0:
    print('当前打印的是：',b,end='->')
    b = b - 1
'''

#打印url
'''
url = 'www.brtesting.com'
while url:
    print(url)
    url = url[1:]
'''


# 小实例

'''
import random
while True:
    number = int(input('输入一个数字：'))
    if number == random.randint(1,5):
        print('猜对了！！！666')
        break
    else:
        print('猜错了！重新猜一猜！')
        number = int(input('输入一个数字：'))
'''


#小游戏 改进版本  使用while循环
'''
guess_number = int(input('猜一个数字：'))
result = 8 
while True:
    if guess_number == result:
        print('猜对了！！！')
        print('没有奖励！')
        break
    elif guess_number > result:
        print('猜大了！')
    else:
        print('猜小了！！')
'''





#1.找出1到20之间的奇数，如果是3的倍数，则不输出，如果是7的倍数，则结束程序

'''
num = 1
while num <= 20:
    if num  % 3 == 0:
        num = num + 2
        continue
    if num % 7 == 0:
        break
    print(num)
    num = num + 2
'''


#练习2：使用while循环，提供多次机会给用户猜测。比如说，最多给用户三次机会

'''
result = 8
times = 0
while times < 3:
    number = int(input('输入一个数字:'))
    if number == result:
        print('猜对了，6666！')
        print('没有奖励！！！')
    else:
        if number > result:
            print('猜大了！！！')
        else:
            print('猜小了！！！')
    times = times + 1
'''


#练习3）求100以内的奇数之和   99+97+95+93+92+91......1

'''
num = 99
all_num = 0
while num > 0:
    all_num = all_num + num
    num -= 2
print('all_number的reslult:',all_num)
'''


#改进 求100以内的奇数之和    1+3+5+7+....+99


'''
str_number = 1
init_number = 0
while str_number < 100:
    init_number = init_number + str_number
    str_number += 2
print('最后的结果是：',init_number)

'''


#练习4）创建一个包含了100以内奇数的列表

'''
s = 1
a = []
while s < 100:
    a.append(s)
    s += 2
print(a)
'''


##练习5 逐一区分列表内的奇数和偶数 li = [11,22,3,24,66,77,89]

'''
l1=[]
l2=[]
li = [11,22,3,24,66,77,89]
s = 0
while  s < len(li):
    number = li.pop()
    if number % 2 == 0:
        l1.append(number)
    else:
        l2.append(number)
print(l1,l2)
'''

# for 循环

'''
结构
遍历序列
计数循环
序列索引
range函数
循环嵌套
编程练习
'''
#例1
'''
for i  in 'python':
    print('当前打印的是：',i)
'''

#例2
'''
for i in range(1,10):
    print(i,end='')
'''

#例3
'''
li = ['python','java','php','javascript','ruby']
for i in range(len(li)):
    print('当前打印的是：%s'%li[i] + '它的长度是：%s'%len(li[i]))
'''

#例4
'''
d = {'name':'fighter',
     'tel':1853600235,
     'age':30}
for k,v in d.items():
    print(k,'===>',v)
'''

#例5

'''
dic={
    "name":'zhangshan',
    "age":150,
    "gender":'man',
    "intrest":'basketball'}

print ('My name is {}'.format(dic['name']))
print ('My age is %s'%(dic['age']))
print ('My intrest is %s'%(dic['intrest']))
'''

#例6
'''
res = None
for i  in range(3):
    if i == 4:
        res = True
        print('找到了！')
        break
if not res:
    print('没找到！')
'''

#例8
'''
l1 = [11,22,'ee','apple','45']
l2 = ['www','apple',45,66,'32']
l3 = []
for index in l1:
    if index not in l2:
        l3.append(index)
    else:
        pass 
print(l3)
'''

#循环嵌套
'''
for  i  in  range(1,10):
    print ('----------------->',i)
    for  j  in range(1,i+1):
        print  ('++++++',j)
        if j == 5:
            break
'''


#练习题：
#练习1.使用for循环嵌套实现99乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) + '*' + str(j) + '=' + str(i*j) + '\t',end='')
    print()
'''

'''
课后练习(冒泡排序)：
	定义一个列表，如 lst = [3,8,2,12,56,9]，然后把列表中
	的数据由高到低排序，并输出。
'''

'''
lst = [3,8,2,12,56,9]
for i in range(0,len(lst)-1): #对比的轮次
    for j in range(0,len(lst)-1-i):  #每一轮对比的次数
        if lst[j] < lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)

'''

'''

a = [9,5,89,11,23,3]
times = len(a) - 1
print(times)
while times > 0:
    for i in range(times):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
    times = times -1
    print(a)
'''
