# mapPartitions（func）转换与map（）类似，但是分别在RDD的每个分区（块）上运行
import sys
import time
from operator import add

from pyspark.sql import SparkSession
def f(iterator):
    for x in iterator:
            print(x)
    print("===")

def adder(iterator):
    yield sum(iterator)

def minmax(iterator):
    firsttime = 0
    min = 0
    max = 0
    for x in iterator:
        if (firsttime == 0):
            min = x
            max = x
            firsttime = 1
        else:
            if x > max:
                max = x
            if x < min:
                min = x
        #
    return (min, max)

print(minmax([10, 20, 3, 4, 5, 2, 2, 20, 20, 10]))

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("mapPartitions") \
        .getOrCreate()
    sc = spark.sparkContext

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rdd = sc.parallelize(numbers, 3)
    print(rdd.getNumPartitions())  # 3

    rdd.foreachPartition(f)

    print(rdd.mapPartitions(adder).collect())

    data = [10, 20, 3, 4, 5, 2, 2, 20, 20, 10]
    rdd2 = sc.parallelize(data, 3)
    rdd2.foreachPartition(f)
    # 这里会返回每个Partition的最大最小值
    minmaxlist = rdd2.mapPartitions(minmax).collect()
    print(minmaxlist)

    print(min(minmaxlist))
    print(max(minmaxlist))

    spark.stop()
