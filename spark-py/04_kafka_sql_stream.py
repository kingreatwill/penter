# https://spark.apache.org/docs/2.4.4/structured-streaming-kafka-integration.html
# https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#handling-late-data-and-watermarking
# https://blog.csdn.net/xingoo_/article/details/86143490
# https://www.adaltas.com/en/2019/04/18/spark-streaming-data-pipelines-with-structured-streaming/
# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.4 structured_kafka_wordcount.py  192.168.110.150:9092,192.168.110.151:9092,192.168.110.152:9092 subscribe DemoCloudProvider4gQueue
## --jars spark-streaming-kafka-0-8-assembly_2.11-2.0.0.jar
# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.4 04_kafka_sql_stream.py
# In Jupyter, you could add this
import os
import sys

# setup arguments
submit_args = ' --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.4 '
if 'PYSPARK_SUBMIT_ARGS' not in os.environ:
    os.environ['PYSPARK_SUBMIT_ARGS'] = submit_args
else:
    os.environ['PYSPARK_SUBMIT_ARGS'] += submit_args
# initialize spark
import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.types import *

# LongType() FloatType()
kafkaSchema = StructType([
    StructField("EventId", StringType()), StructField("Code", StringType()),
    StructField("Data", StringType()), StructField("Stamp", TimestampType())])

# 序列化方式：https://blog.csdn.net/shirukai/article/details/85211951
# https://www.adaltas.com/en/2019/04/18/spark-streaming-data-pipelines-with-structured-streaming/
def parse_data_from_kafka_message(sdf, schema):
    from pyspark.sql.functions import split
    # assert sdf.isStreaming == True, "DataFrame doesn't receive streaming data"
    col = split(sdf['value'], ',')  # split attributes to nested array in one Column
    # now expand col to multiple top-level columns
    for idx, field in enumerate(schema):
        sdf = sdf.withColumn(field.name, col.getItem(idx).cast(field.dataType))
    return sdf.select([field.name for field in schema])

def parse_data_from_kafka_message2(sdf, schema):
    import json
    from pyspark.sql.functions import split
    #j = json.loads(sdf['value'])
    print(sdf['value'])
    col = split(sdf['value'], ',')  # split attributes to nested array in one Column
    # now expand col to multiple top-level columns
    for idx, field in enumerate(schema):
        sdf = sdf.withColumn(field.name, col.getItem(idx).cast(field.dataType))
    return sdf.select([field.name for field in schema])
# lines_2 = parse_data_from_kafka_message(lines, kafkaSchema)
# lines_2.groupBy('word').count()
if __name__ == "__main__":
    bootstrapServers = "192.168.110.150:9092,192.168.110.151:9092,192.168.110.152:9092"
    subscribeType = "subscribe"
    topics = "DemoCloudProvider4gQueue"

    spark = SparkSession \
        .builder \
        .appName("StructuredKafkaWordCountxxx") \
        .getOrCreate()

    # Create DataSet representing the stream of input lines from kafka
    lines = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", bootstrapServers) \
        .option(subscribeType, topics) \
        .option("startingOffsets", "earliest") \
        .load() \
        .selectExpr("CAST(value AS STRING)")
    # .option("startingOffsets", "latest")
    """
           subscribeType 表示订阅类型，包括'assign', 'subscribe', 'subscribePattern'。
           如果设置为assign, 那么相应的值就要设置为消费的topic及partition，例如{"topicA":[0,1],"topicB":[2,4]}。
           如果设置为subscribe，相应的值为消费的topic list.
           如果设置为subscribePattern，相应的正则表达式描述
    """
    # lines_2 = parse_data_from_kafka_message2(lines, kafkaSchema)
    # Split the lines into words
    words = lines.select(
        # explode turns each item in an array into a separate row
        explode(
            split(lines.value, '"')
        ).alias('word')
    )

    # Generate running word count
    #  wordCounts = words.groupBy('word').count()
    wordCounts = words.groupBy('word').count()

    # Start running the query that prints the running counts to the console
    # query = wordCounts.writeStream\
    # .queryName("aggregates")\
    # .outputMode("complete")\
    # .format("memory")\
    # .start()
    # spark.sql("select * from aggregates").show(3)
    # query = wordCounts\
    #     .writeStream\
    #     .outputMode('append')        \
    #     .option("path", r"E:\openjw\penter\spark-py\data") \
    #     .option("checkpointLocation", r"E:\openjw\penter\spark-py\data")        \
    #     .format('parquet')\
    #     .start()
    query = wordCounts \
        .writeStream \
        .outputMode('complete') \
        .format('console') \
        .start()
    query.awaitTermination()
