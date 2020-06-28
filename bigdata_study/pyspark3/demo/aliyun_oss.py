# https://github.com/aliyun/aliyun-emapreduce-sdk
# https://help.aliyun.com/document_detail/28118.html
# https://pypi.org/project/aliyun-python-sdk-emr/
# https://develop.aliyun.com/tools/sdk?#/python
# pip install aliyun-python-sdk-emr

# https://ci.apache.org/projects/flink/flink-docs-release-1.10/zh/ops/filesystems/oss.html

"""

 conf.set("spark.hadoop.fs.oss.impl", "com.aliyun.fs.oss.nat.NativeOssFileSystem")
    conf.set("spark.hadoop.mapreduce.job.run-local", "true")
    conf.set("spark.hadoop.fs.oss.accessKeyId", "accessKeyId")
    conf.set("spark.hadoop.fs.oss.accessKeySecret", "accessKeySecret")

spark.hadoop.fs.oss.accessKeyId = xxxxxx
spark.hadoop.fs.oss.accessKeySecret = xxxxxx
spark.hadoop.fs.oss.endpoint = oss-xxxxxx-internal.aliyuncs.com


sc.textFile(inputPath) // 路径格式 oss://bucket.Endpoint/datapath

"""
from pyspark import SparkContext

sc = SparkContext(appName="KMeansExample")

rdd = sc.textFile("oss://bucket.Endpoint/kmeans_data.txt")

