# 引入日历模块
import calendar
# 星期几（0-6）
#设置第一天是星期天(默认第一天是周一)
calendar.setfirstweekday(firstweekday=6)
# 显示日历
print(calendar.month(2020, 1))

# 第一个元素是所查月份的第一天对应的是星期几
# 第二个元素是这个月的天数
print(calendar.monthrange(2016,9))

# 若只是想知道每个月的天数，可用：
print(calendar.mdays)