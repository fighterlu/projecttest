#coding=utf-8


'''
airen登陆页面对象设计
'''
from  appiumframework.PO import base_page
import time



class Airen_Login_Page(base_page.Action):

    add_button_my=("com.juyang.mall:id/rb_Mine")         #点击我的
    clear_content=("com.juyang.mall:id/edit_Tel")        #清空
    input_username=("com.juyang.mall:id/edit_Tel")       #输入账户
    input_password=("com.juyang.mall:id/edit_Pwd")       #输入密码
    click_login_button=("com.juyang.mall:id/tv_Login")   #点击登陆按钮
    login_result_page_text=(u"商城")                      #验证返回商城首页

    def click_my_button(self):
        '''封装点击我的方法'''
        self.by_id(self.add_button_my).click()
        time.sleep(5)

    def clear_login_content(self):
        '''封装情空方法'''
        self.by_id(self.clear_content).clear()

    def input_text_username(self,username):
        '''封装输入用户名方法'''
        self.by_id(self.input_username).send_keys(username)
        time.sleep(3)

    def input_text_password(self,password):
        '''封装输入密码方法'''
        self.by_id(self.input_password).send_keys(password)

    def click_loginbtn(self):
        '''封装点击登陆方法'''
        self.by_id(self.click_login_button).click()
        time.sleep(8)

    def get_finish_button_text(self):
        '''登陆成功后获取首页商城信息'''
        return self.by_name(self.login_result_page_text).text


    def login_airen_appproject(self,user,passwd):
        '''登陆流程封装'''
        self.click_my_button()
        self.clear_login_content()
        self.input_text_username(user)
        self.input_text_password(passwd)
        self.click_loginbtn()





# def add_button_link(self):
     #     self.find_element(self.add_button_loc).click()
     #     time.sleep(3)           #等待3秒，等待登录弹窗加载完成
     #
     #
     # def run_case(self,value):
     #     self.find_element(self.edittext_loc).send_keys(value)
     #     time.sleep(5)
     #     self.find_element(self.finish_button_loc).click()
     #     time.sleep(2)
     #
     #
     # def get_finish_button_text(self):
     #     return self.find_element(self.edittext_loc).text
     #

# driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps) #链接app
# sleep(4)
# driver.find_element(By.ID,'com.juyang.mall:id/rb_Mine').click()  #点击我的
# sleep(4)
# driver.find_element(By.ID,'com.juyang.mall:id/edit_Tel').clear()
# driver.find_element(By.ID,'com.juyang.mall:id/edit_Tel').send_keys("18665100958")
# driver.find_element(By.ID,'com.juyang.mall:id/edit_Pwd').send_keys("123456")
# driver.find_element(By.ID,"com.juyang.mall:id/tv_Login").click()
# sleep(8)