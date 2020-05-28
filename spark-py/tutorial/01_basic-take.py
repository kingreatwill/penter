import sys
import time
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Take") \
        .getOrCreate()
    sc = spark.sparkContext
    nums = [10, 1, 2, 9, 3, 4, 5, 6, 7]

    print(sc.parallelize(nums).takeOrdered(3))
    print(sc.parallelize(nums).takeOrdered(3, key=lambda x: -x))
    kv = [(10, "z1"), (1, "z2"), (2, "z3"), (9, "z4"), (3, "z5"), (4, "z6"), (5, "z7"), (6, "z8"), (7, "z9")]
    print(sc.parallelize(kv).takeOrdered(3))
    print(sc.parallelize(kv).takeOrdered(3, key=lambda x: -x[0]))


    spark.stop()
