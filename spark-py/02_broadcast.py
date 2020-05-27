import sys
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("PythonWordCount") \
        .getOrCreate()
    sc = spark.sparkContext
    factor = 3
    b_f = sc.broadcast(factor)
    counts = sc.parallelize(range(1, 6)).map(lambda x: x * b_f.value)

    output = counts.collect()
    print(output)

    spark.stop()
