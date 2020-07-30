# https://github.com/arrow-py/arrow
"""
>>> import arrow
>>> arrow.get('2013-05-11T21:23:58.970460+07:00')
<Arrow [2013-05-11T21:23:58.970460+07:00]>

>>> utc = arrow.utcnow()
>>> utc
<Arrow [2013-05-11T21:23:58.970460+00:00]>

>>> utc = utc.shift(hours=-1)
>>> utc
<Arrow [2013-05-11T20:23:58.970460+00:00]>

>>> local = utc.to('US/Pacific')
>>> local
<Arrow [2013-05-11T13:23:58.970460-07:00]>

>>> local.timestamp
1368303838

>>> local.format()
'2013-05-11 13:23:58 -07:00'

>>> local.format('YYYY-MM-DD HH:mm:ss ZZ')
'2013-05-11 13:23:58 -07:00'

>>> local.humanize()
'an hour ago'

>>> local.humanize(locale='ko_kr')
'1시간 전'

>>> arrow.utcnow()
<Arrow [2013-05-07T04:20:39.369271+00:00]>

>>> arrow.now()
<Arrow [2013-05-06T21:20:40.841085-07:00]>

>>> arrow.now('US/Pacific')
<Arrow [2013-05-06T21:20:44.761511-07:00]>

>>> arrow.get(1367900664)
<Arrow [2013-05-07T04:24:24+00:00]>

>>> arrow.get(1367900664.152325)
<Arrow [2013-05-07T04:24:24.152325+00:00]>

>>> arrow.get(datetime.utcnow())
<Arrow [2013-05-07T04:24:24.152325+00:00]>

>>> arrow.get(datetime(2013, 5, 5), 'US/Pacific')
<Arrow [2013-05-05T00:00:00-07:00]>

>>> from dateutil import tz
>>> arrow.get(datetime(2013, 5, 5), tz.gettz('US/Pacific'))
<Arrow [2013-05-05T00:00:00-07:00]>

>>> arrow.get(datetime.now(tz.gettz('US/Pacific')))
<Arrow [2013-05-06T21:24:49.552236-07:00]>

>>> arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss')
<Arrow [2013-05-05T12:30:45+00:00]>

>>> arrow.get('June was born in May 1980', 'MMMM YYYY')
<Arrow [1980-05-01T00:00:00+00:00]>

>>> arrow.get(2013, 5, 5)
<Arrow [2013-05-05T00:00:00+00:00]>

>>> past = arrow.utcnow().shift(hours=-1)
>>> past.humanize()
'an hour ago'

# 只需要时间间隔
>>> present = arrow.utcnow()
>>> future = present.shift(hours=2)
>>> future.humanize(present)
'in 2 hours'
>>> future.humanize(present, only_distance=True)
'2 hours'

# 不同的时间粒度
>>> present = arrow.utcnow()
>>> future = present.shift(minutes=66)
>>> future.humanize(present, granularity="minute")
'in 66 minutes'
>>> future.humanize(present, granularity=["hour", "minute"])
'in an hour and 6 minutes'
>>> present.humanize(future, granularity=["hour", "minute"])
'an hour and 6 minutes ago'
>>> future.humanize(present, only_distance=True, granularity=["hour", "minute"])
'an hour and 6 minutes'

>>> arrow.utcnow().span('hour')
(<Arrow [2013-05-07T05:00:00+00:00]>, <Arrow [2013-05-07T05:59:59.999999+00:00]>)

# 向下取整
>>> arrow.utcnow().floor('hour')
<Arrow [2013-05-07T05:00:00+00:00]>

# 向上取整
>>> arrow.utcnow().ceil('hour')
<Arrow [2013-05-07T05:59:59.999999+00:00]>

# 时间范围序列
>>> start = datetime(2013, 5, 5, 12, 30)
>>> end = datetime(2013, 5, 5, 17, 15)
>>> for r in arrow.Arrow.span_range('hour', start, end):
...     print r
...
(<Arrow [2013-05-05T12:00:00+00:00]>, <Arrow [2013-05-05T12:59:59.999999+00:00]>)
(<Arrow [2013-05-05T13:00:00+00:00]>, <Arrow [2013-05-05T13:59:59.999999+00:00]>)
(<Arrow [2013-05-05T14:00:00+00:00]>, <Arrow [2013-05-05T14:59:59.999999+00:00]>)
(<Arrow [2013-05-05T15:00:00+00:00]>, <Arrow [2013-05-05T15:59:59.999999+00:00]>)
(<Arrow [2013-05-05T16:00:00+00:00]>, <Arrow [2013-05-05T16:59:59.999999+00:00]>)
"""