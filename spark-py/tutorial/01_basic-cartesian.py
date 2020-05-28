import sys
import time
from operator import add

from pyspark.sql import SparkSession

# 笛卡尔
if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("cartesian") \
        .getOrCreate()
    sc = spark.sparkContext

    a = [('k1', 'v1'), ('k2', 'v2')]
    b = [('k3', 'v3'), ('k4', 'v4'), ('k5', 'v5')]
    rdd1 = sc.parallelize(a)
    rdd2 = sc.parallelize(b)

    rdd3 = rdd1.cartesian(rdd2)
    print(rdd3.collect())

    spark.stop()
