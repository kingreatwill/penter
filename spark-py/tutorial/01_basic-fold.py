# spark-py\tutorial\01_basic-average.py

import sys
import time
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Fold") \
        .getOrCreate()
    sc = spark.sparkContext
    numbers = sc.parallelize([1, 2, 3, 4])
    mult = numbers.fold(1, (lambda x, y: x * y))
    print(mult)

    sum = numbers.fold(0, (lambda x, y: x + y))
    print(sum)


    spark.stop()
