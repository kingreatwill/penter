# 先进的SQLAlchemy查询
# 使用sqlalchemy.text()以一种与后端无关的方式指定查询参数

import numpy as np
import pandas as pd
import sqlalchemy as sa
from pandas.io import sql
import datetime
import io
from sqlalchemy.types import VARCHAR, Float, Integer, Date, Numeric,Boolean,DateTime

"""
import cStringIO
 
output = cStringIO.StringIO()
# ignore the index
df_a.to_csv(output, sep='\t',index = False, header = False)
output.getvalue()
# jump to start of stream
output.seek(0)
 
connection = engine.raw_connection() #engine 是 from sqlalchemy import create_engine
cursor = connection.cursor()
# null value become ''
cursor.copy_from(output,table_name,null='')
connection.commit()
cursor.close()

本来50万条数据，使用pd.to_sql方法，设置chunksize=2000，跑了5个小时。
而上面这个方法，插40万条数据，只需1分钟。
有人说这个是postgresql专有的 https://gist.github.com/catawbasam/3164289
未经测试
"""



engine = sa.create_engine('sqlite:///:memory:')

df = pd.DataFrame(np.random.randn(20, 3), columns=list('abc'))
df.to_sql('data_chunks', engine, index=False)

sql.execute('INSERT INTO data_chunks VALUES(?, ?, ?)', engine,
            params=[(1, 12.2, 2)])

print(pd.read_sql(sa.text('SELECT * FROM data_chunks where a=:a1'), engine, params={'a1': 1.0}))

"""
import sqlite3
con = sqlite3.connect(':memory:')

data.to_sql('data', con)
pd.read_sql_query("SELECT * FROM data", con)

"""



import time
import datetime
class dateprocess:
    # datetime 转 string
    def datetime2str(self,input_datetime):
        input_str = input_datetime.strftime('%Y-%m-%d %H:%M:%S')
        return input_str
    # string 转 datetime
    def str2datetime(self,input_str):
        input_dt = datetime.datetime.strptime(input_str,'%Y-%m-%d %H:%M:%S')
        return input_dt
    # string 转 timestamp
    def str2timestamp(self,input_str):
        timeArray  = time.strptime(input_str, "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(timeArray))
        return timestamp
    # timestamp 转 string
    def timestamp2str(self,input_str):
        input_dt = datetime.datetime.fromtimestamp(input_str)
        return input_dt
    # datetime 转 time_tuple
    def datetime2time_tuple(self,dt):
        input_dt = dt.timetuple()
        return input_dt
   # str 转 time_tuple
    def str2time_tuple(self,data_str):
        input_str = time.strptime(data_str,'%Y-%m-%d %H:%M:%S')
        return input_str
   # timestap 转 time_tuple
    def timestamp2time_tuple(self,data_timestamp):
        input_str = time.localtime(data_timestamp)
        return input_str
   # time_tuple 转 timestamp
    def time_tuple2timestamp(self,time_tuple):
        input_str = int(time.mktime(time_tuple))
        return input_str
    # 比如昨天同一时刻
    def days_difference(self,n):
        now_dt = datetime.datetime.now() - datetime.timedelta(days=n)
        return now_dt
    # 比如一个小时之前
    def hours_difference(self,n):
        now_dt = datetime.datetime.now() - datetime.timedelta(hours=n)
        return now_dt



data = dateprocess()
now = datetime.datetime.now()
data_str = data.datetime2str(now)
print('-----------data_str--------------')
print(data_str)


d ="""
Date,Col_1,Col_2,Col_3
2010-10-18,X,27.50,True
2010-10-19,Y,-12.50,False
2010-10-20,Z,5.73,True
"""

data = pd.read_csv(io.StringIO(d))
data.to_sql('data', engine, index=True, dtype={
    'Date': sa.DateTime,
    'Col_1': VARCHAR,
    'Col_2': Float,
    "Col_3": Boolean})

print(pd.read_sql_query('SELECT * FROM data', engine))

# 如果您有数据库的SQLAlchemy描述，则可以使用SQLAlchemy表达式表达条件
metadata = sa.MetaData()
data_table = sa.Table('data', metadata,
                      sa.Column('index', sa.Integer),
                      sa.Column('Date', sa.DateTime),
                      sa.Column('Col_1', sa.String),
                      sa.Column('Col_2', sa.Float),
                      sa.Column('Col_3', sa.Boolean),
                      )

print(pd.read_sql(sa.select([data_table]).where(data_table.c.Col_3 is True), engine))

expr = sa.select([data_table]).where(data_table.c.Date > sa.bindparam('date'))
print(pd.read_sql(expr, engine, params={'date': datetime.datetime(2010, 10, 18)}))
