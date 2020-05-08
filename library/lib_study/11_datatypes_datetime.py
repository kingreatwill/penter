import datetime

# date, datetime, time 和 timezone 类型共享这些通用特性: 1. 这些类型的对象都是不可变的。2. 这些类型的对象是可哈希的，这意味着它们可被作为字典的键。 3. 这些类型的对象支持通过 pickle 模块进行高效的封存。
print(datetime.MINYEAR)
print(datetime.MAXYEAR)

print(datetime.date(2020, 5, 7))
print(datetime.time(20, 5, 7, 123000))
print(datetime.datetime(2020, 5, 7, 20, 5, 7))

print(datetime.datetime.now())  # now有@classmethod修饰，所以不需要实例化
print(datetime.datetime.utcnow())

print(datetime.datetime(2020, 5, 7, 20, 5, 8) - datetime.datetime(2020, 5, 7, 20, 5, 7))

print(datetime.datetime.now().strftime("%A"))
print(datetime.datetime.strptime('2020-01-01 0:0:0', '%Y-%m-%d %H:%M:%S'))
# 使用 datetime.strptime(date_string, format) 等价于:
# datetime(*(time.strptime(date_string, format)[0:6]))

day20 = datetime.datetime.strptime('2021-01-01 0:0:0', '%Y-%m-%d %H:%M:%S')
nowdate = datetime.datetime.today()
dela = day20 - nowdate
day = dela.days
hour = int(dela.seconds / 60 / 60)
minute = int((dela.seconds - hour * 60 * 60) / 60)
second = dela.seconds - hour * 60 * 60 - minute * 60
print('到2021年元旦还有：' + str(day) + '天' + str(hour) + '小时' + str(minute) + '分' + str(second) + '秒')

print("----------")



from datetime import datetime
from datetime import timedelta

# 1) 获取当前日期和时间
today = datetime.today()  # 返回当前时间时分秒都为0
print("当前时间")
print(today)
today1 = datetime.now()  # 返回当前日期和时间
# now.hour # 时
# now.minute # 分
# now.isoweekday（）# 返回的1-7代表周一--周日；
# now.weekday（）# 返回的0-6代表周一--到周日
# 而标准格式种%w 1-6表示周一--周六，0代表周日
print(today1)
today2 = datetime.utcnow()  # 返回当前东八区时间就是比当时时间少8个小时
print(today2)

# 2) 获取指定日期和时间,加减计算
time = datetime(2019, 5, 12, 12, 13, 14)
d = time + timedelta(weeks=0, days=0, hours=0, minutes=0, seconds=0, milliseconds=0, microseconds=0, )
# 依次为 "周" "天", "时","分","秒","毫秒","微秒"
print(time)
print(d)

time1 = "2019-5-12 12:13:14"  # 字符串 日期
d1 = datetime.strptime(str(time1), '%Y-%m-%d %H:%M:%S')
plus = d1 + timedelta(days=1)  # 加
minus = d1 - timedelta(days=1)  # 减
print(time1)
print(d1)
print(plus)
print(minus)

time2 = 20190512121314
d2 = datetime.strptime(str(time2), '%Y%m%d%H%M%S')
delta = d2 + timedelta(days=1)
print(time2)
print(d2)
print(delta)

# 3) 日期datetime-timestamp 时间戳相互转
now_stamp = time.timestamp()
print('指定时间对应时间戳 :', now_stamp)

print('对应本地时间 :', datetime.fromtimestamp(now_stamp))
print('UTC标准时间 :', datetime.utcfromtimestamp(now_stamp))
print('本周的第几天:', datetime.fromtimestamp(now_stamp).weekday())

# 4) datetime 时间 转换为str字符串
now = datetime.now()
print('当前时间 :', now)
print(now.strftime('%Y%m%d%H%M%S'))

import pytz

print(datetime(2011, 11, 11, 0, 0, 0, tzinfo=pytz.utc))
print(datetime(2011, 11, 11, 0, 0, 0, tzinfo=pytz.timezone("Asia/Shanghai")))

from datetime import datetime, timedelta, timezone
print(datetime.utcnow())
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
cn_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(cn_dt)
jan_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(jan_dt)
cn_2_jan_dt = cn_dt.astimezone(timezone(timedelta(hours=9)))
print(cn_2_jan_dt)
