import sys
import time
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("SortByKey") \
        .getOrCreate()
    sc = spark.sparkContext

    lines = sc.textFile('data.txt', 1)
    frequencies = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
    print(frequencies.collect())

    sorted = frequencies.sortByKey()
    print(sorted.collect())

    sortedDescending = frequencies.sortByKey(False)
    print(sortedDescending.collect())


    spark.stop()
