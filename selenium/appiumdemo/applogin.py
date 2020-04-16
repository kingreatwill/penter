# Android environment
import unittest
from appium import webdriver

desired_caps = {
    "version": "",
    "deviceName": "Android01",
    "platform": "ANDROID",
    "appActivity": ".HomeScreenActivity",
    "appPackage": "io.selendroid.testapp",
}

"""
Desired Capabilities在启动session的时候是必须提供的。

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.ANDROID

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = 'E:/Tests/Appium/selendroid-test-app-0.11.0.apk'
"browserName": "chrome"


automationName：使用哪种自动化引擎。appium（默认）还是Selendroid？
platformName：使用哪种移动平台。iOS, Android, orFirefoxOS？
app： 应用的绝对路径，注意一定是绝对路径。如果指定了appPackage和appActivity的话，这个属性是可以不设置的。另外这个属性和browserName属性是冲突的。
browserName：移动浏览器的名称。比如Safari' for iOS and 'Chrome', 'Chromium', or 'Browser' for Android；与app属性互斥。

udid：物理机的id。比如1ae203187fc012g。
deviceName：启动哪种设备，是真机还是模拟器？iPhone Simulator, iPad Simulator, iPhone Retina 4-inch, Android Emulator, Galaxy S4, etc...
下面这些属性是android平台特定的：
'appPackage':启动android时，app的package是什么？（uiautomatorviewer.bat可以看到）
待测试的app的java package。比如com.example.android.myApp, com.android.settings。

'appActivity':启动android时，app的activity是什么？
待测试的app的Activity名字。比如MainActivity, .Settings。注意，原生app的话要在activity前加个"."。

如何获取android app的Activity
adb dumpsys  activity activities | grep mFocusedActivity # 8.0以下
adb shell dumpsys activity activities | grep mResumedActivity # 8.0
如果不行
1. adb devices 查看设备列表
2. -s 设备
adb -s emulator-5554 shell dumpsys activity activities | findstr mResumedActivity
adb -s emulator-5554 shell dumpsys activity activities | grep mResumedActivity
如果实际上只有一个设备或模拟器，并且查到有offline的状态；
那就说明是ADB本身的BUG所导致的，就需要用如下的方法处理下了：
adb kill-server
taskkill /f /im adb.exe
第一条命令是杀ADB的服务，第二条命令是杀ADB的进程！
如果第一条没有用，才考虑用第二条命令再试试看的！



desired_caps = {
'platformName': 'Android',
'deviceName': '127.0.0.1:62001',
'platformVersion': '4.4.2',
'appPackage': 'iflytek.testTech.propertytool',
'appActivity': '.activity.HomeActivity',
'unicodeKeyboard': "True",    #使用unicode输入法
'resetKeyboard': "True",       #重置输入法到初始状态
'noReset': "True"               #启动app时不要清除app里的原有的数据
}
"""

# driver.installApp("D:\\android\\apk\\ContactManager.apk");
# removeApp() 从设备中删除一个应用
# closeApp()
# launchApp() 启动应用
# isAppInstalled() 检查应用是否安装
# runAppInBackground() 将应用置于后台 这个方法需要入参，需要指定应用置于后台的时长。driver.runAppInBackground(2);
# resetApp() 应用重置
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# http://127.0.0.1:4723/wd/hub  http://192.168.110.216:9999/wd/hub

driver = webdriver.Remote(command_executor='http://192.168.110.216:9999/wd/hub',
                          desired_capabilities=desired_caps)

if driver.is_app_installed("io.selendroid.testapp"):
    print("installed")
    # 升级 driver.install_app('E:/Tests/Appium/selendroid-test-app-0.11.0.apk')
    # driver.launch_app()
else:
    print("not installed")
    driver.install_app('E:/Tests/Appium/selendroid-test-app-0.11.0.apk')

el = driver.find_element_by_id('io.selendroid.testapp:id/my_text_field')
el.send_keys("123")
