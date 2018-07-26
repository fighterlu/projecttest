'''
函数实战：
    1.加法计算器
    2.过滤器
    4.登录功能实战
'''

def add(a,b):
    return a+b

def login_order():
    return 'asdfasdfdasfadsf'

def myOrder(session):
    '''查看我的订单记录'''
    if session == 'asdfasdfdasfadsf':
        print('login success')
        print('你可以查询你的订单记录了：具体信息。。。')
        return True
    else:
        print('login fail')
        return False
myOrder(login())

'''
需求：一个用户登陆系统成功后显示它登陆的账号
1.注册，就是把注册的账号写到了info记事本中
2.登录，从记事本info.txt中读取注册的用户名和密码
3.然后登录，登录成功后,打印出登录账号的信息
4.优化代码
'''

def register(username,password):
    '''
    注册用户
    :param username:注册的用户名
    :param password:注册账号的密码
    '''
    # username = input('请输入您的账号：\n')
    # password = input('请输入您的密码：\n')
    temp = username + '|'+ password
    #把注册的用户名和密码写到info.txt文件中
    with open('info.txt','w') as f:
        f.write(temp)
# register()

def login(username,password):
    '''
    用户登录系统
    :param username:登录的用户名
    :param passoword: 登录的密码
    :return: 登录成功 False:登录失败
    '''
    #读取记事本info.txt中的数据
    f=open('info.txt','r')
    # print(f.read(),type(f.read()))
    list1 = f.read().split('|')
    # print(list1,type(list1))
    # print('username:',list1[0])
    # print('password:',list1[1])
    # username = input('请输入登录的账号： \n')
    # password = input('请输入登录的密码： \n')
    if  username == list1[0] and password ==list1[1]:
        # print('login is success')
        return True
    else:
        # print('login is fail')
        return False


def getUserInfo():
    '''打印用户登录成功后的信息'''
    f=open('info.txt','r')
    list1 = f.read().split('|')
    print('恭喜{0},登录系统成功，请开始你的操作:'.format(list1[0]))
    # if login():
    #     print('恭喜{0},登录系统成功，请开始你的操作:'.format(list1[0]))
    # else:
    #     # print('login fail')
    #     return False

def exit():
    '''退出系统'''
    import sys
    sys.exit(1)

def getUsername():
    '''获取输入的用户名'''
    username = input('请输入您的账号：\n')
    return username

def getPassword():
    '''获取输入的密码'''
    password = input('请输入您的账号的密码：\n')
    return password

def system():
    '''程序执行的入口'''
    # username = input('请输入登录的账号： \n')
    # password = input('请输入登录的密码： \n')
    while True:         #3.获取用户信息
        t=int(input('1、注册   2、登录    3、退出系统\n'))
        if   t == 1:
            # username = input('请输入您的账号：\n')
            # password = input('请输入您的密码：\n')
            register(getUsername(),getPassword())
        elif t == 2:
            # username = input('请输入登录的账号： \n')
            # password = input('请输入登录的密码： \n')
            s=login(getUsername(),getPassword())
            if s:
                getUserInfo()
            else:
                print('很遗憾！请登录系统，谢谢~')
        # elif t == 3:
        #     getUserInfo()
        elif t == 3:
            exit()
        else:
            break

if __name__ == '__main__':
    system()

'''
1.代码优化：用户名和密码分离，放入主函数，login(username,password) 入参数
2.注册代码进行分离 
3.写一个方法对
'''







