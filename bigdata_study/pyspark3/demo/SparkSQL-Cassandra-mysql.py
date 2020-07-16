import os
from pyspark.sql import SparkSession

os.environ[
    'PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.0.0-beta,mysql:mysql-connector-java:5.1.40 pyspark-shell'

if "__main__" == __name__:
    spark = SparkSession \
        .builder \
        .appName("SparkCassandraMysql") \
        .getOrCreate()

    def load_and_get_table_df(keys_space_name, table_name):
        table_df = spark.read \
            .format("org.apache.spark.sql.cassandra") \
            .options(table=table_name, keyspace=keys_space_name) \
            .option("spark.cassandra.connection.host", "127.0.0.1") \
            .load()
        return table_df


    # sample_kvs = load_and_get_table_df("examples", "tbl_sample_kv")
    sample_kvs = load_and_get_table_df("examples", "sample_times")
    sample_kvs.show()

    # --jars E:\elastic\canal\canal.admin-1.1.4.tar\canal.admin-1.1.4\lib\mysql-connector-java-5.1.40.jar
    # properties = { 'user' : 'x', 'password' : 'x',"driver" :"com.mysql.jdbc.Driver" }
    # tb = spark.read.jdbc("jdbc:mysql://192.168.1.50:3306/x",table="ProductBasic",properties=properties)

    tb = spark.read.format("jdbc") \
        .option("url", "jdbc:mysql://127.0.0.1:3306/DemoCloud?useSSL=false") \
        .option("driver", "com.mysql.jdbc.Driver") \
        .option("dbtable", "ProductBasic") \
        .option("user", "root") \
        .option("password", "123456@lcb") \
        .load()
    tb.show()

    sample_kvs.createOrReplaceTempView("A")
    tb.createOrReplaceTempView("B")

    query = spark.sql("SELECT ProductId,b FROM B JOIN A ON B.ProductId = A.a WHERE B.ProductId < 10")
    query.explain(True)
    query.show()

    query.write \
        .mode("append") \
        .format("org.apache.spark.sql.cassandra") \
        .options(table="sample_times_join", keyspace="examples") \
        .option("spark.cassandra.connection.host", "127.0.0.1") \
        .save()

    # mysql overwrite:清理以前的表数据和结构； append：会重复数据（主键属性会被干掉）
    query.write \
        .mode("append") \
        .format("jdbc") \
        .option("url", "jdbc:mysql://127.0.0.1:3306/DemoCloud?useSSL=false") \
        .option("driver", "com.mysql.jdbc.Driver") \
        .option("dbtable", "sample_times_join2") \
        .option("user", "root") \
        .option("password", "123456@lcb") \
        .save()