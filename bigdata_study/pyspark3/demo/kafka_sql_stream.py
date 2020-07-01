
# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.4 kafka_sql_stream.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, window
from pyspark.sql.functions import split

# http://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html
if __name__ == "__main__":
    bootstrapServers = "192.168.110.150:9092,192.168.110.151:9092,192.168.110.152:9092"
    subscribeType = "subscribe"
    topics = "kafka_sql_stream_topic"

    spark = SparkSession \
        .builder \
        .appName("StructuredKafkaWordCount") \
        .getOrCreate()


    lines = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", bootstrapServers) \
        .option(subscribeType, topics) \
        .option("startingOffsets", "earliest") \
        .load() \
        .selectExpr("CAST(value AS STRING)")

    """
           subscribeType 表示订阅类型，包括'assign', 'subscribe', 'subscribePattern'。
           如果设置为assign, 那么相应的值就要设置为消费的topic及partition，例如{"topicA":[0,1],"topicB":[2,4]}。
           如果设置为subscribe，相应的值为消费的topic list.
           如果设置为subscribePattern，相应的正则表达式描述
    """

    words = lines.select(
        explode(
            split(lines.value, '[\s,.]')
        ).alias('word')
    )

    wordCounts = words.groupBy("word").count()

    query = wordCounts \
        .writeStream \
        .outputMode('complete') \
        .format('console') \
        .start()
    query.awaitTermination()
