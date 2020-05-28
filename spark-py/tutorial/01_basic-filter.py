import sys
import time
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Filter") \
        .getOrCreate()
    sc = spark.sparkContext
    nums = sc.parallelize([1, 2, 3, 4, 5, 6, 7])
    filtered1 = nums.filter(lambda x: x % 2 == 1)
    print(filtered1.collect())

    filtered2 = nums.filter(lambda x: x % 2 == 0)
    print(filtered2.collect())

    spark.stop()
