import sys
import time
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Map") \
        .getOrCreate()
    sc = spark.sparkContext
    nums = sc.parallelize([1, 2, 3, 4, 5])

    bytwo = nums.map(lambda x: x + 2)
    print(bytwo.collect())

    squared = nums.map(lambda x: x * x)
    print(squared.collect())


    spark.stop()
