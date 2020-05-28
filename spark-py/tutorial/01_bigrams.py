import sys
import time
from operator import add

from pyspark.sql import SparkSession

# 二元
if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("bigrams") \
        .getOrCreate()
    sc = spark.sparkContext

    lines = sc.textFile("data.txt")

    bigrams = lines.map(lambda s: s.split(" ")).flatMap(lambda s: [((s[i], s[i + 1]), 1) for i in range(0, len(s) - 1)])
    print(bigrams.collect())

    counts = bigrams.reduceByKey(lambda x, y: x + y)
    print(counts.collect())

    spark.stop()
