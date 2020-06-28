# http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD
# 核心
"""
RDD 算子类型：
Transformation（转换）：
    根据数据集创建一个新的数据集，计算后返回一个新RDD；例如：一个rdd进行map操作后生了一个新的rdd。

    Spark宽窄依赖详解  https://blog.csdn.net/modefrog/article/details/79581770
    宽依赖：父RDD的分区被子RDD的多个分区使用   例如 groupByKey、reduceByKey、sortByKey等操作会产生宽依赖，会产生shuffle
    窄依赖：父RDD的每个分区都只被子RDD的一个分区使用  例如map、filter、union等操作会产生窄依赖

Action（动作）：
    对rdd结果计算后返回一个数值value给驱动程序；

# Spark中控制算子也是懒执行的，需要Action算子触发才能执行，主要是为了对数据进行缓存。

有人说还有 控制算子：
cache # 对于重复使用的算子,进行cache做缓存使用,数据只保存在内存中,性能提升（有action动作才会cache）
persist
# 对应unpersist，unpersist将RDD标记为非持久性，并从内存和磁盘中删除它的所有块。
checkPoint
"""
from pyspark import SparkContext

"""
名词解释：
shuffle

job
一个 job，就是由一个 rdd 的 action 触发的动作，可以简单的理解为，当你需要执行一个 rdd 的 action 的时候，会生成一个 job。

stage
stage 是一个 job 的组成单位，就是说，一个 job 会被切分成 1 个或 1 个以上的 stage，然后各个 stage 会按照执行顺序依次执行。
Stage的划分规则
1.从后向前推理，遇到宽依赖就断开，遇到窄依赖就把当前的RDD加入到Stage中；
2.每个Stage里面的Task的数量是由该Stage中最后 一个RDD的Partition数量决定的；
3.最后一个Stage里面的任务的类型是ResultTask，前面所有其他Stage里面的任务类型都是ShuffleMapTask；
4.代表当前Stage的算子一定是该Stage的最后一个计算步骤；

总结：由于spark中stage的划分是根据shuffle来划分的，而宽依赖必然有shuffle过程，因此可以说spark是根据宽窄依赖来划分stage的。


task
即 stage 下的一个任务执行单元，一般来说，一个 rdd 有多少个partition，就会有多少个 task，因为每一个 task 只是处理一个partition 上的数据。

Pipeline
在spark中pipeline是一个partition对应一个partition，所以在stage内部只有窄依赖
stage与stage之间是宽依赖

"""
sc = SparkContext(appName="rdd")
rdd = sc.parallelize([1, 2, 3, 4])

print(len(dir(rdd)))  # 144
funcs = [element for element in dir(rdd) if not element.startswith("_")]
print(len(funcs))  # 106

# https://www.jb51.net/article/163214.htm
print("-----------aggregate函数---treeAggregate-----------")


# seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
def seqOp(x, y):
    print("seqOp:%s,%s" % (x, y))
    return (x[0] + y, x[1] + 1)


# combOp = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
def combOp(x, y):
    print("combOp:%s,%s" % (x, y))
    return (x[0] + y[0], x[1] + y[1])


agg_rdd = sc.parallelize([1, 2, 3, 4], 4).aggregate((0, 0), seqOp, combOp)
print(agg_rdd)  # (10,4)
print(sc.parallelize([1, 2, 3, 4], 4).aggregate((3, 3), seqOp, combOp))  # 1个分区的结果(16, 10)     4个分区的结果(25, 19)
print(sc.parallelize([], 4).aggregate((3, 3), seqOp, combOp))  # 1个分区的结果(6, 6)         4个分区的结果(15, 15)
"""
seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
第一步x=(3, 3),y=1  结果(4, 4)
第二步:将第一步的结果tuple作为参数传入进去 x=(4, 4),y=2 结果(6, 5)
第三步：y=3  (9, 6) 第四步：y=4 (13,7)
其次是分区之间的聚合，分区之间的聚合也是要在初始值的基础上相加的
(16,10)

将每个分区里面的元素进行聚合，然后用combine函数将每个分区的结果和初始值(zeroValue)进行combine操作。这个函数最终返回的类型不需要和RDD中元素类型一致。

seqOp操作会聚合各分区中的元素，然后combOp操作把所有分区的聚合结果再次聚合，两个操作的初始值都是zeroValue.   
seqOp的操作是遍历分区中的所有元素(T)，第一个T跟zeroValue做操作，结果再作为与第二个T做操作的zeroValue，直到遍历完整个分区。
combOp操作是把各分区聚合的结果，再聚合。aggregate函数返回一个跟RDD不同类型的值。因此，需要一个操作seqOp来把分区中的元素T合并成一个U，另外一个操作combOp把所有U聚合。

该函数是spark中的一个高性能的算子，它实现了先进性分区内的聚合之后在进行了对每个分区的聚合结果再次进行聚合的操作，
这样的在大数据量的情况下，大大减少了数据在各个节点之间不必要的网络IO，大大提升了性能，相比于groupBy的函数，在特定情况下，性能提升数十倍不止
"""
print("-----------aggregateByKey函数--------------")
rdd = sc.parallelize([(1, 1), (1, 2), (2, 1), (2, 3), (2, 4), (1, 7)], 2)


def seqFunc(a, b):
    print("seqFunc:%s,%s" % (a, b))
    return max(a, b)  # 取最大值


def combFunc(a, b):
    print("combFunc:%s,%s" % (a, b))
    return a + b  # 累加起来


aggregateRDD = rdd.aggregateByKey(3, seqFunc, combFunc)
rest = aggregateRDD.collectAsMap()
print(rest)

# rdd.barrier()
# rdd.cache()
# rdd.checkpoint()  # need sc.setCheckpointDir()
# rdd.localCheckpoint() # The checkpoint directory set through SparkContext.setCheckpointDir() is not used.





print("-----------cartesian 笛卡尔积-------")
rdd = sc.parallelize([1, 2])
rdd2 = sc.parallelize([1, 2, 3])
print(sorted(rdd2.cartesian(rdd).collect()))  # [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
print(sorted(rdd.cartesian(rdd2).collect()))  # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]
print("-----------coalesce 合并-------")
# glom()
# 返回通过将每个分区内的所有元素合并到列表中而创建的RDD。
# rdd = sc.parallelize([1, 2, 3, 4], 2)
# sorted(rdd.glom().collect())
# [[1, 2], [3, 4]]
print(sc.parallelize([1, 2, 3, 4, 5], 3).glom().collect())  # [[1], [2, 3], [4, 5]]
print(sc.parallelize([1, 2, 3, 4, 5], 3).coalesce(1).glom().collect())
# [[1, 2, 3, 4, 5]]


# cogroup 连接两个或多个关系；多关系分组
x = sc.parallelize([("a", 1), ("b", 4)])
y = sc.parallelize([("a", 2)])

print(x.cogroup(y).collect())
# [('a', (<pyspark.resultiterable.ResultIterable object at 0x000001F59811BA08>, <pyspark.resultiterable.ResultIterable object at 0x000001F59811BC48>)),
# ('b', (<pyspark.resultiterable.ResultIterable object at 0x000001F59811BA48>, <pyspark.resultiterable.ResultIterable object at 0x000001F59811B348>))]

# [(x, tuple(map(list, y))) for x, y in sorted(list(x.cogroup(y).collect()))]
# [('a', ([1], [2])), ('b', ([4], []))]

print("---------------combineByKey------------")
# combineByKey是Spark中一个比较核心的高级函数，其他一些高阶键值对函数底层都是用它实现的。诸如 groupByKey,reduceByKey等等
x = sc.parallelize([("a", 1), ("b", 1), ("a", 2)])


def to_list(a):  # createCombiner
    print("createCombiner:{}", a)
    return [a]


def append(a, b):  # mergeValue
    print("mergeValue:{} - {}", a, b)
    a.append(b)
    return a


def extend(a, b):  # mergeCombiners
    print("mergeCombiners:{} - {}", a, b)
    a.extend(b)
    return a


print(sorted(x.combineByKey(to_list, append, extend).collect()))
# [('a', [1, 2]), ('b', [1])]
print("--------------")
data = [("A", 2.), ("A", 4.), ("A", 9.),
        ("B", 10.), ("B", 20.),
        ("Z", 3.), ("Z", 5.), ("Z", 8.), ("Z", 12.)]


def createCombiner2(value):
    print("createCombiner2:{}", value)
    return (value, value * value, 1)


def mergeValue2(x, value):
    print("mergeValue2:{} - {}", x, value)
    return (x[0] + value, x[1] + value * value, x[2] + 1)


def mergeCombiners2(x, y):
    print("mergeCombiners2:{} - {}", x, y)
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


rdd2 = sc.parallelize(data)
sumCount2 = rdd2.combineByKey(
    createCombiner2,
    mergeValue2,
    mergeCombiners2
)
print(sumCount2.collect())
# [('A', (15.0, 101.0, 3)), ('B', (30.0, 500.0, 2)), ('Z', (28.0, 242.0, 4))]


# countApprox count()的近似版本，它在超时时返回可能不完整的结果，即使不是所有任务都已完成。
# countApproxDistinct HyperLogLog

# sorted(sc.parallelize([1, 1, 2, 3]).distinct().collect()) [1, 2, 3]
# sc.parallelize([2, 3, 4]).first()
print("---------------filter-------")
# rdd = sc.parallelize([1, 2, 3, 4, 5])
# rdd.filter(lambda x: x % 2 == 0).collect()
# [2, 4]

print("------------flatMap-----------")
# rdd = sc.parallelize([2, 3, 4])
# sorted(rdd.flatMap(lambda x: range(1, x)).collect())
# [1, 1, 1, 2, 2, 3]
# sorted(rdd.flatMap(lambda x: [(x, x), (x, x)]).collect())
# [(2, 2), (2, 2), (3, 3), (3, 3), (4, 4), (4, 4)]

# x = sc.parallelize([("a", ["x", "y", "z"]), ("b", ["p", "r"])])
# def f(x): return x
# x.flatMapValues(f).collect()
# [('a', 'x'), ('a', 'y'), ('a', 'z'), ('b', 'p'), ('b', 'r')]

print("------------fold-----------")
from operator import add

# 使用给定的关联函数和中性的“零值”，汇总每个分区的元素，然后汇总所有分区的结果。
print(sc.parallelize([1, 2, 3, 4, 5]).fold(0, add))  # 15
print(sc.parallelize([1, 2, 3, 4, 5]).fold(3, add))  # 30 = 15+ (4+1)*3

print(sc.parallelize([1, 2, 3, 4, 5], 2).fold(3, add))  # 24 = 15+ (2+1)*3
print(sc.parallelize([1, 2, 3, 4, 5], 3).fold(3, add))  # 27 = 15+ (3+1)*3

# rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
# from operator import add
# sorted(rdd.foldByKey(0, add).collect())
# [('a', 2), ('b', 1)]

print("----------foreach------------")


def f(x): print(x)


sc.parallelize([1, 2, 3, 4, 5]).foreach(f)


def f(iterator):
    print("ppp")
    for x in iterator:
        print(x)


sc.parallelize([1, 2, 3, 4, 5]).foreachPartition(f)

# rdd.getStorageLevel()
# rdd.getCheckpointFile()
# rdd.getNumPartitions()
# rdd.id()
# rdd.name()

print("-----------groupBy-------------")
rdd = sc.parallelize([1, 1, 2, 3, 5, 8])
result = rdd.groupBy(lambda x: x % 2).collect()
print(result)
# [(0, <pyspark.resultiterable.ResultIterable object at 0x0000014CDF051248>), (1, <pyspark.resultiterable.ResultIterable object at 0x0000014CDF0510C8>)]
# sorted([(x, sorted(y)) for (x, y) in result])
# [(0, [2, 8]), (1, [1, 1, 3, 5])]

rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
print(sorted(rdd.groupByKey().mapValues(len).collect()))
# [('a', 2), ('b', 1)]
print(sorted(rdd.groupByKey().mapValues(list).collect()))
# [('a', [1, 1]), ('b', [1])]


w = sc.parallelize([("a", 5), ("b", 6)])
x = sc.parallelize([("a", 1), ("b", 4)])
y = sc.parallelize([("a", 2)])
z = sc.parallelize([("b", 42)])
print([(x, tuple(map(list, y))) for x, y in sorted(list(w.groupWith(x, y, z).collect()))])
# [('a', ([5], [1], [2], [])), ('b', ([6], [4], [], [42]))]


# rdd = sc.parallelize(range(51))
# rdd.histogram(2)
# ([0, 25, 50], [25, 26])
# rdd.histogram([0, 5, 25, 50])
# ([0, 5, 25, 50], [5, 20, 26])
# rdd.histogram([0, 15, 30, 45, 60])  # evenly spaced buckets
# ([0, 15, 30, 45, 60], [15, 15, 15, 6])
# rdd = sc.parallelize(["ab", "ac", "b", "bd", "ef"])
# rdd.histogram(("a", "b", "c"))
# (('a', 'b', 'c'), [2, 2])
# e.g. [1,10,20,50] means the buckets are [1,10) [10,20) [20,50], which means 1<=x<10, 10<=x<20, 20<=x<=50.

print("------------intersection 交集--------")
# 返回这个RDD和另一个RDD的交集。即使输入RDDs包含重复元素，输出也不会包含重复元素。
rdd1 = sc.parallelize([1, 10, 2, 3, 4, 5])
rdd2 = sc.parallelize([1, 6, 2, 3, 7, 8])
print(rdd1.intersection(rdd2).collect())
# [1, 2, 3]

print(rdd.isLocallyCheckpointed())
print(rdd.isCheckpointed())
print(sc.parallelize([]).isEmpty())  # True
print(sc.emptyRDD().isEmpty())  # True

print("-------union----join------fullOuterJoin------leftOuterJoin--------rightOuterJoin-------")
rdd = sc.parallelize([1, 1, 2, 3])
print(rdd.union(rdd).collect())
# [1, 1, 2, 3, 1, 1, 2, 3]

x = sc.parallelize([("a", 1), ("b", 4)])
y = sc.parallelize([("a", 2), ("a", 3)])
print(sorted(x.join(y).collect()))
# [('a', (1, 2)), ('a', (1, 3))]

x = sc.parallelize([("a", 1), ("b", 4)])
y = sc.parallelize([("a", 2), ("c", 8)])
print(sorted(x.fullOuterJoin(y).collect()))
# [('a', (1, 2)), ('b', (4, None)), ('c', (None, 8))]

x = sc.parallelize([("a", 1), ("b", 4)])
y = sc.parallelize([("a", 2)])
print(sorted(x.leftOuterJoin(y).collect()))
# [('a', (1, 2)), ('b', (4, None))]


x = sc.parallelize([("a", 1), ("b", 4)])
y = sc.parallelize([("a", 2)])
print(sorted(y.rightOuterJoin(x).collect()))
# [('a', (2, 1)), ('b', (None, 4))]




print("-------------keyBy-----------------")

x = sc.parallelize(range(0, 3)).keyBy(lambda x: x * x)
y = sc.parallelize(zip(range(0, 5), range(0, 5)))
print(x.collect())  # [(0, 0), (1, 1), (4, 2)]
print(y.collect())  # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
print([(x, list(map(list, y))) for x, y in sorted(x.cogroup(y).collect())])
# [(0, [[0], [0]]), (1, [[1], [1]]), (2, [[], [2]]), (3, [[], [3]]), (4, [[2], [4]])]


# m = sc.parallelize([(1, 2), (3, 4)]).keys()
# m.collect()
# [1, 3]
#
# m = sc.parallelize([(1, 2), (3, 4)]).values()
# m.collect() # [2, 4]



print("-----------lookup--------------")
# Return the list of values in the RDD for key key.  通过key查找，返回value列表
l = range(1000)
rdd = sc.parallelize(zip(l, l), 10)
print(rdd.lookup(42))  # slow
# [42]
sorted = rdd.sortByKey()
print(sorted.lookup(42))  # fast
# [42]
print(sorted.lookup(1024))
# []
"""
rdd2 = sc.parallelize([(('a', 'b'), 'c')]).groupByKey()
print(list(rdd2.lookup(('a', 'b'))[0]))
# ['c']

报错
Exception: Randomness of hash of string should be disabled via PYTHONHASHSEED

解决方法：

在运行py文件前加入环境变量如下：
os.environ[‘PYTHONHASHSEED’] = “123”

value值随便写即可
如果还不行，在spark配置文件spark-defaults.conf中加入：
spark.executorEnv.PYTHONHASHSEED=0
"""

print("-----------map--------------")
rdd = sc.parallelize(["b", "a", "c"])
print(rdd.map(lambda x: (x, 1)).collect())
# [('a', 1), ('b', 1), ('c', 1)]

rdd = sc.parallelize([1, 2, 3, 4], 2)


def f(iterator):
    yield sum(iterator)


print(rdd.mapPartitions(f).collect())
# [3, 7]

rdd = sc.parallelize([1, 2, 3, 4], 4)


def f(splitIndex, iterator):
    print(splitIndex)
    print(list(iterator))
    yield splitIndex


print(rdd.mapPartitionsWithIndex(f).collect())
#[0, 1, 2, 3]

x = sc.parallelize([("a", ["apple", "banana", "lemon"]), ("b", ["grapes"])])


def f(x):
    return len(x)


print(x.mapValues(f).collect())
# [('a', 3), ('b', 1)]

rdd = sc.parallelize([1.0, 5.0, 43.0, 10.0])
print(rdd.max())
# 43.0
print(rdd.max(key=str))
# 5.0

print(sc.parallelize([1, 2, 3]).mean())
# 2.0
# meanApprox 在超时内返回均值或满足置信度的近似运算。

rdd = sc.parallelize([2.0, 5.0, 43.0, 10.0])
print(rdd.min())
# 2.0
print(rdd.min(key=str))
# 10.0

print("-----------partitionBy-----------")
pairs = sc.parallelize([1, 2, 3, 4, 2, 4, 1]).map(lambda x: (x, x))
print(pairs.collect())
# [(1, 1), (2, 2), (3, 3), (4, 4), (2, 2), (4, 4), (1, 1)]
sets = pairs.partitionBy(2).glom().collect()
print(sets)
# [[(2, 2), (4, 4), (2, 2), (4, 4)], [(1, 1), (3, 3), (1, 1)]]


print("------pipe(command, env=None, checkCode=False)-----")
# sc.parallelize(['1', '2', '', '3']).pipe('cat').collect()
# ['1', '2', '', '3']
# 使用Spark Pipe来给你的既有分析任务提速 https://zhuanlan.zhihu.com/p/72653757

"""
第一步：创建RDD
这一个步骤主要是罗列输入的任务，即，包含哪些文件。

// 此处文件的List可以从另一个HDFS上的文件读取过来
val data = List("hdfs://xxx/xxx/xxx/1.txt","hdfs://xxx/xxx/xxx/2.txt",...)
val dataRDD = sc.makeRDD(data) //sc 是你的 SparkContext
第二步：创建一个Shell脚本启动分析任务
我们已经有了RDD了，那么接下来写一个启动launch.sh脚本来启动我们的分析程序

#!/bin/sh
echo "Running launch.sh shell script..."
while read LINE; do
   echo "启动分析任务, 待分析文件路径为: ${LINE}"
   bash hdfs://xxx/xxx/xx/analysis_program.sh ${LINE}
done
第三步：RDD对接到启动脚本
下面的步骤就是整合步骤了

val scriptPath = "hdfs://xxx/xxx/launch.sh"
val pipeRDD = dataRDD.pipe(scriptPath)
pipeRDD.collect()

"""


print("---------randomSplit(weights, seed=None)-----------")
# rdd = sc.parallelize(range(500), 1)
# rdd1, rdd2 = rdd.randomSplit([2, 3], 17)
# len(rdd1.collect() + rdd2.collect())
# 500
# 150 < rdd1.count() < 250
# True
# 250 < rdd2.count() < 350
# True


print("-------reduce(f) 重点学习-- treeReduce------")
sc.parallelize([1, 2, 3, 4, 5]).reduce(add)
# 15

rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
print(rdd.reduceByKey(add).collect())
# [('a', 2), ('b', 1)]

# rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
# print(rdd.reduceByKeyLocally(add).items())
# [('a', 2), ('b', 1)]

print("-------repartition 重新分配分区---------")
# https://stackoverflow.com/questions/33831561/pyspark-repartition-vs-partitionby
rdd = sc.parallelize([1,2,3,4,5,6,7], 4)
# sorted(rdd.glom().collect())
# [[1], [2, 3], [4, 5], [6, 7]]
print(len(rdd.repartition(2).glom().collect()))
# 2
# len(rdd.repartition(10).glom().collect())

rdd = sc.parallelize([('a', 1), ('a', 2), ('b', 1), ('b', 3), ('c',1), ('ef',5)])
rdd1 = rdd.repartition(4)
rdd2 = rdd.partitionBy(4) # 元素必须有key

print(rdd1.glom().collect())
# [[('b', 1), ('ef', 5)], [], [], [('a', 1), ('a', 2), ('b', 3), ('c', 1)]]

print(rdd2.glom().collect())
# [[('a', 1), ('a', 2)], [], [('c', 1)], [('b', 1), ('b', 3), ('ef', 5)]]


rdd = sc.parallelize([(0, 5), (3, 8), (2, 6), (0, 8), (3, 8), (1, 3)])
rdd2 = rdd.repartitionAndSortWithinPartitions(2, lambda x: x % 2, True)
print(rdd2.glom().collect())
# [[(0, 5), (0, 8), (2, 6)], [(1, 3), (3, 8), (3, 8)]]


print("-----sample-------")
# 提取当前rdd中的样本
"""
rdd = sc.parallelize(range(100), 4)
6 <= rdd.sample(False, 0.1, 81).count() <= 14


fractions = {"a": 0.2, "b": 0.1}
rdd = sc.parallelize(fractions.keys()).cartesian(sc.parallelize(range(0, 1000)))
sample = dict(rdd.sampleByKey(False, fractions, 2).groupByKey().collect())
100 < len(sample["a"]) < 300 and 50 < len(sample["b"]) < 150
True
max(sample["a"]) <= 999 and min(sample["a"]) >= 0
True
max(sample["b"]) <= 999 and min(sample["b"]) >= 0
True
"""
# （标准差，反应平均值的离散程度） https://tool.520101.com/calculator/biaozhuncha-fangcha/
# sampleStdev（与stdev意义相同，stdev分母N-1，sampleStdev分母N）、sampleVariance（方差，所有值平方和除N-1）
# sampleStdev 计算这个RDD元素的样本标准差
sc.parallelize([1, 2, 3]).sampleStdev()
# 1.0

# 计算这个RDD元素的标准差
sc.parallelize([1, 2, 3]).stdev()
# 0.816...

# sampleVariance 计算这个RDD元素的样本方差
sc.parallelize([1, 2, 3]).sampleVariance()
# 1.0

# 计算此RDD元素的方差。
sc.parallelize([1, 2, 3]).variance()
# 0.666...

print("------save-------")
"""
saveAsHadoopDataset(conf, keyConverter=None, valueConverter=None)
saveAsHadoopFile(path, outputFormatClass, keyClass=None, valueClass=None, keyConverter=None, valueConverter=None, conf=None, compressionCodecClass=None)
saveAsNewAPIHadoopDataset(conf, keyConverter=None, valueConverter=None)
saveAsNewAPIHadoopFile(path, outputFormatClass, keyClass=None, valueClass=None, keyConverter=None, valueConverter=None, conf=None)
saveAsPickleFile(path, batchSize=10)
saveAsSequenceFile(path, compressionCodecClass=None)
saveAsTextFile(path, compressionCodecClass=None)
"""

# rdd1.setName('RDD1').name()
# rdd1.stats() # Return a StatCounter object
print("--------sortBy-----------")

tmp = [('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)]
print(sc.parallelize(tmp).sortBy(lambda x: x[0]).collect()) # sc.parallelize(tmp).sortByKey()
# [('1', 3), ('2', 5), ('a', 1), ('b', 2), ('d', 4)]
print(sc.parallelize(tmp).sortBy(lambda x: x[1]).collect())
# [('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)]


print("--------subtract 差集--------")
x = sc.parallelize([("a", 1), ("b", 4), ("b", 5), ("a", 3)])
y = sc.parallelize([("a", 3), ("c", None)])
print(x.subtract(y).collect())
# [('a', 1), ('b', 4), ('b', 5)]

x = sc.parallelize([("a", 1), ("b", 4), ("b", 5), ("a", 2)])
y = sc.parallelize([("a", 3), ("c", None)])
print(x.subtractByKey(y).collect())
# [('b', 4), ('b', 5)]

sc.parallelize([1.0, 2.0, 3.0]).sum()
# 6.0
# sumApprox 在超时内返回总和或满足置信度的近似运算。

print("----------take-------------")

sc.parallelize([2, 3, 4, 5, 6]).cache().take(2)
# [2, 3]
sc.parallelize([2, 3, 4, 5, 6]).take(10)
# [2, 3, 4, 5, 6]
sc.parallelize(range(100), 100).filter(lambda x: x > 90).take(3)
# [91, 92, 93]

sc.parallelize([10, 1, 2, 9, 3, 4, 5, 6, 7]).takeOrdered(6)
# [1, 2, 3, 4, 5, 6]
sc.parallelize([10, 1, 2, 9, 3, 4, 5, 6, 7], 2).takeOrdered(6, key=lambda x: -x)
# [10, 9, 7, 6, 5, 4]



rdd = sc.parallelize(range(0, 10))
len(rdd.takeSample(False, 20, 1))
# 10
len(rdd.takeSample(True, 20, 1))
# 20
len(rdd.takeSample(False, 5, 2))
# 5
len(rdd.takeSample(False, 15, 3))
# 10


# rdd.toDebugString()

# rdd = sc.parallelize(range(10))
# [x for x in rdd.toLocalIterator()]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("--------top-----------")

sc.parallelize([10, 4, 2, 12, 3]).top(1)
# [12]
sc.parallelize([2, 3, 4, 5, 6], 2).top(2)
# [6, 5]
sc.parallelize([10, 4, 2, 12, 3]).top(3, key=str)
# [4, 3, 2]

print("---------zip-----------")
x = sc.parallelize(range(0,5))
y = sc.parallelize(range(1000, 1005))
print(x.zip(y).collect())
# [(0, 1000), (1, 1001), (2, 1002), (3, 1003), (4, 1004)]


print(sc.parallelize(["a", "b", "c", "d"], 3).zipWithIndex().collect()) # x.zip(sc.parallelize(range(0,len(x)))).collect()
# [('a', 0), ('b', 1), ('c', 2), ('d', 3)]

#  zipWithUniqueId   k, n+k, 2*n+k, …,
"""
# [['a', 'b'], ['c', 'd', 'e']]
>>> sc.parallelize(["a", "b", "c", "d", "e"], 2).zipWithUniqueId().collect()
[('a', 0), ('b', 2), ('c', 1), ('d', 3), ('e', 5)]

# [['a'], ['b', 'c'], ['d', 'e']]
>>> sc.parallelize(["a", "b", "c", "d", "e"], 3).zipWithUniqueId().collect()
[('a', 0), ('b', 1), ('c', 4), ('d', 2), ('e', 5)]

# [['a'], ['b'], ['c'], ['d', 'e']]
>>> sc.parallelize(["a", "b", "c", "d", "e"], 4).zipWithUniqueId().collect()
[('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 7)]

>>> sc.parallelize(["a", "b", "c", "d", "e"], 5).zipWithUniqueId().collect()
[('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)]
"""


