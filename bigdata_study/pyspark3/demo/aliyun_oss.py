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

# 重磅：阿里云 JindoFS SDK 全面开放使用，OSS 文件各项操作性能得到大幅提升 https://developer.aliyun.com/article/767222?groupCode=aliyunemr
# JindoFS SDK 使用 https://github.com/aliyun/aliyun-emapreduce-sdk/blob/master-2.x/docs/jindofs_sdk_how_to.md
from pyspark import SparkContext

sc = SparkContext(appName="KMeansExample")

rdd = sc.textFile("oss://bucket.Endpoint/kmeans_data.txt")

