import sys
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("AVG") \
        .getOrCreate()
    sc = spark.sparkContext

    nums = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 20])
    print(nums.collect())

    # reduce()与fold()方法是对同种元素类型数据的RDD进行操作，即必须同构。其返回值返回一个同样类型的新元素。
    sum = nums.reduce(lambda x, y: x + y)
    print(sum)
    print(nums.count())

    # 加上一个初始值作为第一次调用的结果。（例如，加法初始值应为0，乘法初始值应为1）
    sumAndCount = nums.map(lambda x: (x, 1)).fold((0, 0), (lambda x, y: (x[0] + y[0], x[1] + y[1])))

    print(sumAndCount)
    avg = float(sumAndCount[0]) / float(sumAndCount[1])
    print(avg)

    # 第一个lambda对单独一个分区内的数据进行累加及计数，所以lambda表达式为x[0]+y，x[1]+1
    # 第二个lambda方法则是对以上每个分区的结果进行聚合汇总。这里要注意参数的写法，x[0]+y[0]，因为是对每一组序列的累加，所以不再用单独的y来表示了。
    sumAndCount2 = nums.aggregate((0, 0), (lambda x, y: (x[0] + y, x[1] + 1)),
                                  (lambda x, y: (x[0] + y[0], x[1] + y[1])))
    print(sumAndCount2)
    spark.stop()
