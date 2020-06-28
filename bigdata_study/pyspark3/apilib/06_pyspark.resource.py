# http://spark.apache.org/docs/latest/api/python/pyspark.resource.html
# New in version 3.0.0.
from pyspark import SparkContext
from pyspark.resource import ResourceInformation

r = ResourceInformation("name",[])

sc = SparkContext(jsc=None)
# SparkContext使用Py4J启动JVM并创建JavaSparkContext。
# 由jsc传入的
# jsc: The JavaSparkContext instance (optional).
# SparkContext(jsc=xx)

"""
源码
Create the Java SparkContext through Py4J
self._jsc = jsc or self._initialize_context(self._conf._jconf)
"""
print(sc.resources)
