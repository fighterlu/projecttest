#coding=utf-8

#.keyevent( )方法，只限于Android使用

from appium import webdriver
from time import sleep

desired_caps = {
        'platformName': 'Android',
        'platformVersion': '5.0.0.0',
        'deviceName': '127.0.0.1:62001',
        'appPackage': 'com.shanjian.originaldesign',
        'appActivity':'.activity.other.Activity_In'
        }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(10)
driver.find_element_by_id('com.shanjian.originaldesign:id/edit_Tel').clear()
driver.find_element_by_id('com.shanjian.originaldesign:id/edit_Tel').send_keys("15817252876")
driver.find_element_by_id("com.shanjian.originaldesign:id/edit_Pwd").click()
driver.keyevent(29)  #输入a
driver.keyevent(30)  #输入b

#通过keyevent()输入之前，先通过click()点击要输入的控件。而且它每次只能输入一个字符

'''
下面提供keycode 参考表：
电话键
KEYCODE_CALL 拨号键5
KEYCODE_ENDCALL 挂机键6
KEYCODE_HOME 按键Home 3
KEYCODE_MENU 菜单键82
KEYCODE_BACK 返回键4
KEYCODE_SEARCH 搜索键84
KEYCODE_CAMERA 拍照键27
KEYCODE_FOCUS 拍照对焦键80
KEYCODE_POWER 电源键26
KEYCODE_NOTIFICATION 通知键83
KEYCODE_MUTE 话筒静音键91
KEYCODE_VOLUME_MUTE 扬声器静音键164
KEYCODE_VOLUME_UP 音量增加键24
KEYCODE_VOLUME_DOWN 音量减小键25

控制键
KEYCODE_ENTER 回车键66
KEYCODE_ESCAPE ESC 键111
KEYCODE_DPAD_CENTER 导航键确定键23
KEYCODE_DPAD_UP 导航键向上19
KEYCODE_DPAD_DOWN 导航键向下20
KEYCODE_DPAD_LEFT 导航键向左21
KEYCODE_DPAD_RIGHT 导航键向右22
KEYCODE_MOVE_HOME 光标移动到开始键122
KEYCODE_MOVE_END 光标移动到末尾键123
KEYCODE_PAGE_UP 向上翻页键92
KEYCODE_PAGE_DOWN 向下翻页键93
KEYCODE_DEL 退格键67
KEYCODE_FORWARD_DEL 删除键112
KEYCODE_INSERT 插入键124
KEYCODE_TAB Tab 键61
KEYCODE_NUM_LOCK 小键盘锁143
KEYCODE_CAPS_LOCK 大写锁定键115
KEYCODE_BREAK Break/Pause 键121
KEYCODE_SCROLL_LOCK 滚动锁定键116
KEYCODE_ZOOM_IN 放大键168
KEYCODE_ZOOM_OUT 缩小键169

组合键
KEYCODE_ALT_LEFT Alt+Left
KEYCODE_ALT_RIGHT Alt+Right
KEYCODE_CTRL_LEFT Control+Left
KEYCODE_CTRL_RIGHT Control+Right
KEYCODE_SHIFT_LEFT Shift+Left
KEYCODE_SHIFT_RIGHT Shift+Right

基本
KEYCODE_0 按键'0' 7
KEYCODE_1 按键'1' 8
KEYCODE_2 按键'2' 9
KEYCODE_3 按键'3' 10
KEYCODE_4 按键'4' 11
KEYCODE_5 按键'5' 12
KEYCODE_6 按键'6' 13
KEYCODE_7 按键'7' 14
KEYCODE_8 按键'8' 15
KEYCODE_9 按键'9' 16
KEYCODE_A 按键'A' 29
KEYCODE_B 按键'B' 30
KEYCODE_C 按键'C' 31
KEYCODE_D 按键'D' 32
KEYCODE_E 按键'E' 33
KEYCODE_F 按键'F' 34
KEYCODE_G 按键'G' 35
KEYCODE_H 按键'H' 36
KEYCODE_I 按键'I' 37
KEYCODE_J 按键'J' 38
KEYCODE_K 按键'K' 39
KEYCODE_L 按键'L' 40
KEYCODE_M 按键'M' 41
KEYCODE_N 按键'N' 42
KEYCODE_O 按键'O' 43
KEYCODE_P 按键'P' 44
KEYCODE_Q 按键'Q' 45
KEYCODE_R 按键'R' 46
KEYCODE_S 按键'S' 47
KEYCODE_T 按键'T' 48
KEYCODE_U 按键'U' 49
KEYCODE_V 按键'V' 50
KEYCODE_W 按键'W' 51
KEYCODE_X 按键'X' 52
KEYCODE_Y 按键'Y' 53
KEYCODE_Z 按键'Z' 54

'''