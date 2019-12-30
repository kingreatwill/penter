import datetime
import time
from datetime import date

now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(1964, 7, 31)
age = now - birthday
print(age)
print(age.days)


today = date.today()
print(today)

yesterday = today - datetime.timedelta(days=1)
print(yesterday)

last_month = today.month - 1 if today.month - 1 else 12
print(last_month)

time_stamp = time.time()
print(time_stamp)

print(datetime.datetime.fromtimestamp(time_stamp))

print( int(time.mktime(today.timetuple())))
today_str = today.strftime("%Y-%m-%d")
today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
# 补时差
today + datetime.timedelta(hours=8)



