from pyspark.sql import SparkSession,Row

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Data Source") \
    .getOrCreate()


df = spark.read.load("resources/users.parquet")
df.select("name", "favorite_color").show()
#df.select("name", "favorite_color").write.save("namesAndFavColors.parquet")

# df = spark.read.load("resources/people.json", format="json")
# df.select("name", "age").write.save("namesAndAges.parquet", format="parquet")

df = spark.read.load("resources/people.csv",
                     format="csv", sep=";", inferSchema="true", header="true")

df.show()


df = spark.read.orc("resources/users.orc")
# (df.write.format("orc")
#     .option("orc.bloom.filter.columns", "favorite_color")
#     .option("orc.dictionary.key.threshold", "1.0")
#     .option("orc.column.encoding.direct", "name")
#     .save("users_with_options.orc"))
df.show()

df = spark.sql("SELECT * FROM parquet.`resources/users.parquet`")
df.show()
# df.write.mode("ignore").format("json").save("users.json")
# df1 = spark.read.json("users.json")
# df1.show()



# 忽略损坏文件（包含不符合格式的文件）
spark.sql("set spark.sql.files.ignoreCorruptFiles=true")
# dir1/file3.json is corrupt from parquet's view
test_corrupt_df = spark.read.parquet("resources/dir1/",
                                     "resources/dir1/dir2/")
test_corrupt_df.show()
"""
Spark允许您在从文件读取数据时使用spark.sql.files.ignoreMissingFiles忽略丢失的文件。 
在这里，丢失文件实际上意味着在构造DataFrame之后目录下的已删除文件。 设置为true时，遇到丢失的文件时，Spark作业将继续运行，并且已读取的内容仍将返回。
"""

df = spark.read.load("resources/dir1",
                     format="parquet", pathGlobFilter="*.parquet")
df.show()

# 递归查找文件
recursive_loaded_df = spark.read.format("parquet")\
    .option("recursiveFileLookup", "true")\
    .load("resources/dir1")
recursive_loaded_df.show()

# from pyspark.sql import Row
#
# # spark is from the previous example.
# # Create a simple DataFrame, stored into a partition directory
# sc = spark.sparkContext
#
# squaresDF = spark.createDataFrame(sc.parallelize(range(1, 6))
#                                   .map(lambda i: Row(single=i, double=i ** 2)))
# squaresDF.write.parquet("data/test_table/key=1")
#
# # Create another DataFrame in a new partition directory,
# # adding a new column and dropping an existing column
# cubesDF = spark.createDataFrame(sc.parallelize(range(6, 11))
#                                 .map(lambda i: Row(single=i, triple=i ** 3)))
# cubesDF.write.parquet("data/test_table/key=2")
#
# # Read the partitioned table
# spark.read.option("mergeSchema", "true").parquet("data/test_table").show()
# spark.read.parquet("data/test_table").show()



# --driver-class-path postgresql-9.4.1207.jar --jars postgresql-9.4.1207.jar
# --jars E:\elastic\canal\canal.admin-1.1.4.tar\canal.admin-1.1.4\lib\mysql-connector-java-5.1.40.jar
# properties = { 'user' : 'x', 'password' : 'x',"driver" :"com.mysql.jdbc.Driver" }
# tb = spark.read.jdbc("jdbc:mysql://192.168.1.x:3306/x",table="x",properties=properties)
# tb.show()

# spark.read.format("binaryFile").option("pathGlobFilter", "*.png").load("/path/to/data")

