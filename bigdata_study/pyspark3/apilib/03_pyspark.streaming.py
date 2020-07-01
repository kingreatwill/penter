# Spark Streaming vs. Structured Streaming https://dzone.com/articles/spark-streaming-vs-structured-streaming

"""
核心组件
pyspark.streaming.StreamingContext
Main entry point for Spark Streaming functionality.

pyspark.streaming.DStream
A Discretized Stream (DStream), the basic abstraction in Spark Streaming.
"""
import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    sc = SparkContext(appName="Streaming ")
    ssc = StreamingContext(sc, 1)

    lines = ssc.textFileStream("03_pyspark.streaming.py") # return  DStream
    counts = lines.flatMap(lambda line: line.split(" "))\
                  .map(lambda x: (x, 1))\
                  .reduceByKey(lambda a, b: a+b)
    counts.pprint()

    ssc.start()
    ssc.awaitTermination()
