import sys
import time
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Join") \
        .getOrCreate()
    sc = spark.sparkContext
    # Spark从外部读取数据之textFile https://blog.csdn.net/legotime/article/details/51871724
    # Spark 数据读取与保存（输入、输出）  https://www.cnblogs.com/LXL616/p/11147909.html
    """
    sc.textFiles(path) 能将path 里的所有文件内容读出，以文件中的每一行作为一条记录的方式，

    文件的每一行 相当于 List中以 “,”号 隔开的一个元素，因此可以在每个partition中用for i in data的形式遍历处理Array里的数据;
    
    而使用 sc.wholeTextFiles()时:
    返回的是[(K1, V1), (K2, V2)...]的形式，其中K是文件路径，V是文件内容，这里我们要注意的重点是：
    官方一句话：''Each file is read as a single record'' 这句话，每个文件作为一个记录！这说明这里的 V 将不再是 list 的方式将文件每行拆成一个 list的元素,
    而是将整个文本的内容以字符串的形式读进来，也就是说val = '...line1...\n...line2...\n'
    这时需要你自己去拆分每行！而如果你还是用for i in val的形式来便利 val那么i得到的将是每个字符.
    
    Sequence 文件 
　　      SequenceFile 文件是 Hadoop 用来存储二进制形式的 key-value 对而设计的一种平面
        文件(Flat File)。Spark 有专门用来读取 SequenceFile 的接口。在 SparkContext 中，可以
        调用 sequenceFile[ keyClass, valueClass](path)。
        注意：SequenceFile 文件只针对 PairRDD 
    """
    R = sc.textFile("R.txt")
    print(R.collect())
    S = sc.textFile("S.txt")
    print(S.collect())

    r1 = R.map(lambda s: s.split(","))
    print(r1.collect())
    r2 = r1.flatMap(lambda s: [(s[0], s[1])])
    print(r2.collect())

    s1 = S.map(lambda s: s.split(","))
    print(s1.collect())
    s2 = s1.flatMap(lambda s: [(s[0], s[1])])
    print(s2.collect())

    RjoinedS = r2.join(s2) #r2 包含的
    print(RjoinedS.collect())

    spark.stop()
