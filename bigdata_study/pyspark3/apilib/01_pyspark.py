from pyspark import SparkContext, SparkConf, AccumulatorParam, SparkFiles, StorageLevel, MarshalSerializer, \
    PickleSerializer, TaskContext, RDDBarrier, BarrierTaskContext

# from pyspark.context import SparkContext # SparkContext实际是在pyspark.context


"""
SparkConf
SparkContext
SparkFiles
RDD
StorageLevel
Broadcast
Accumulator
AccumulatorParam
MarshalSerializer
PickleSerializer
StatusTracker
SparkJobInfo
SparkStageInfo
Profiler
BasicProfiler
TaskContext
RDDBarrier
BarrierTaskContext
BarrierTaskInfo
"""

"""
当前文件主要介绍SparkContext，扫描除了RDD class

核心组件
pyspark.SparkContext
Main entry point for Spark functionality.

pyspark.RDD
A Resilient Distributed Dataset (RDD), the basic abstraction in Spark.
"""

conf = SparkConf()
conf.setAppName("appName")
conf.setMaster("local")
conf.set("key", "value")  # setIfMissing setSparkHome
print(conf.getAll())
print(conf.get('spark.app.name'))
print(conf.contains('spark.app.name'))
print(conf.toDebugString())

# show_profiles()
conf.set('spark.python.profile', 'true')

# Spark功能的主入口点。SparkContext表示到Spark集群的连接，可用于在该集群上创建RDD和广播变量。
# 每个JVM只有一个SparkContext是活动的。在创建新的SparkContext之前，必须停止()活动SparkContext。
# class pyspark.SparkContext(master=None, appName=None, sparkHome=None, pyFiles=None, environment=None, batchSize=0, serializer=PickleSerializer(), conf=None, gateway=None, jsc=None, profiler_cls=<class 'pyspark.profiler.BasicProfiler'>)
# sc = SparkContext(conf=conf)
print("--------------------SparkConf结束---------SparkContext开始-------------------------------")
sc = SparkContext(conf=conf)

sc.setLogLevel("WARN")
print(sc.appName)
# 共享变量累加器
inc = sc.accumulator(1)
inc.add(5)
print(inc.value)

# 共享变量广播
bs = sc.broadcast(10)

# sc.addFile(fulltestpath) # C:/test.txt
# SparkFiles.get(filename ) # test.txt
# 也就是会分发到每个节点


# addPyFile(path)
# 为将来要在此SparkContext上执行的所有任务添加.py或.zip依赖项。 传递的路径可以是本地文件，HDFS（或其他受Hadoop支持的文件系统）中的文件或HTTP，HTTPS或FTP URI。

print(sc.applicationId)
print(sc.defaultMinPartitions)  # 当用户没有给出Hadoop RDDs的默认最小分区数时
print(sc.defaultParallelism)  # 用户未指定时要使用的默认并行级别 (e.g. for reduce tasks)

#
# sc.binaryFiles()
# sc.binaryRecords()

# sc.cancelAllJobs()
# sc.cancelJobGroup(groupId)
# sc.setJobGroup(groupId,"")

# 将概要信息转储到目录路径中
# sc.dump_profiles(path)

rdd = sc.emptyRDD()
# 创建一个没有分区或元素的RDD。

print(sc.getConf())  # 返回SparkConf对象

# getLocalProperty(key)
# Get a local property set in this thread, or null if it is missing. See setLocalProperty().

# classmethod getOrCreate(conf=None)

"""
sc.hadoopFile()
sc.hadoopRDD()
sheet = sc.newAPIHadoopFile(
    '/user/me/sample.txt',
    'org.apache.hadoop.mapreduce.lib.input.TextInputFormat',
    'org.apache.hadoop.io.LongWritable',
    'org.apache.hadoop.io.Text',
    conf={'textinputformat.record.delimiter': 'Time\tMHist'}
)

parquet_rdd = sc.newAPIHadoopFile(
        path,
        'org.apache.parquet.avro.AvroParquetInputFormat',
        'java.lang.Void',
        'org.apache.avro.generic.IndexedRecord',
        valueConverter='org.apache.spark.examples.pythonconverters.IndexedRecordToJavaConverter')
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

# rdd.saveAsHadoopFile()
# rdd.saveAsTextFile() # textFile 行列表  wholeTextFiles返回（文件名 内容）列表
# rdd.saveAsHadoopDataset()
# rdd.saveAsNewAPIHadoopDataset()
# rdd.saveAsNewAPIHadoopFile()
# rdd.saveAsPickleFile() # 对应pickleFile
# rdd.saveAsSequenceFile() # sequenceFile

"""
es_write_conf = { 
    "es.nodes": "localhost", 
    "es.port": "9200", 
    "es.resource": "pipe/word" 
} 
rdd.saveAsNewAPIHadoopFile(
    path='-', 
    outputFormatClass="org.elasticsearch.hadoop.mr.EsOutputFormat", 
    keyClass="org.apache.hadoop.io.NullWritable", 
    valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable", 
    conf=es_write_conf) 
    
value_counts.foreachRDD(lambda rdd: rdd.saveAsNewAPIHadoopFile(...)) 
"""

"""
glom

把rdd中的每个片段映射为一个列表
rdd = sc.parallelize([1, 2, 3, 4], 2)
rdd.collect()结果为[1,2,3,4]  说明rdd中的元素认为数字
rdd.glom.collect()结果为[[1,2],[3,4]] 说明rdd中的元素已经变成了分片映射的列表

parallelize
分发本地Python集合以形成RDD。如果输入表示一个性能范围，建议使用xrange。意思就是最好使用方法，减少传输性能
"""

pr = sc.parallelize([0, 2, 3, 4, 6], 3).glom().collect()
print(pr)  # [[0], [2, 3], [4, 6]]
print(sc.parallelize([0, 2, 3, 4, 6], 10).glom().collect())
# [[], [0], [], [2], [], [3], [], [4], [], [6]]

# sc.range(5).collect() # 等于 sc.parallelize(xrange(5))
# sc.range(2, 4).collect() # sc.parallelize(xrange(2, 4))
# sc.range(1, 7, 2).collect() # sc.parallelize(xrange(1, 7, 2))


print(sc.resources)

"""
runJob(rdd, partitionFunc, partitions=None, allowLocal=False)
对指定的分区集执行给定的partitionFunc，以元素数组的形式返回结果。如果未指定分区，则将在所有分区上运行。
"""

myRDD = sc.parallelize(range(6), 3)
print(sc.runJob(myRDD, lambda part: [x * x for x in part]))
# [0, 1, 4, 9, 16, 25]
print(myRDD.getNumPartitions())  # 3
print(sc.runJob(myRDD, lambda part: [x * x for x in part], [0, 2], True))
# [0, 1, 16, 25]

# RDD的持久化/缓存、容错机制Checkpoint https://msd.misuland.com/pd/4146263708462485282
"""
rdd.cache()

//设置检查点目录,会立即在HDFS上创建一个空目录
sc.setCheckpointDir("hdfs://node01:8020/ckpdir") 

//对rdd1进行检查点保存
rdd1.checkpoint() 
"""

# setJobDescription(value) 设置可读的当前作业描述。

import threading
from time import sleep

result = "Not Set"
lock = threading.Lock()


def map_func(x):
    sleep(100)
    raise Exception("Task should have been cancelled")


def start_job(x):
    global result
    try:
        sc.setJobGroup("job_to_cancel", "some description")
        result = sc.parallelize(range(x)).map(map_func).collect()
    except Exception as e:
        result = "Cancelled"
    lock.release()


def stop_job():
    sleep(5)
    sc.cancelJobGroup("job_to_cancel")


suppress = lock.acquire()
suppress = threading.Thread(target=start_job, args=(10,)).start()
suppress = threading.Thread(target=stop_job).start()
suppress = lock.acquire()
print(result)

# classmethod setSystemProperty(key, value)设置Java系统属性，例如spark.executor.memory。 必须在实例化SparkContext之前调用它。

# Print the profile stats to stdout
# conf.set('spark.python.profile','true')
# dump_profiles(path)
sc.show_profiles()

# Get SPARK_USER for user who is running SparkContext.
print(sc.sparkUser())

print(sc.startTime)  # 1592982207167
print(sc.uiWebUrl)  # http://DESKTOP-PK520IC:4040
print(sc.version)  # 3.0.0

# sc.statusTracker() # Return StatusTracker object
# sc.stop()

# path = os.path.join(tempdir, "union-text.txt")
# with open(path, "w") as testFile:
#    _ = testFile.write("Hello")
# textFile = sc.textFile(path)
# textFile.collect()
# # ['Hello']
# parallelized = sc.parallelize(["World!"])
# sorted(sc.union([textFile, parallelized]).collect())
# # ['Hello', 'World!']

print("--------------------SparkContext结束----------SparkFiles开始------------------------------")

# 解析通过SparkContext.addFile（）添加的文件的路径。
# SparkFiles只包含类方法;用户不应该创建SparkFiles实例。
# classmethod get(filename)
# Get the absolute path of a file added through SparkContext.addFile().
#
# classmethod getRootDirectory()
# Get the root directory that contains files added through SparkContext.addFile().

print("--------------------SparkFiles结束----------StorageLevel开始------------------------------")
# rdd.cache() # 等于 rdd.persist(StorageLevel.MEMORY_ONLY)
print(StorageLevel.DISK_ONLY)
print(StorageLevel.MEMORY_AND_DISK)

print("--------------------StorageLevel结束----------Broadcast开始------------------------------")

b = sc.broadcast([1, 2, 3, 4, 5])
print(b.value)
# [1, 2, 3, 4, 5]
sc.parallelize([0, 0]).flatMap(lambda x: b.value).collect()
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
b.unpersist()
large_broadcast = sc.broadcast(range(10000))

large_broadcast.destroy()
# 销毁与此广播变量有关的所有数据和元数据。 请谨慎使用； 广播变量一旦被销毁，将无法再次使用。

# large_broadcast.unpersist()
# # 在执行器上删除此广播的缓存副本。如果在调用之后使用广播，则需要将其重新发送给每个执行器。


# 直接pickle.dump和load不太明白用处
# large_broadcast.dump()
# large_broadcast.load()
# large_broadcast.load_from_path() # load

print("--------------------Broadcast结束----------Accumulator和AccumulatorParam开始------------------------------")
a = sc.accumulator(3)
a.add(10)


# 有点像自定义累加器
class CanAccumulator:
    def update(self, ac2):
        pass


class KeyAccumulatorParam(AccumulatorParam):
    def zero(self, value):
        return CanAccumulator()

    def addInPlace(self, ac1, ac2):
        ac1.update(ac2)
        return ac1


keyAccum = sc.accumulator(
    CanAccumulator(),
    KeyAccumulatorParam()
)

keyAccum.add(CanAccumulator())

print(keyAccum.value)


class MyAccumulatorParam(AccumulatorParam):
    # def __init__(self):
    #     self.value = 0

    def zero(self, value):
        self.value = 0
        print("---", value) # 目前没有执行（不知道怎么执行）
        return self.value

    def addInPlace(self, ac1, ac2):
        return ac1 + ac2


myAccum = sc.accumulator(
    3,
    MyAccumulatorParam()
)

myAccum.add(25)

print(myAccum.value) # 28

print("------------MarshalSerializer---PickleSerializer------StatusTracker--"
      "---SparkJobInfo-----SparkStageInfo----")

from pyspark.serializers import FramedSerializer,CloudPickleSerializer
# MarshalSerializer,PickleSerializer 在 pyspark有快捷引入，pyspark.serializers包含所有的
# MarshalSerializer 使用Python的Marshal序列化器序列化对象 此序列化器比PickleSerializer更快，但支持的数据类型更少。
x = MarshalSerializer()
# 这个序列化器几乎支持任何Python对象，但速度可能不如更专门的序列化器快。
x2 = PickleSerializer()

# sc = SparkContext("local", "serialization app", serializer = MarshalSerializer())

# 低级状态报告API
sta = sc.statusTracker()
print(sta)
print("------")
print(sta.getActiveJobsIds()) # 返回包含所有活动作业的id的数组。
print(sta.getActiveStageIds()) # 返回包含所有活动阶段的id的数组。
print(sta.getJobIdsForGroup()) # 返回特定作业组中所有已知作业的列表。 如果jobGroup为None，则返回未与作业组关联的所有已知作业。
# print(sta.getJobInfo(JobsId)) # 返回一个SparkJobInfo对象，如果找不到或被垃圾回收，则返回None。
# print(sta.getStageInfo(stageId)) # 返回SparkStageInfo对象，如果无法找到舞台信息或被垃圾收集，则返回None。

print("--Profiler---BasicProfiler----------")

sc.stop()


from pyspark import SparkConf, SparkContext
from pyspark import BasicProfiler,Profiler

class MyCustomProfiler(BasicProfiler):
    def show(self, id):
        print("My custom profiles for RDD:%s" % id)

conf = SparkConf().set("spark.python.profile", "true")
sc = SparkContext('local', 'test', conf=conf, profiler_cls=MyCustomProfiler)
sc.parallelize(range(1000)).map(lambda x: 2 * x).take(10)
sc.parallelize(range(1000)).count()
sc.show_profiles()
# My custom profiles for RDD:1
# My custom profiles for RDD:3
sc.stop()

print("-----TaskContext-----RDDBarrier----BarrierTaskContext----BarrierTaskInfo--------------")
tc = TaskContext.get() # 返回当前活动的TaskContext。可以在用户函数内部调用它，以访问有关正在运行的任务的上下文信息。
if tc:
    print(tc.attemptNumber())
    print(tc.getLocalProperty("key"))
    print(tc.partitionId())
    print(tc.resources())
    print(tc.stageId())
    print(tc.taskAttemptId())

# RDDBarrier(实验性的) 用屏障包装RDD以实现屏障执行。 屏障调度器barrier scheduling
# Spark 为了支持深度学习而引入的屏障调度器
b = rdd.barrier()# b = RDDBarrier(rdd)
# b.mapPartitions()
# b.mapPartitionsWithIndex()

# bt = BarrierTaskContext.get()
# if bt:
#     print(bt.getTaskInfos())
#     # Returns BarrierTaskInfo for all tasks in this barrier stage, ordered by partition ID.