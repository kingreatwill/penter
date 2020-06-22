from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split


# win use:nc -L -p 9999 启动服务
def demo_socket():
    spark = SparkSession \
        .builder \
        .appName("StructuredNetworkWordCount") \
        .getOrCreate()

    # Create DataFrame representing the stream of input lines from connection to localhost:9999
    lines = spark \
        .readStream \
        .format("socket") \
        .option("host", "127.0.0.1") \
        .option("port", 9999) \
        .load()

    # Split the lines into words
    words = lines.select(
       explode(
           split(lines.value, " ")
       ).alias("word")
    )

    # Generate running word count
    wordCounts = words.groupBy("word").count()

    query = wordCounts \
        .writeStream \
        .outputMode("complete") \
        .format("console") \
        .start()

    query.awaitTermination()




"""
words = ...  # streaming DataFrame of schema { timestamp: Timestamp, word: String }

# Group the data by window and word and compute the count of each group
windowedCounts = words.groupBy(
    window(words.timestamp, "10 minutes", "5 minutes"),
    words.word
).count()
"""


"""
words = ...  # streaming DataFrame of schema { timestamp: Timestamp, word: String }

# Group the data by window and word and compute the count of each group
windowedCounts = words \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        window(words.timestamp, "10 minutes", "5 minutes"),
        words.word) \
    .count()
"""

# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0
# 输出 http://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#output-sinks



if __name__ == "__main__":
    demo_socket()