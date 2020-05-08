# class calendar.Calendar(firstweekday=0)
# 创建一个 Calendar 对象。 firstweekday 是一个整数，用于指定一周的第一天。 0 是星期一（默认值），6 是星期天。
import calendar

# 全局设置
# calendar.setfirstweekday(calendar.SUNDAY)
import time

print(calendar.firstweekday())
print(calendar.isleap(2020)) # 如果 year 是闰年则返回 True ,否则返回 False

print(calendar.leapdays(1991,2020)) # 返回在范围 y1 至 y2 （包含 y1 和 y2 ）之间的闰年的年数，其中 y1 和 y2 是年份。此函数适用于跨越一个世纪变化的范围。

print(calendar.timegm((2020,5,8,11,21,55)))
print(calendar.timegm(time.gmtime()))
"""
calendar.weekday(year, month, day)
返回某年（ 1970 -- ...），某月（ 1 -- 12 ），某日（ 1 -- 31 ）是星期几（ 0 是星期一）。

calendar.weekheader(n)
返回一个包含星期几的缩写名的头。 n 指定星期几缩写的字符宽度。

calendar.monthrange(year, month)
返回指定 年份 的指定 月份 的第一天是星期几和这个月的天数。

calendar.monthcalendar(year, month)
返回表示一个月的日历的矩阵。每一行代表一周；此月份外的日子由零表示。除非由 setfirstweekday() 设置，否则每周以周一为始。

calendar.prmonth(theyear, themonth, w=0, l=0)
打印由 month() 返回的一个月的日历。

calendar.month(theyear, themonth, w=0, l=0)
使用 TextCalendar 类的 formatmonth() 以多行字符串形式返回月份日历。

calendar.prcal(year, w=0, l=0, c=6, m=3)
打印由 calendar() 返回的整年的日历。

calendar.calendar(year, w=2, l=1, c=6, m=3)
使用 TextCalendar 类的 formatyear() 返回整年的3列的日历以多行字符串的形式。

calendar.timegm(tuple)
一个不相关但很好用的函数，它接受一个时间元组例如 time 模块中的 gmtime() 函数的返回并返回相应的 Unix 时间戳值，假定 1970 年开始计数， POSIX 编码。实际上， time.gmtime() 和 timegm() 是彼此相反的。
"""
for i in calendar.day_name:
    print(i)
for i in calendar.day_abbr:
    print(i)
for i in calendar.month_name:
    print(i)
for i in calendar.month_abbr:
    print(i)
print("------------------")
# class calendar.Calendar
c = calendar.Calendar(0)
for i in c.iterweekdays():
    print(i)
# c = calendar.Calendar(6)  是不一样的结果
for i in c.itermonthdates(2020, 5):
    print(i)

# 返回的日期为当月每一天的日期对应的天数。对于不在当月的日期，显示为 0。
for i in c.itermonthdays(2020, 5):
    print(i)

# 迭代器中的元素为一个由日期和代表星期几的数字组成的的元组。
for i in c.itermonthdays2(2020, 5):
    print(i)

# 迭代器的元素为一个由年，月，日组成的元组。
for i in c.itermonthdays3(2020, 5):
    print(i)

# 迭代器的元素为一个由年，月，日和代表星期几的数字组成的元组。
for i in c.itermonthdays4(2020, 5):
    print(i)

# 返回一个表示指定年月的周列表。周列表由七个 datetime.date 对象组成。
for i in c.monthdatescalendar(2020, 5):
    print(i)
# c = calendar.Calendar(6)  是不一样的结果
for i in calendar.Calendar(6).monthdatescalendar(2020, 5):
    print(i)

# c = calendar.Calendar(6)  是不一样的结果
for i in c.monthdays2calendar(2020, 5):
    print(i)
# c = calendar.Calendar(6)  是不一样的结果
for i in c.monthdayscalendar(2020, 5):
    print(i)
# 返回可以用来格式化的指定年月的数据。返回的值是一个列表，列表是月份组成的行。每一行包含了最多 width 个月(默认为3)。每个月包含了4到6周，每周包含1--7天。每一天使用 datetime.date 对象。
for i in c.yeardatescalendar(2020):
    print(i)
# 返回可以用来模式化的指定年月的数据(与 yeardatescalendar() 类似)。周列表的元素是由表示日期的数字和表示星期几的数字组成的元组。不在这个月的日子为0。
for i in c.yeardays2calendar(2020):
    print(i)
# 返回可以用来模式化的指定年月的数据(与 yeardatescalendar() 类似)。周列表的元素是表示日期的数字。不在这个月的日子为0。
for i in c.yeardayscalendar(2020):
    print(i)

# class calendar.TextCalendar(firstweekday=0)
t = calendar.TextCalendar()
print(t.formatmonth(2020, 5))
print(calendar.TextCalendar(6).formatmonth(2020, 5))
# 与 formatmonth() 方法一样，打印一个月的日历。
t.prmonth(2020, 5)

print(t.formatyear(2020))
# 与 formatyear() 方法一样，打印一整年的日历。
t.pryear(2020)

# class calendar.HTMLCalendar(firstweekday=0)

h = calendar.HTMLCalendar()
print(h.formatmonth(2020, 5))
print(h.formatyear(2020))
print(h.formatyearpage(2020))


# 自定义样式;
class CustomHTMLCal(calendar.HTMLCalendar):
    cssclasses = [style + " text-nowrap" for style in
                  calendar.HTMLCalendar.cssclasses]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"


ch = CustomHTMLCal()

print(ch.formatmonth(2020, 5))
# class calendar.LocaleTextCalendar(firstweekday=0, locale=None)
# class calendar.LocaleHTMLCalendar(firstweekday=0, locale=None)
# 这两个类的 formatweekday() 和 formatmonthname() 方法临时更改dang当前区域至给定 locale 。由于当前的区域设置是进程范围的设置，因此它们不是线程安全的。



