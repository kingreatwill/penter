from pyspark.sql import Row, SparkSession, Window

spark = SparkSession.builder \
    .master("local") \
    .appName("SQL-OTHER") \
    .getOrCreate()
print("-----class pyspark.sql.GroupedData(jgd, df)---class pyspark.sql.PandasCogroupedOps(gd1, gd2)-------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.GroupedData
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.PandasCogroupedOps

import pandas as pd
from pyspark.sql.functions import pandas_udf

df1 = spark.createDataFrame(
    [(20000101, 1, 1.0), (20000101, 2, 2.0), (20000102, 1, 3.0), (20000102, 2, 4.0)],
    ("time", "id", "v1"))
df2 = spark.createDataFrame(
    [(20000101, 1, "x"), (20000101, 2, "y")],
    ("time", "id", "v2"))


def asof_join(l, r):
    return pd.merge_asof(l, r, on="time", by="id")


df1.groupby("id").cogroup(df2.groupby("id")).applyInPandas(
    asof_join, schema="time int, id int, v1 double, v2 string"
).show()

# +--------+---+---+---+
# |    time| id| v1| v2|
# +--------+---+---+---+
# |20000101|  1|1.0|  x|
# |20000102|  1|3.0|  x|
# |20000101|  2|2.0|  y|
# |20000102|  2|4.0|  y|
# +--------+---+---+---+


print("-----重点-----class pyspark.sql.Column(jc)--------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.Column
"""
# 1. Select a column out of a DataFrame

df.colName
df["colName"]

# 2. Create from an expression
df.colName + 1
1 / df.colName
"""

df = spark.createDataFrame([('Tom', 80), ('Alice', None)], ["name", "height"])
df.select(df.name).orderBy(df.name.asc()).collect()
# [Row(name='Alice'), Row(name='Tom')]

# df = spark.createDataFrame([Row(r=Row(a=1, b="b"))])
# df.select(df.r.getField("b")).show()
# +---+
# |r.b|
# +---+
# |  b|
# +---+
# df.select(df.r.a).show()
# +---+
# |r.a|
# +---+
# |  1|
# +---+


print("-----重点-----class pyspark.sql.Row--------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.Row
"""
row = Row(name="Alice", age=11)
Person = Row("name", "age")
Person("Alice", 11)
"""

print("-----重点-----class pyspark.sql.Window--------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.Window
from pyspark.sql import functions as func

tup = [(1, "a"), (1, "a"), (2, "a"), (1, "b"), (2, "b"), (3, "b")]
df = spark.createDataFrame(tup, ["id", "category"])
# Window.unboundedPreceding 无界 开始第一行, Window.unboundedFollowing 无界结束最后一行, and Window.currentRow 当前
window = Window.partitionBy("category").orderBy("id").rangeBetween(Window.currentRow, 1)

df.withColumn("sum", func.sum("id").over(window)).sort("id", "category").show()

# +---+--------+---+
# | id|category|sum|
# +---+--------+---+
# |  1|       a|  4|
# |  1|       a|  4|
# |  1|       b|  3|
# |  2|       a|  2|
# |  2|       b|  5|
# |  3|       b|  3|
# +---+--------+---+

# >>> df.withColumn("sum", func.sum("id").over(window)).show()
# +---+--------+---+
# | id|category|sum|
# +---+--------+---+
# |  1|       b|  3|
# |  2|       b|  5|
# |  3|       b|  3|
# |  1|       a|  4|
# |  1|       a|  4|
# |  2|       a|  2|
# +---+--------+---+
# https://stackoverflow.com/questions/59571231/how-spark-rangebetween-works-with-descending-order
# https://www.csdn.net/gather_29/MtTaYg4sNzExMC1ibG9n.html
df \
    .withColumn("sum", func.sum("id").over(window)) \
    .withColumn("list", func.collect_list("id").over(window)) \
    .show()
# +---+--------+---+---------+
# | id|category|sum|     list|
# +---+--------+---+---------+
# |  1|       b|  3|   [1, 2]|
# |  2|       b|  5|   [2, 3]|
# |  3|       b|  3|      [3]|
# |  1|       a|  4|[1, 1, 2]|   #   1+0 <= value <=1+1   如果是desc  则 是+变-
# |  1|       a|  4|[1, 1, 2]|  #   1+0 <= value <=1+1
# |  2|       a|  2|      [2]|  #   2+0 <= value <=2+1
# +---+--------+---+---------+


window2 = Window.partitionBy("category").orderBy("id").rowsBetween(Window.currentRow, 1)
df.withColumn("sum", func.sum("id").over(window2)).sort("id", "category", "sum").show()
# +---+--------+---+
# | id|category|sum|
# +---+--------+---+
# |  1|       a|  2|
# |  1|       a|  3|
# |  1|       b|  3|
# |  2|       a|  2|
# |  2|       b|  5|
# |  3|       b|  3|
# +---+--------+---+

# df.withColumn("sum", func.sum("id").over(window2)).show()# 这个可以理解
# +---+--------+---+
# | id|category|sum|
# +---+--------+---+
# |  1|       b|  3|
# |  2|       b|  5|
# |  3|       b|  3|
# |  1|       a|  2|
# |  1|       a|  3|
# |  2|       a|  2|
# +---+--------+---+


"""
1、over函数的写法：

　　over（partition by class order by sroce） 按照sroce排序进行累计，order by是个默认的开窗函数，按照class分区。

2、开窗的窗口范围：

　　over（order by sroce range between 5 preceding and 5 following）：窗口范围为当前行数据幅度减5加5后的范围内的。

　　over（order by sroce rows between 5 preceding and 5 following）：窗口范围为当前行前后各移动5行。
"""

# days = lambda i: i * 86400
# .rangeBetween(-days(7), 0)
# .rowsBetween(-sys.maxsize, 0)
'''
spark.sql(
    """SELECT *, mean(some_value) OVER (
        PARTITION BY id 
        ORDER BY CAST(start AS timestamp) 
        RANGE BETWEEN INTERVAL 7 DAYS PRECEDING AND CURRENT ROW
     ) AS mean FROM df""").show()
'''

from pyspark.sql.functions import current_timestamp

spark.range(3).withColumn('date', current_timestamp()).show()

print("--------Window里面的方法其实就是创建WindowSpec----class pyspark.sql.WindowSpec(jspec)-------------")
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.WindowSpec

print("-------------重点--pyspark.sql.functions module------------------")

import pyspark.sql.functions

print([element for element in dir(pyspark.sql.functions) if not element.startswith("_")])
# 224 个方法和类（8个类 216个方法）
"""
['Column', 'DataFrame', 'DataType', 'PandasUDFType', 'PythonEvalType', 'SparkContext', 'StringType', 'UserDefinedFunction',
 
 'abs', 'acos', 'add_months', 'approxCountDistinct', 'approx_count_distinct', 'array', 'array_contains', 'array_distinct', 'array_except', 'array_intersect', 
 'array_join', 'array_max', 'array_min', 'array_position', 'array_remove', 'array_repeat', 'array_sort', 'array_union', 'arrays_overlap', 'arrays_zip', 
 'asc', 'asc_nulls_first', 'asc_nulls_last', 'ascii', 'asin', 'atan', 'atan2', 'avg', 
 'base64', 'basestring', 'bin', 'bitwiseNOT', 'blacklist', 'broadcast', 'bround',
  'cbrt', 'ceil', 'coalesce', 'col', 'collect_list', 'collect_set', 'column', 'concat', 
  'concat_ws', 'conv', 'corr', 'cos', 'cosh', 'count', 'countDistinct', 'covar_pop', 'covar_samp', 'crc32',
   'create_map', 'cume_dist', 'current_date', 'current_timestamp',
'date_add', 'date_format', 'date_sub', 'date_trunc', 'datediff', 'dayofmonth', 'dayofweek', 'dayofyear', 
'decode', 'degrees', 'dense_rank', 'desc', 'desc_nulls_first', 'desc_nulls_last', 
'element_at', 'encode', 'exp', 'explode', 'explode_outer', 'expm1', 'expr',
 'factorial', 'first', 'flatten', 'floor', 
 'format_number', 'format_string', 'from_csv', 'from_json', 'from_unixtime', 'from_utc_timestamp', 
 'functools', 'get_json_object', 'greatest', 'grouping', 'grouping_id', 'hash', 'hex', 'hour', 'hypot', 
 'ignore_unicode_prefix', 'initcap', 'input_file_name', 'instr', 'isnan', 'isnull', 'json_tuple', 'kurtosis',
  'lag', 'last', 'last_day', 'lead', 'least', 'length', 'levenshtein', 'lit', 'locate',
'log', 'log10', 'log1p', 'log2', 'lower', 'lpad', 'ltrim',
 'map_concat', 'map_entries', 'map_from_arrays', 'map_from_entries', 'map_keys', 'map_values',
'max', 'md5', 'mean', 'min', 'minute', 'monotonically_increasing_id', 'month', 'months_between', 
'nanvl', 'next_day', 'ntile', 'overlay', 'pandas_udf', 'percent_rank', 'posexplode', 'posexplode_outer', 
'pow', 'quarter', 'radians', 'rand', 'randn', 'rank', 'regexp_extract', 'regexp_replace', 
'repeat', 'reverse', 'rint', 'round', 'row_number', 'rpad', 'rtrim', 'schema_of_csv', 'schema_of_json', 
'second', 'sequence', 'sha1', 'sha2', 'shiftLeft', 'shiftRight', 'shiftRightUnsigned', 'shuffle', 'signum', 'sin', 'since', 'sinh',
 'size', 'skewness', 'slice', 'sort_array', 'soundex', 'spark_partition_id', 'split', 'sqrt', 'stddev', 'stddev_pop', 'stddev_samp',
  'struct', 'substring', 'substring_index', 'sum', 'sumDistinct', 'sys', 'tan', 'tanh',
   'toDegrees', 'toRadians', 'to_csv', 'to_date', 'to_json', 'to_str', 'to_timestamp', 'to_utc_timestamp', 'translate', 
   'trim', 'trunc', 'udf', 'unbase64', 'unhex', 'unix_timestamp', 'upper', 'var_pop', 'var_samp', 'variance', 'warnings', 
   'weekofyear', 'when', 'window', 'xxhash64', 'year']
"""
from pyspark.sql.functions import window,sum

df = spark.createDataFrame([("2016-03-11 09:00:07", 1)]).toDF("date", "val")
w = df.groupBy(window("date", "5 seconds")).agg(sum("val").alias("sum"))
w.select(w.window.start.cast("string").alias("start"), w.window.end.cast("string").alias("end"), "sum").collect()

# [Row(start='2016-03-11 09:00:05', end='2016-03-11 09:00:10', sum=1)]
