import datetime
import locale

print(locale.getdefaultlocale())
# loc = locale.getlocale()  # get current locale
# print(loc)
# locale.setlocale(locale.LC_ALL, 'de_DE')
# locale.strcoll('f\xe4n', 'foo')  # compare a string containing an umlaut
# locale.setlocale(locale.LC_ALL, '')   # use user's preferred locale
# locale.setlocale(locale.LC_ALL, 'C')  # use default (C) locale
# locale.setlocale(locale.LC_ALL, loc)  # restore saved locale



alllocale = locale.locale_alias
for k in alllocale.keys():
    print('locale[%s] %s' % (k, alllocale[k]))


import time

print(time.strptime('Thu, 24 Nov 2016 07:01:59 GMT', '%a, %d %b %Y %H:%M:%S GMT'))

locale.setlocale(locale.LC_TIME)
print(time.strptime('Thu, 24 Nov 2016 07:01:59 GMT', '%a, %d %b %Y %H:%M:%S GMT'))

locale.setlocale(locale.LC_TIME, 'en_US')
print(time.strptime('Thu, 24 Nov 2016 07:01:59 GMT', '%a, %d %b %Y %H:%M:%S GMT'))

# print(locale.getlocale())
# print(locale.setlocale(locale.LC_ALL, ''))
# print(locale.getlocale())
# print(time.strptime('Thu, 24 Nov 2016 07:01:59 GMT', '%a, %d %b %Y %H:%M:%S GMT'))
# # 出错  这里的 %a %b 等，所以在不对的 locale 环境下，格式化出现了错误。

dt = datetime.datetime(2015, 11, 15, 16, 30)
locale.setlocale(locale.LC_ALL, "en_GB.utf8")
print(dt.strftime("%A, %d. %B %Y %I:%M%p"))

locale.setlocale(locale.LC_ALL, "zh_cn.utf8")
print(dt.strftime("%A, %d. %B %Y %I:%M%p"))

locale.setlocale(locale.LC_ALL, "nb_NO.utf8")
print(dt.strftime("%A, %d. %B %Y %I:%M%p"))

