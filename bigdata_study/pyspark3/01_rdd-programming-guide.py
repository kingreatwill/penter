from pyspark import SparkContext, SparkConf, AccumulatorParam

#  .setMaster(master) master is a Spark, Mesos or YARN cluster URL, or a special “local” string to run in local mode.
conf = SparkConf().setAppName("appName")
sc = SparkContext(conf=conf)

# RDD - > Resilient Distributed Datasets

# Parallelized Collections
data = [1, 2, 3, 4, 5]
# 可以指定分区数 :sc.parallelize(data,10)
distData = sc.parallelize(data)

red = distData.reduce(lambda a, b: a + b)
print(red)  # 15

# External Datasets

distFile = sc.textFile("01_rdd-programming-guide.py")

# 除了文件，还包括目录，压缩文件和通配符 textFile("/my/directory"), textFile("/my/directory/*.txt"), and textFile("/my/directory/*.gz")
# textFile方法还采用一个可选的第二个参数来控制文件的分区数。 默认情况下，Spark为文件的每个块创建一个分区（HDFS中的块默认为128MB），但是您也可以通过传递更大的值来请求更大数量的分区。 请注意，分区不能少于块。
lineLengths = distFile.map(lambda s: len(s))
# before the reduce, which would cause lineLengths to be saved in memory after the first time it is computed.
lineLengths.persist()
totalLength = lineLengths.reduce(lambda a, b: a + b)
print(totalLength)
"""
Spark非常重要的一个功能特性就是可以将RDD持久化在内存中。当对RDD执行持久化操作时，每个节点都会将自己操作的RDD的partition持久化到内存中，并且在之后对
该RDD的反复使用中，直接使用内存缓存的partition。这样的话，对于针对一个RDD反复执行多个操作的场景，就只要对RDD计算一次即可，后面直接使用该RDD，而不
需要反复计算多次该RDD。

巧妙使用RDD持久化，甚至在某些场景下，可以将spark应用程序的性能提升10倍。对于迭代式算法和快速交互式应用来说，RDD持久化，是非常重要的。

要持久化一个RDD，只要调用其cache()或者persist()方法即可。在该RDD第一次被计算出来时，就会直接缓存在每个节点中。而且Spark的持久化机制还是自动容错的，
如果持久化的RDD的任何partition丢失了，那么Spark会自动通过其源RDD，使用transformation操作重新计算该partition。

cache()和persist()的区别在于，cache()是persist()的一种简化方式，cache()的底层就是调用的persist()的无参版本，同时就是调用persist(MEMORY_ONLY)，将数据持久化到内存
中。如果需要从内存中清楚缓存，那么可以使用unpersist()方法。

Spark自己也会在shuffle操作时，进行数据的持久化，比如写入磁盘，主要是为了在节点失败时，避免需要重新计算整个过程。


RDD的容错机制Checkpoint

持久化的局限
  持久化/缓存可以把数据放在内存中，虽然是快速的，但是也是最不可靠的；也可以把数据放在磁盘上，也不是完全可靠的！例如磁盘会损坏等。

问题解决
    Checkpoint的产生就是为了更加可靠的数据持久化，在Checkpoint的时候一般把数据放在在HDFS上，这就天然的借助了HDFS天生的高容错、高可靠来实现数据最大程度上的安全，实现了RDD的容错和高可用。

可以对频繁使用且重要的数据，先做缓存/持久化，再做checkpint操作

持久化和Checkpoint的区别
1.位置
    Persist 和 Cache 只能保存在本地的磁盘和内存中(或者堆外内存--实验中)
    Checkpoint 可以保存数据到 HDFS 这类可靠的存储上
    
2.生命周期
    Cache和Persist的RDD会在程序结束后会被清除或者手动调用unpersist方法
    Checkpoint的RDD在程序结束后依然存在，不会被删除
    
3.Lineage(血统、依赖链–其实就是依赖关系)
    Persist和Cache，不会丢掉RDD间的依赖链/依赖关系，因为这种缓存是不可靠的，
    如果出现了一些错误(例如 Executor 宕机)，需要通过回溯依赖链重新计算出来。
    Checkpoint会斩断依赖链，因为Checkpoint会把结果保存在HDFS这类存储中，
    更加的安全可靠，一般不需要回溯依赖链。


https://msd.misuland.com/pd/4146263708462485282





if __name__ == "__main__":
    def myFunc(s):
        words = s.split(" ")
        return len(words)

    sc = SparkContext(...)
    sc.textFile("file.txt").map(myFunc)

注意：如果是类的方法，那么类的实例也要发送到集群，为避免此问题，最简单的方法是将字段复制到局部变量中，而不是从外部访问它：
def doStuff(self, rdd):
   return rdd.map(lambda s: self.field + s)
替换成下面的写法
def doStuff(self, rdd):
    field = self.field
    return rdd.map(lambda s: field + s)
"""
# wholeTextFiles 返回 (filename, content) 而textFile 返回one record per line in each file

"""
rdd = sc.parallelize(range(1, 4)).map(lambda x: (x, "a" * x))
rdd.saveAsSequenceFile("sf")  # saveAsPickleFile
print(sorted(sc.sequenceFile("sf").collect()))  # pickleFile
"""


# Saving and Loading Other Hadoop Input/Output Formats
"""
# 在命令行中执行
# ./bin/pyspark --jars E:\bigdata\hadoop-plugin\elasticsearch-hadoop-7.4.2\dist\elasticsearch-hadoop-7.4.2.jar
# https://www.elastic.co/guide/en/elasticsearch/hadoop/current/configuration.html
conf = {
    "es.resource": "x",
    "es.nodes": "x:9200"}  # assume Elasticsearch is running on localhost defaults
rdd = sc.newAPIHadoopRDD("org.elasticsearch.hadoop.mr.EsInputFormat",
                         "org.apache.hadoop.io.NullWritable",
                         "org.elasticsearch.hadoop.mr.LinkedMapWritable",
                         conf=conf)
# Cassandra / HBase 等同上  一般都不这样用，直接Spark SQL 读取，指定format就好了


rdd.first()
"""


# Understanding closures
# 闭包  以下是错误的示例，因为集群，不会有什么global变量

"""counter = 0
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Wrong: Don't do this!!
def increment_counter(x):
    global counter
    counter += x

rdd.foreach(increment_counter)

print("Counter value: ", counter)"""


# Transformations  http://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations
# Actions http://spark.apache.org/docs/latest/rdd-programming-guide.html#actions

# RDD Persistence http://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence
# 上面lineLengths.persist()可以传入持久化等级，默认是MEMORY_ONLY


# Shared Variables 共享变量
## 1. Broadcast Variables 广播变量
## 2. Accumulator（累加变量）
"""
Broadcast Variable会将使用到的变量，仅仅为每个节点拷贝一份，更大的用处是优化性能，减少网络传输以及内存消耗。
Accumulator则可以让多个task共同操作一份变量，主要可以进行累加操作。

Spark提供的Broadcast Variable，是只读的。并且在每个节点上只会有一份副本，而不会为每个task都拷贝一份副本。
因此其最大作用，就是减少变量到各个节点的网络传输消耗，以及在各个节点上的内存消耗。
此外，spark自己内部也使用了高效的广播算法来减少网络消耗。

Spark提供的Accumulator，主要用于多个节点对一个变量进行共享性的操作。Accumulator只提供了累加的功能。但是确给我们提供了多个task对一个变量并行操作的功能。
但是task只能对Accumulator进行累加操作，不能读取它的值。只有Driver程序可以读取Accumulator的值。

"""

broadcastVar = sc.broadcast([1, 2, 3])
accum = sc.accumulator(0)

sc.parallelize([1, 2, 3, 4]).foreach(lambda x: accum.add(x))

print(accum.value) # 10

