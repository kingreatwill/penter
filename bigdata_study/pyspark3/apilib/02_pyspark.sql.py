"""
http://spark.apache.org/docs/latest/api/python/pyspark.sql.html
核心组件

pyspark.sql.SparkSession
Main entry point for DataFrame and SQL functionality.

pyspark.sql.DataFrame
A distributed collection of data grouped into named columns.


重要：
pyspark.sql.SparkSession                Main entry point for DataFrame and SQL functionality.
pyspark.sql.DataFrame                   A distributed collection of data grouped into named columns.
pyspark.sql.Column                      A column expression in a DataFrame.
pyspark.sql.Row                         A row of data in a DataFrame.
pyspark.sql.GroupedData                 Aggregation methods, returned by DataFrame.groupBy().
pyspark.sql.DataFrameNaFunctions        Methods for handling missing data (null values).
pyspark.sql.DataFrameStatFunctions      Methods for statistics functionality.
pyspark.sql.functions                   List of built-in functions available for DataFrame.
pyspark.sql.types                       List of data types available.
pyspark.sql.Window                      For working with window functions.
"""
import pandas as pd
from pyspark.sql import SparkSession


print("-------重点----class pyspark.sql.SparkSession(sparkContext, jsparkSession=None)----------")
spark = SparkSession.builder \
    .master("local") \
    .appName("Word Count") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

print("-------属性----------")

# 基础属性
print(spark.version)

# spark.catalog #return Catalog  http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.Catalog
# spark.conf #return RuntimeConfig  上一章学的
# spark.sparkContext # return SparkContext 上一章学的
# spark.udf # return UDFRegistration http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.UDFRegistration

# spark.read.text() # return DataFrameReader http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameReader
# spark.readStream.text() # return DataStreamReader http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.streaming.DataStreamReader

# spark.streams # return StreamingQueryManager http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.streaming.StreamingQueryManager


print("------------createDataFrame(data, schema=None, samplingRatio=None, verifySchema=True)---------")

l = [('Alice', 1)]
print(spark.createDataFrame(l).collect())
# [Row(_1='Alice', _2=1)]
print(spark.createDataFrame(l, ['name', 'age']).collect())
# [Row(name='Alice', age=1)]
d = [{'name': 'Alice', 'age': 1}]
print(spark.createDataFrame(d).collect())
# [Row(age=1, name='Alice')]
rdd = spark.sparkContext.parallelize(l)
print(spark.createDataFrame(rdd).collect())
# [Row(_1='Alice', _2=1)]
df = spark.createDataFrame(rdd, ['name', 'age'])
print(df.collect())
# [Row(name='Alice', age=1)]

from pyspark.sql import Row

Person = Row('name', 'age')
person = rdd.map(lambda r: Person(*r))
df2 = spark.createDataFrame(person)
print(df2.collect())
# [Row(name='Alice', age=1)]


from pyspark.sql.types import *

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)])
df3 = spark.createDataFrame(rdd, schema)
print(df3.collect())
# [Row(name='Alice', age=1)]

spark.createDataFrame(df.toPandas()).collect()
# [Row(name='Alice', age=1)]
spark.createDataFrame(pd.DataFrame([[1, 2]])).collect()
# [Row(0=1, 1=2)]

spark.createDataFrame(rdd, "a: string, b: int").collect()
# [Row(a='Alice', b=1)]
rdd = rdd.map(lambda row: row[1])
spark.createDataFrame(rdd, "int").collect()
# [Row(value=1)]

# SparkSession.getActiveSession()
#
# s = spark.newSession()


print("--sql----")
# df.createOrReplaceTempView("table1")
# df2 = spark.sql("SELECT name AS f1, age as f2 from table1") # SELECT * FROM table1
# df2.collect()


df.createOrReplaceTempView("table1")
df2 = spark.table("table1")
# sorted(df.collect()) == sorted(df2.collect())
# True

print("-------class pyspark.sql.SQLContext(sparkContext, sparkSession=None, jsqlContext=None)-----------")
# spark.sparkContext 操作rdd
# SQLContext  操作 dataframe
# 不推荐直接创建，在Spark 2.0中，这被SparkSession取代。但是，我们保留这个类是为了向后兼容
print("----------class pyspark.sql.HiveContext(sparkContext, jhiveContext=None)----------")
# 不推荐直接创建，使用 SparkSession.builder.enableHiveSupport().getOrCreate()
# 从类路径上的hime -site.xml读取Hive的配置
# HiveContext是SQLContext的子类

print("-----------class pyspark.sql.UDFRegistration(sparkSession)----------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.UDFRegistration

print("     -----------register(name, f, returnType=None)-------")
# 1. When f is a Python function: returnType 默认是字符串 可以指定, IntegerType()
strlen = spark.udf.register("stringLengthString", lambda x: len(x))
print(spark.sql("SELECT stringLengthString('test')").collect())
# [Row(stringLengthString(test)='4')]

spark.sql("SELECT 'foo' AS text").select(strlen("text")).collect()
# [Row(stringLengthString(text)='3')]

# 2. When f is a user-defined function:  udf函数 ，则register不用指定returnType
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import udf
slen = udf(lambda s: len(s), IntegerType())
_ = spark.udf.register("slen", slen)
spark.sql("SELECT slen('test')").collect()
# [Row(slen(test)=4)]

import random
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
random_udf = udf(lambda: random.randint(0, 100), IntegerType()).asNondeterministic()
new_random_udf = spark.udf.register("random_udf", random_udf)
spark.sql("SELECT random_udf()").collect()
# [Row(random_udf()=82)]

import pandas as pd
from pyspark.sql.functions import pandas_udf
@pandas_udf("integer")
def add_one(s: pd.Series) -> pd.Series:
    return s + 1

_ = spark.udf.register("add_one", add_one)
spark.sql("SELECT add_one(id) FROM range(3)").collect()
# [Row(add_one(id)=1), Row(add_one(id)=2), Row(add_one(id)=3)]


@pandas_udf("integer")
def sum_udf(v: pd.Series) -> int:
    return v.sum()

_ = spark.udf.register("sum_udf", sum_udf)
q = "SELECT sum_udf(v1) FROM VALUES (3, 0), (2, 0), (1, 1) tbl(v1, v2) GROUP BY v2"
spark.sql(q).collect()
# [Row(sum_udf(v1)=1), Row(sum_udf(v1)=5)]
print("     ---------registerJavaFunction(name, javaClassName, returnType=None)----------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.UDFRegistration.registerJavaFunction

print("     --------registerJavaUDAF(name, javaClassName)---注册聚合函数（python聚合服务用的pandas）-------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.UDFRegistration.registerJavaUDAF

print("----------------class pyspark.sql.Catalog(sparkSession)---------------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.Catalog
"""
spark.createDataFrame([(1, 1)]).createGlobalTempView("my_table")
spark.table("global_temp.my_table").collect()
[Row(_1=1, _2=1)]
spark.catalog.dropGlobalTempView("my_table")
spark.table("global_temp.my_table") 
Traceback (most recent call last):
    ...
AnalysisException: ...
"""

print("----------重点----class pyspark.sql.DataFrameReader(spark)--------------------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameReader

# df = spark.read.csv('python/test_support/sql/ages.csv')
#   or
# rdd = sc.textFile('python/test_support/sql/ages.csv')
# df2 = spark.read.csv(rdd)
#   or
# df3 = spark.read.format('csv').load('python/test_support/sql/ages.csv')
#   or
# df3 = spark.read.load('python/test_support/sql/ages.csv','csv')

# spark.read.csv()
# spark.read.json()
# spark.read.jdbc()
# spark.read.orc()
# spark.read.parquet()
# spark.read.text()
# spark.read.table()
# df = spark.read.parquet('python/test_support/sql/parquet_partitioned')
# df.createOrReplaceTempView('tmpTable')
# spark.read.table('tmpTable')

# DataFrameWriter 见 df.write


print("-------------class pyspark.sql.streaming.DataStreamReader(spark)------------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.streaming.DataStreamReader




print("----------class pyspark.sql.streaming.StreamingQuery(jsq)----class pyspark.sql.streaming.StreamingQueryManager(jsqm)--------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.streaming.StreamingQuery
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.streaming.StreamingQueryManager
# sq = df.writeStream.format("xx").start()
# sq.awaitTermination()
#
# sqm = spark.streams
# sqm.awaitAnyTermination()
# [q.name for q in sqm.active]

print("----------pyspark.sql.types module---------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.types
from pyspark.sql.types import *
# DataType() # 基类
# NullType()
# StringType()
# BinaryType()
# BooleanType()
# DateType()
# TimestampType()
# DecimalType()
# DoubleType()
# FloatType()
# ByteType()
# IntegerType()
# LongType()
# ShortType()
# ArrayType()
# MapType()
# StructField()
# StructType()

# >>> struct1 = StructType([StructField("f1", StringType(), True)])
# >>> struct1["f1"]
# # StructField(f1,StringType,true)
# >>> struct1[0]
# # StructField(f1,StringType,true)

# >>> struct1 = StructType().add("f1", StringType(), True).add("f2", StringType(), True, None)
# >>> struct2 = StructType([StructField("f1", StringType(), True), StructField("f2", StringType(), True, None)])
# >>> struct1 == struct2
# # True
# >>> struct1 = StructType().add(StructField("f1", StringType(), True))
# >>> struct2 = StructType([StructField("f1", StringType(), True)])
# >>> struct1 == struct2
# # True
# >>> struct1 = StructType().add("f1", "string", True)
# >>> struct2 = StructType([StructField("f1", StringType(), True)])
# >>> struct1 == struct2
# # True