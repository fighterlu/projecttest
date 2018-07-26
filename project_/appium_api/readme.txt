ADB常用命令详解
    ADB是一个 客户端-服务器端 程序, 其中客户端是你用来操作的电脑, 服务器端是android设备.

# 问题：Ui Automator识别APP元素时报错 Error obtaining UI hierarchy
# 解决办法：adb root

1. 查看设备
adb devices    这个命令是查看当前连接的设备, 连接到计算机的android设备或者模拟器将会列出显示

2.关闭adb
adb kill-server

3.开启adb
adb start-server
adb reboot


4. 安装软件
adb install   这个命令将指定的apk文件安装到设备上
adb install   路径\app-weichi-release.apk

当有多个设备接入ADB客户端，就要指定设备名称
adb -s 设备名 install 包名
adb -s emulator-5556 install 路径\helloWorld.apk
如果显示success，那么久安装apk包成功，显示Failure，则安装失败。检查错误，排错，再执行如下命令：abd install -r 包名.apk


5、获取app的包名和activity名称
adb logcat | findstr START
脚本中，cmp= 后面的值就是 包名/activity名称

其他方式：
aapt dump badging E:\apk\xxxx.apk
adb logcat | findstr START


6. 卸载软件
adb uninstall <软件名>
adb uninstall -k <软件名>
如果加 -k 参数,为卸载软件但是保留配置和缓存文件.


#*************************APP启动时间的监控*********************#

7、监控APP启动时间
语法：adb shell am start -W packagename/activity
例子：adb shell am start -W com.android.calculator2/.Calculator

TotalTime的值，就是APP启动所消耗的时间.


8、关闭app
语法：adb shell am force-stop 包名
例子：adb shell am force-stop com.android.calculator2


9、把app从前台调入后台
语法：adb shell input keyevent 3

ps：app的启动，分为冷启动和热启动
冷启动：app彻底停止运行后再启动
热启动：app进入后台后再启动


10. 从电脑上发送文件到设备(输入命令adb remount ,意思是将设备改为可读可写)

adb push <本地路径> <远程路径>
用push命令可以把本机电脑上的文件或者文件夹复制到设备(手机)

如:adb push recovery.img /sdcard/recovery.img,将本地目录中的recovery.img文件传送手机的SD卡中并取同样的文件名.
adb push C:\recovery.img /sdcard/


11. 从设备上下载文件到电脑
adb pull <远程路径> <本地路径>
如：adb pull /data/local/tmp/blacklist.txt D:test.txt   将/data/local/tmp/blacklist.txt拉取到 本地D:text.txt 命名为text.txt
用pull命令可以把设备(手机)上的文件或者文件夹复制到本机电脑


12. 登录设备shell
adb shell
进入之后就可以执行shell命令了，比如cd ,pwd,ls等。