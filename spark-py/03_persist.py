import sys
from operator import add

from pyspark.sql import SparkSession
from pyspark.storagelevel import StorageLevel

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("storagelevel") \
        .getOrCreate()
    sc = spark.sparkContext
    factor = 3
    b_f = sc.broadcast(factor)
    rdd1 = sc.parallelize(range(1, 10), 4).map(lambda x: x * b_f.value)  # 4个分区
    rdd2 = rdd1.persist(StorageLevel.DISK_ONLY) # 持久化到磁盘
    output = rdd2.collect()
    print(output)

    spark.stop()
