import os

from pyspark.sql import SparkSession

# https://github.com/datastax/spark-cassandra-connector/blob/master/doc/15_python.md
# https://blog.tanka.la/2018/09/06/running-pyspark-with-cassandra-using-spark-cassandra-connector-in-jupyter-notebook/

# Configuratins related to Cassandra connector & Cluster http://maven.aliyun.com/nexus/content/groups/public/
os.environ['PYSPARK_SUBMIT_ARGS'] = '--repositories https://maven.aliyun.com/repository/central --packages com.datastax.spark:spark-cassandra-connector_2.12:3.0.0-beta --conf spark.cassandra.connection.host=127.0.0.1 pyspark-shell'

# Configuratins related to Cassandra connector & Cluster
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.3.0 --conf spark.cassandra.connection.host=192.168.0.123,192.168.0.124 pyspark-shell'

spark = SparkSession \
    .builder \
    .appName("SparkCassandra") \
    .getOrCreate()

# Loads and returns data frame for a table including key space given
def load_and_get_table_df(keys_space_name, table_name):
    table_df = spark.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table=table_name, keyspace=keys_space_name)\
        .load()
    return table_df

# sample_kvs = load_and_get_table_df("examples", "tbl_sample_kv")
sample_kvs = load_and_get_table_df("examples", "sample_times")
sample_kvs.show()
# ratings.groupBy("user_id").count().orderBy('count', ascending=False).show()
# ratings.printSchema()
# firstUserMovies = ratings.where(ratings["user_id"] == 45811).select("movie_id")

# load_options = { "table": "kv", "keyspace": "test", "spark.cassandra.input.split.size_in_mb": "10"}
# spark.read.format("org.apache.spark.sql.cassandra").options(**load_options).load().show()

# df.write \
#     .format("org.apache.spark.sql.cassandra") \
#     .mode('append') \
#     .options(table="kv", keyspace="test") \
#     .save()

"""
cassandra 不支持join 
那么使用spark join
session
    .read.cassandraFormat("cc_transactions", "cc")
    .load()
    .createOrReplaceTempView("spark_cc_transactions")
session
    .read.cassandraFormat("cc_customers", "cc")
    .load()
    .createOrReplaceTempView("spark_cc_customers")
    
    session.sql(
          '''
            |SELECT c.county as county, t.year as year, t.month as month, -SUM(t.amount) as total_amount
            |FROM spark_cc_customers c
            |INNER JOIN spark_cc_transactions as t ON c.id = t.customerid
            |WHERE t.status = 'COMPLETED'
            |GROUP BY c.county, t.year, t.month
          '''.stripMargin
        )
   .toDF()
   .write.mode(Overwrite)
  .cassandraFormat("cc_county_statistics", "cc")
   .save()
"""


