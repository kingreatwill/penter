import sys
import time
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("combineByKey") \
        .getOrCreate()
    sc = spark.sparkContext
    input = [("k1", 1), ("k1", 2), ("k1", 3), ("k1", 4), ("k1", 5),
             ("k2", 6), ("k2", 7), ("k2", 8),
             ("k3", 10), ("k3", 12)]
    rdd = sc.parallelize(input)

    # 三个lambda分别是createCombiner, mergeValue, mergeCombiners
    #  - C{createCombiner}, which turns a V into a C (e.g., creates a one-element list)
    #  - C{mergeValue}, to merge a V into a C (e.g., adds it to the end of a list)
    #  - C{mergeCombiners}, to combine two C's into a single one (e.g., merges the lists) (此函数作用范围在rdd的不同分区间内，跨分区合并)
    sumCount = rdd.combineByKey(
        (lambda x: (x, 1)), # x其实是value 拿k2来说 - 也就是 6,7,8 创建只取第一个 -》结果(k2,(6,1))
        (lambda x, y: (x[0] + y, x[1] + 1)),# x其实是上一步的结果 也就是 （(6,1)[0]+7,(6,1)[1]+1） # y是value  第二个结果 （K3,(13,2)） 第三个结果 = 第二个结果 + mergeValue （(13,2)[0]+8,(13,2)[1]+1） 结果('k2', (21, 3))
        (lambda x, y: (x[0] + y[0], x[1] + y[1])) # 跨分区合并，如果在一个分区，这个函数没有意义
    )

    print(sumCount.collect())
    # [('k1', (15, 5)), ('k2', (21, 3)), ('k3', (22, 2))]

    avg = sumCount.mapValues(lambda v: v[0] / v[1])
    print(avg.collect())
    # [('k1', 3.0), ('k2', 7.0), ('k3', 11.0)]



    print("--------------")
    data = [("A", 2.), ("A", 4.), ("A", 9.),
        ("B", 10.), ("B", 20.),
        ("Z", 3.), ("Z", 5.), ("Z", 8.), ("Z", 12.)]

    rdd2 = sc.parallelize(data)
    sumCount2 = rdd2.combineByKey(
        lambda value: (value, value * value, 1),
        lambda x, value: (x[0] + value, x[1] + value * value, x[2] + 1),
        lambda x, y: (x[0] + y[0], x[1] + y[1], x[2] + y[2])
        )
    print(sumCount2.collect())
    # [('A', (15.0, 101.0, 3)), ('B', (30.0, 500.0, 2)), ('Z', (28.0, 242.0, 4))]

    import math
    def stdDev(sumX, sumSquared, n):
        mean = sumX / n
        stdDeviation = math.sqrt((sumSquared - n * mean * mean) / n)
        return (mean, stdDeviation)


    meanAndStdDev = sumCount2.mapValues(lambda x: stdDev(x[0], x[1], x[2]))
    print(meanAndStdDev.collect())
    # [('A', (5.0, 2.943920288775949)), ('B', (15.0, 5.0)), ('Z', (7.0, 3.391164991562634))]


    spark.stop()
    """
    data = [
        (A, 2.), (A, 4.), (A, 9.), 
        (B, 10.), (B, 20.), 
        (Z, 3.), (Z, 5.), (Z, 8.), (Z, 12.) 
    ]
    rdd = sc.parallelize( data )    
    sumCount = rdd.combineByKey(lambda value: (value, 1),
                                lambda x, value: (x[0] + value, x[1] + 1),
                                lambda x, y: (x[0] + y[0], x[1] + y[1])
                               )    
    averageByKey = sumCount.map(lambda (key, (totalSum, count)): (key, totalSum / count))    
    averageByKey.collectAsMap()    
    Result:    
    {
      A: 5.0, 
      B: 15.0
      Z: 7.0
    }
    
    
    解析：
    data = [
        ("A", 2.), ("A", 4.), ("A", 9.), 
        ("B", 10.), ("B", 20.), 
        ("Z", 3.), ("Z", 5.), ("Z", 8.), ("Z", 12.) 
       ]

    Partition 1: ("A", 2.), ("A", 4.), ("A", 9.), ("B", 10.)
    Partition 2: ("B", 20.), ("Z", 3.), ("Z", 5.), ("Z", 8.), ("Z", 12.) 
    
    
    Partition 1 
    ("A", 2.), ("A", 4.), ("A", 9.), ("B", 10.)
    
    A=2. --> createCombiner(2.) ==> accumulator[A] = (2., 1)
    A=4. --> mergeValue(accumulator[A], 4.) ==> accumulator[A] = (2. + 4., 1 + 1) = (6., 2)
    A=9. --> mergeValue(accumulator[A], 9.) ==> accumulator[A] = (6. + 9., 2 + 1) = (15., 3)
    B=10. --> createCombiner(10.) ==> accumulator[B] = (10., 1)
    
    Partition 2
    ("B", 20.), ("Z", 3.), ("Z", 5.), ("Z", 8.), ("Z", 12.) 
    
    B=20. --> createCombiner(20.) ==> accumulator[B] = (20., 1)
    Z=3. --> createCombiner(3.) ==> accumulator[Z] = (3., 1)
    Z=5. --> mergeValue(accumulator[Z], 5.) ==> accumulator[Z] = (3. + 5., 1 + 1) = (8., 2)
    Z=8. --> mergeValue(accumulator[Z], 8.) ==> accumulator[Z] = (8. + 8., 2 + 1) = (16., 3)
    Z=12. --> mergeValue(accumulator[Z], 12.) ==> accumulator[Z] = (16. + 12., 3 + 1) = (28., 4)
    
    Merge partitions together
    A ==> (15., 3)
    B ==> mergeCombiner((10., 1), (20., 1)) ==> (10. + 20., 1 + 1) = (30., 2)
    Z ==> (28., 4)
    
    So, you should get back an array something like this:    
    Array( [A, (15., 3)], [B, (30., 2)], [Z, (28., 4)])
    """
