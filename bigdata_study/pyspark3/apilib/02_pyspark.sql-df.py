# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame
from pyspark.sql import SparkSession

# df.stat           # return  DataFrameStatFunctions  http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameStatFunctions
# df.na             # return  DataFrameNaFunctions  http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameNaFunctions

# df.write          # return DataFrameWriter        http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameWriter
# df.writeStream    # return DataStreamWriter       http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.streaming.DataStreamWriter

spark = SparkSession.builder \
    .master("local") \
    .appName("SQL-DF") \
    .getOrCreate()
"""
# To create DataFrame using SparkSession
people = spark.read.parquet("...")
department = spark.read.parquet("...")

people.filter(people.age > 30).join(department, people.deptId == department.id) \
  .groupBy(department.name, "gender").agg({"salary": "avg", "age": "max"})
"""

df = spark.createDataFrame([{"name": "A", "age": 18}, {"name": "B", "age": 28}, {"name": "C", "age": 38}])
# >>> df.collect()
# [Row(age=18, name='A'), Row(age=28, name='B'), Row(age=38, name='C')]
# >>> df.agg({"age": "max"}).collect()
# [Row(max(age)=38)]

from pyspark.sql.functions import *

# >>> df.agg(min(df.age)).collect()
# [Row(min(age)=18)]


df_as1 = df.alias("df_as1")
df_as2 = df.alias("df_as2")
joined_df = df_as1.join(df_as2, col("df_as1.name") == col("df_as2.name"), 'inner')
joined_df.select("df_as1.name", "df_as2.name", "df_as2.age").sort(desc("df_as1.name")).collect()
# [Row(name='C', name='C', age=38), Row(name='B', name='B', age=28), Row(name='A', name='A', age=18)]


# 分位数
df.approxQuantile("age", [0.25, 0.75], 0.05)
# [18.0, 38.0]

# `DataFrame` with the default storage level (`MEMORY_AND_DISK`).
df.cache()

# spark.sparkContext.setCheckpointDir()
# df.checkpoint()

# >>> df.rdd.getNumPartitions()
# 4
# >>> df.coalesce(10).rdd.getNumPartitions()
# 4
# >>> df.coalesce(1).rdd.getNumPartitions()


df = spark.createDataFrame([("a", 1), ("b", 2), ("c", 3)], ["Col1", "Col2"])
df.select(df.colRegex("`(Col1)?+.+`")).show()  # 不以Col1开头 ，标准写法： (?!Col1).+  （go不支持(?!xx) 不以xx开头 (?=xx) 以xx开头    ）
# 匹配Col2列

df = spark.createDataFrame([(1, 1), (2, 2), (3, 3)], ["c1", "c2"])
df.corr("c1", "c2")  # 当前仅支持Pearson相关系数。两列必须为数字
# 1.0

# 计算给定列（由其名称指定）的样本协方差，作为双精度值。
df.cov("c1", "c2")
# 1.0


df.createGlobalTempView("people")  # createOrReplaceGlobalTempView(name)
df2 = spark.sql("select * from global_temp.people")
# 全局表需要加上global_temp

# createTempView createOrReplaceTempView
# df.createOrReplaceTempView("people")

print("--------crossJoin------")
df = spark.createDataFrame([{"name": "A", "age": 18}, {"name": "B", "age": 28}, {"name": "C", "age": 38}])
df2 = spark.createDataFrame([{"name": "D", "height": 170}, {"name": "C", "height": 85}])
df.select("age", "name").collect()
# [Row(age=18, name='A'), Row(age=28, name='B'), Row(age=38, name='C')]
df2.select("name", "height").collect()
# [Row(name='D', height=170), Row(name='C', height=85)]
df.crossJoin(df2.select("height")).select("age", "name", "height").collect()
# [Row(age=18, name='A', height=170), Row(age=18, name='A', height=85), Row(age=28, name='B', height=170),
#  Row(age=28, name='B', height=85), Row(age=38, name='C', height=170), Row(age=38, name='C', height=85)]


print("--------join------")

"""
df.join(df2, 'name', 'outer').select('name', 'height').sort(desc("name")).collect()
[Row(name='Tom', height=80), Row(name='Bob', height=85), Row(name='Alice', height=None)]

cond = [df.name == df3.name, df.age == df3.age]
df.join(df3, cond, 'outer').select(df.name, df3.age).collect()
[Row(name='Alice', age=2), Row(name='Bob', age=5)]

df.join(df2, 'name').select(df.name, df2.height).collect()
[Row(name='Bob', height=85)]

df.join(df4, ['name', 'age']).select(df.name, df.age).collect()
[Row(name='Bob', age=5)]
"""

print("--------union--unionAll-----unionByName------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame.union

# >>> df1 = spark.createDataFrame([[1, 2, 3]], ["col0", "col1", "col2"])
# >>> df2 = spark.createDataFrame([[4, 5, 6]], ["col1", "col2", "col0"])
# >>> df1.unionByName(df2).show()
# +----+----+----+
# |col0|col1|col2|
# +----+----+----+
# |   1|   2|   3|
# |   6|   4|   5|
# +----+----+----+
#
# >>> df1.union(df2).show()
# +----+----+----+
# |col0|col1|col2|
# +----+----+----+
# |   1|   2|   3|
# |   4|   5|   6|
# +----+----+----+
#
# >>> df1.unionAll(df2).show()
# +----+----+----+
# |col0|col1|col2|
# +----+----+----+
# |   1|   2|   3|
# |   4|   5|   6|
# +----+----+----+


# >>> df.crosstab("name","age").collect()
# [Row(name_age='A', 18=1, 28=0, 38=0), Row(name_age='C', 18=0, 28=0, 38=1), Row(name_age='B', 18=0, 28=1, 38=0)]

# >>> df.cube("name", df.age).count().orderBy("name", "age").show()
# +----+----+-----+
# |name| age|count|
# +----+----+-----+
# |null|null|    3|
# |null|  18|    1|
# |null|  28|    1|
# |null|  38|    1|
# |   A|null|    1|
# |   A|  18|    1|
# |   B|null|    1|
# |   B|  28|    1|
# |   C|null|    1|
# |   C|  38|    1|
# +----+----+-----+
#
# >>> df.describe(['age']).show()
# >>> df.summary("count", "min", "25%", "75%", "max").show()
# >>> df.select("age", "name").summary("count").show()

# >>> df.describe().show()
# +-------+------------------+-----------------+
# |summary|                id|              age|
# +-------+------------------+-----------------+
# |  count|                 2|                2|
# |   mean|               1.5|             25.5|
# | stddev|0.7071067811865476|6.363961030678928|
# |    min|                 1|               21|
# |    max|                 2|               30|
# +-------+------------------+-----------------+
#
# >>> df.summary().show()
# +-------+------------------+-----------------+
# |summary|                id|              age|
# +-------+------------------+-----------------+
# |  count|                 2|                2|
# |   mean|               1.5|             25.5|
# | stddev|0.7071067811865476|6.363961030678928|
# |    min|                 1|               21|
# |    25%|                 1|               21|
# |    50%|                 1|               21|
# |    75%|                 2|               30|
# |    max|                 2|               30|
# +-------+------------------+-----------------+

# drop  dropDuplicates

# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame.drop


print("-------exceptAll---(a-b)--")
df1 = spark.createDataFrame(
    [("a", 1), ("a", 1), ("a", 1), ("a", 2), ("b", 3), ("c", 4)], ["C1", "C2"])
df2 = spark.createDataFrame([("a", 1), ("b", 3)], ["C1", "C2"])
df1.exceptAll(df2).show()
# +---+---+
# | C1| C2|
# +---+---+
# |  a|  1|
# |  a|  1|
# |  a|  2|
# |  c|  4|
# +---+---+

# 填充
df.cube("name", df.age).count().orderBy("name", "age").na.fill({'age': 50, 'name': 'unknown'}).show()
# 替换
# df4.na.replace('Alice', None).show()


# hint提示，当使用不当时会有提示，可以根据提示优化
# >>> df.join(df2.hint("broadcast"), "name").show()
# +----+---+------+
# |name|age|height|
# +----+---+------+
# |   C| 38|    85|
# +----+---+------+
#
# >>> df.join(df2, "name").show()
# +----+---+------+
# |name|age|height|
# +----+---+------+
# |   C| 38|    85|
# +----+---+------+

# subtract 差集
# intersect 交集
df3 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3), ("c", 4)], ["C1", "C2"])
df4 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3)], ["C1", "C2"])
df3.intersect(df4).sort("C1", "C2").show()
# +---+---+
# | C1| C2|
# +---+---+
# |  a|  1|
# |  b|  3|
# +---+---+
df3.intersectAll(df4).sort("C1", "C2").show()
# +---+---+
# | C1| C2|
# +---+---+
# |  a|  1|
# |  a|  1|
# |  b|  3|
# +---+---+


from pyspark.sql.functions import pandas_udf

df = spark.createDataFrame([(1, 21), (2, 30)], ("id", "age"))


def filter_func(iterator):
    for pdf in iterator:
        yield pdf[pdf.id == 1]


df.mapInPandas(filter_func, df.schema).show()
# +---+---+
# | id|age|
# +---+---+
# |  1| 21|
# +---+---+


# 返回具有新指定列名的新DataFrame
df.toDF('f1', 'f2').collect()
# df.toJSON() # return rdd

# list(df.toLocalIterator())
# df.toPandas()

from pyspark.sql.functions import col

df = spark.createDataFrame([(1, 1.0), (2, 2.0)], ["int", "float"])


def cast_all_to_int(input_df):
    return input_df.select([col(col_name).cast("int") for col_name in input_df.columns])


def sort_columns_asc(input_df):
    return input_df.select(*sorted(input_df.columns))


df.transform(cast_all_to_int).transform(sort_columns_asc).show()

# df.withColumn('age2', df.age + 2).collect()
# [Row(age=2, name='Alice', age2=4), Row(age=5, name='Bob', age2=7)]

# df.withColumnRenamed('age', 'age2').collect()
# [Row(age2=2, name='Alice'), Row(age2=5, name='Bob')]

print("---------重点---withWatermark------------------")
# 定义此数据格式的事件时间水印。水印跟踪一个时间点，在此时间点之前，我们假定不会再有延迟数据到达。


# withWatermark(eventTime, delayThreshold)  eventTime:包含行事件时间的列的名称。 delayThreshold: e.g. “1 minute” or “5 hours”
# sdf.select('name', sdf.time.cast('timestamp')).withWatermark('time', '10 minutes')

print("------------------class pyspark.sql.DataFrameNaFunctions(df)-----------------------------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameNaFunctions

# 用于处理DataFrame中缺少的数据的功能。
# df.na
# drop,fill,replace 三个方法

print("----------------重点--class pyspark.sql.DataFrameWriter(df)--------------------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameWriter
"""
使用registerTempTable注册表是一个临时表，生命周期只在所定义的sqlContext或hiveContext实例之中。
换而言之，在一个sqlontext（或hiveContext）中registerTempTable的表不能在另一个sqlContext（或hiveContext）中使用。

而saveAsTable则是永久的，只要连接存在，spark再启的时候，这个表还是在的。saveAsTable会利用hive API将Dataset持久化为表,saveAsTable()的默认策略是如果表存在就会报错

使用spark做增量操作的时候,会看到有2个方法都可以做:
insertInto 和 mode(SaveMode.Append).saveAsTable()

"""
# df.write.format('parquet').partitionBy('year', 'month').bucketBy(100, 'year', 'month').saveAsTable('xxx')


print("----------------------------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.streaming.DataStreamWriter

# # Print every row using a function
# def print_row(row):
#     print(row)
#
# writer = sdf.writeStream.foreach(print_row)
# # Print every row using a object with process() method
# class RowPrinter:
#     def open(self, partition_id, epoch_id):
#         print("Opened %d, %d" % (partition_id, epoch_id))
#         return True
#     def process(self, row):
#         print(row)
#     def close(self, error):
#         print("Closed with error: %s" % str(error))
#
# writer = sdf.writeStream.foreach(RowPrinter())

# # trigger the query for execution every 5 seconds
# writer = sdf.writeStream.trigger(processingTime='5 seconds')
# # trigger the query for just once batch of data
# writer = sdf.writeStream.trigger(once=True)
# # trigger the query for execution every 5 seconds
# writer = sdf.writeStream.trigger(continuous='5 seconds')
"""
https://cloud.tencent.com/developer/article/1032539
一，Structured Streaming的Triggers

在Structured Streaming中，Trigger用来指定Streaming 查询产生结果的频率。一旦Trigger触发，Spark将会检查是否有新数据可用。
如果有新数据，查询将增量的从上次触发的地方执行。如果没有新数据，Stream继续睡眠，直到下次Trigger触发。

Structured Streaming的默认行为尽可能低延迟地运行，trigger会在上次trigger触发结束之后立即运行。
针对一些有低延迟要求的使用案例，Structured Streaming支持ProcessingTime trigger，也即将会用用户提供的时间间隔，例如每分钟，去触发一次查询。

这虽然很好，但是也免不了24*7运行。相反，RunOnce Trigger仅仅会执行一次查询，然后停止查询。

Trigger在你启动Streams的时候指定。


"""

"""
https://zhenchao125.github.io/bigdata_spark-project_atguigu/di-7-bu-fen-structured-streaming/di-7-zhangtrigger-hong-fa-566829.html

流式查询的触发器定义了流式数据处理的时间, 流式查询根据触发器的不同, 可以是根据固定的批处理间隔进行微批处理查询, 也可以是连续的查询.

Trigger Type	                                    Description
unspecified (default)	                            没有显示的设定触发器, 表示使用 micro-batch mode, 尽可能块的处理每个批次的数据. 如果无数据可用, 则处于阻塞状态, 等待数据流入
Fixed interval micro-batches 
固定周期的微批处理	                                    查询会在微批处理模式下执行, 其中微批处理将以用户指定的间隔执行. 
                                                        1. 如果以前的微批处理在间隔内完成, 则引擎会等待间隔结束, 然后开启下一个微批次 
                                                        2. 如果前一个微批处理在一个间隔内没有完成(即错过了间隔边界), 则下个微批处理会在上一个完成之后立即启动(不会等待下一个间隔边界) 
                                                        3. 如果没有新数据可用, 则不会启动微批次. 适用于流式数据的批处理作业
One-time micro-batch 
一次性微批次	                                        查询将在所有可用数据上执行一次微批次处理, 然后自行停止. 
                                                    如果你希望定期启动集群, 然后处理集群关闭期间产生的数据, 然后再关闭集群. 
                                                    这种情况下很有用. 它可以显著的降低成本. 一般用于非实时的数据分析

Continuous with fixed checkpointinterval 
(experimental 2.3 引入) 连续处理	                    以超低延迟处理数据



// 1. 默认触发器
val query: StreamingQuery = df.writeStream
    .outputMode("append")
    .format("console")
    .start()
// 2. 微批处理模式
val query: StreamingQuery = df.writeStream
        .outputMode("append")
        .format("console")
        .trigger(Trigger.ProcessingTime("2 seconds"))
        .start

// 3. 只处理一次. 处理完毕之后会自动退出
val query: StreamingQuery = df.writeStream
        .outputMode("append")
        .format("console")
        .trigger(Trigger.Once())
        .start()

// 4. 持续处理
val query: StreamingQuery = df.writeStream
    .outputMode("append")
    .format("console")
    .trigger(Trigger.Continuous("1 seconds"))
    .start
"""

