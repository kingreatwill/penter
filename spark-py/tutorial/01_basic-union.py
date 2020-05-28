import sys
import time
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Union") \
        .getOrCreate()
    sc = spark.sparkContext
    d1 = [('k1', 1), ('k2', 2), ('k3', 5)]
    d2 = [('k1', 3), ('k2', 4), ('k4', 8)]

    rdd1 = sc.parallelize(d1)
    rdd2 = sc.parallelize(d2)

    rdd3 = rdd1.union(rdd2)
    print(rdd3.collect())

    rdd4 = rdd3.reduceByKey(lambda x, y: x + y)
    print(rdd4.collect())


    spark.stop()
