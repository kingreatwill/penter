# Android environment
import unittest
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from matplotlib.backend_bases import KeyEvent

desired_caps = {
    #"version": "",
    "deviceName": "d00c5441",
    #"platform": "ANDROID",
    "platformName": "Android",
    "platformVersion": "9",
    #"automationName": "Flutter",
    #"app":"F:/github/openjw/penter/selenium/appiumdemo/selendroid-test-app-0.11.0.apk",
    "appActivity": ".MainActivity",
    "appPackage": "com.lingcb.saas",  # "io.flutter.demo.gallery",
    # 'unicodeKeyboard': True,  # 是使用unicode编码方式发送字符串
    # 'resetKeyboard': True  # 隐藏键盘
}
# desired_caps = {
#     "version": "",
#     "deviceName": "emulator-5554",
#     "platform": "ANDROID",
#     "platformName": "Android",
#     # "platformVersion": '9',
#     "appActivity": ".HomeScreenActivity",
#     "appPackage": "io.selendroid.testapp",  # "io.flutter.demo.gallery",
#     # 'unicodeKeyboard': True,  # 是使用unicode编码方式发送字符串
#     # 'resetKeyboard': True  # 隐藏键盘
# }
# https://github.com/appium/python-client
"""
http://www.testclass.net/appium/appium-base-summary/
Desired Capabilities在启动session的时候是必须提供的。

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.ANDROID

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = 'F:/github/openjw/penter/selenium/appiumdemo/selendroid-test-app-0.11.0.apk'
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

 "appActivity": ".HomeScreenActivity",
    "appPackage": "io.selendroid.testapp",
     driver.install_app('E:/Tests/Appium/selendroid-test-app-0.11.0.apk')

el = driver.find_element_by_id('io.selendroid.testapp:id/my_text_field')
el.send_keys("123")
"""

# driver.installApp("D:\\android\\apk\\ContactManager.apk");
# removeApp() 从设备中删除一个应用
# closeApp()
# launchApp() 启动应用
# isAppInstalled() 检查应用是否安装
# runAppInBackground() 将应用置于后台 这个方法需要入参，需要指定应用置于后台的时长。driver.runAppInBackground(2);
# resetApp() 应用重置
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# http://127.0.0.1:4723/wd/hub  http://192.168.110.216:9999/wd/hub

# driver = webdriver.Remote(command_executor='http://192.168.110.216:9999/wd/hub',  desired_capabilities=desired_caps)
# settings = driver.get_settings()
# driver.update_settings({"some setting": "the value"})

# driver.start_activity('com.foo.app', '.MyActivity')
# driver.start_activity('com.foo.app', '.MainActivity', app_wait_package='your package name')

# if driver.is_app_installed("io.flutter.demo.gallery"):
#     print("installed")
#     # 升级 driver.install_app('E:/Tests/Appium/selendroid-test-app-0.11.0.apk')
#     # driver.launch_app()
# else:
#     print("not installed")
#     driver.install_app('E:/Tests/Appium/flutter_gallery_android.apk')
"""
# 打开 uiautomatorviewer
# resource-id 使用 driver.find_element_by_id('io.selendroid.testapp:id/my_text_field')
# from selenium.webdriver.common.by import By
# or driver.findElement(By.ID,"com.android.calculator2:id/formula")



# text 使用 driver.find_element_by_name("name") ??? 不行！
# el = driver.find_element(By.NAME, "CUPERTINO")
# el = driver.find_elements_by_android_uiautomator('new UiSelector().text("CUPERTINO")')[0] 可以！
# driver.find_element_by_xpath("//android.view.View[contains(@text,'CUPERTINO')]") 可以！
els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')


# UiSelector
driver.findElementByAndroidUIAutomator("new UiSelector().text(\"clr\")").click();
driver.findElementByAndroidUIAutomator("new UiSelector().text(\"8\")").click();
driver.findElementByAndroidUIAutomator("new UiSelector().description(\"plus\")").click(); // content-desc
driver.findElementByAndroidUIAutomator("new UiSelector().text(\"5\")").click();
driver.findElementByAndroidUIAutomator("new UiSelector().description(\"equals\")").click();
需要注意的是 description() 方法用的是content-desc属性。


# content-desc 对应driver.find_element_by_accessibility_id('Animation')




# xpath 用class的属性来替代做标签的名字。
# findElementByXpath("//android.widget.TextView[contains(@text,'Add note')]")
使用方法：

driver.findElement(By.xpath("//android.view.ViewGroup/android.widget.Button"))  //7
当果如果出现class 相同的情况下可以用控件的属性值进行区分。 
java driver.findElement(By.xpath("//android.widget.Button[contains(@text,'7')]")).click(); //7 
driver.findElement(By.xpath("//android.widget.Button[contains(@content-desc,'times')]")).click(); //* 
driver.findElement(By.xpath("//android.widget.Button[contains(@text,'7')]")).click(); //7 
driver.findElement(By.xpath("//android.widget.Button[contains(@content-desc,'equals')]")).click(); //= 
XPath 在 Appium 上的用法依然很强大，有时需要写更臭更长的定位语法，因为APP上元素的class命令本来就长，再加上多层级，结果可想而知。


"""

from time import sleep
from selenium.webdriver.common.by import By

sleep(5)
# el = driver.find_elements_by_android_uiautomator('new UiSelector().text("CUPERTINO")')[0]
# el = driver.find_element_by_name("CUPERTINO") NO
el = driver.find_element_by_xpath("//android.widget.ImageView[contains(@text,'请输入公司编码')]").send_keys("Appium")
#el = driver.find_element_by_xpath('//android.widget.EditText[@content-desc="my_text_fieldCD"]')

# pip install Appium-Flutter-Finder
# from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
#
# el = FlutterElement(driver, FlutterFinder().by_text('请输入公司编码'))
#el.click()
#el.send_keys("Appium")
# el.get_attribute('text')

# https://stackoverflow.com/questions/60601889/error-getting-on-appium-cannot-set-the-element-to-value-did-you-interact-wit
# driver.find_element_by_android_uiautomator('new UiSelector().text("请输入公司编码")').click()
# driver.press_keycode(AndroidKey.A)
"""
按键
driver.press_keycode(4)          #发送keycode，功能：按键 # 该方法Android特有

KEYCODE_CALL 拨号键 5 
KEYCODE_ENDCALL 挂机键 6 
KEYCODE_HOME 按键Home 3 
KEYCODE_MENU 菜单键 82 
KEYCODE_BACK 返回键 4 
KEYCODE_SEARCH 搜索键 84 
KEYCODE_CAMERA 拍照键 27 
KEYCODE_FOCUS 拍照对焦键 80 
KEYCODE_POWER 电源键 26 
KEYCODE_NOTIFICATION 通知键 83 
KEYCODE_MUTE 话筒静音键 91 
KEYCODE_VOLUME_MUTE 扬声器静音键 164 
KEYCODE_VOLUME_UP 音量增加键 24 
KEYCODE_VOLUME_DOWN 音量减小键 25
Tips：后面的数字为  keycode
Android模拟事件keycode对照表 https://blog.csdn.net/fengjinghuanian/article/details/90710877

driver.keyevent(4)               #发送keycode，功能：按键，与press_keycode无区别
driver.hide_keyboard()           #iOS使用key_name隐藏，安卓不使用参数，功能：隐藏键盘
driver.long_press_keycode(4)     #发送keycode，功能：长按键
driver.lock(100) # 熄屏  设置熄屏一段时间 不带参数，所以熄屏之后就不会再点亮屏幕了

driver.current_activity # 得到当前应用的activity。只适用于Android
driver.hide_keyboard() # 收起键盘，这个方法很有用，当我们对一个输入框输入完成后，需要将键盘收起，再切换到一下输入框进行输入
driver.swipe(75, 500, 75, 0, 800) # 模拟用户滑动。将控件或元素从一个位置（x,y）拖动到另一个位置（x,y）。
driver.pull_file() # 从设备中拉出文件。
Java String content = "some data for the file"; byte[] data = Base64.encodeBase64(content.getBytes()); 
driver.pushFile("sdcard/test.txt", data); # 推送文件到设备中去。


sleep(5)
# home按键
driver.press_keycode(3)

from appium.webdriver.extensions.android.nativekey import AndroidKey
driver.press_keycode(AndroidKey.HOME)
"""

from appium.webdriver.common.touch_action import TouchAction
# action = TouchAction(driver)
# action.tap(元素) or
# action.press(x=110,y=200).move_to(x=3,y=10).release().perform()


# 多指操作
from appium.webdriver.common.multi_action import MultiAction

# smile = TouchAction()
# smile.press(x=110,y=200).move_to(x=3,y=10).release()
# ma = MultiAction(driver)
# ma.add(e1, e2, smile)
# ma.perform()
# or
# smile1 = TouchAction()
# smile2 = TouchAction()
# smile1.press(e1).move_to(x=3,y=10).release()
# ma = MultiAction(driver)
# ma.add(smile1, smile2)
# ma.perform()

sleep(5)
