from pyspark import SparkContext, SparkConf, AccumulatorParam

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
核心组件
pyspark.SparkContext
Main entry point for Spark functionality.

pyspark.RDD
A Resilient Distributed Dataset (RDD), the basic abstraction in Spark.
"""

conf = SparkConf().setAppName("appName")
sc = SparkContext(conf=conf)

