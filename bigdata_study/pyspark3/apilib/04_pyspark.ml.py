# http://spark.apache.org/docs/latest/api/python/pyspark.ml.html
from pyspark.ml.feature import Binarizer
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("SQL-ML") \
    .getOrCreate()

"""
Spark机器学习之特征提取、选择、转换 : https://blog.csdn.net/cheng9981/article/details/63280665/
处理特征的算法，大致分为以下几组：
     1、提取：从“原始”数据提取特征
     2、转换：缩放，转换或修改要素
     3、选择：从一组较大的要素中选择一个子集
     4、局部敏感哈希（LSH）：这类算法将特征变换的方面与其他算法相结合。
"""

df2 = spark.createDataFrame([(0.5, 0.3),(0.5, 0.7)], ["values1", "values2"])
binarizer2 = Binarizer(thresholds=[0.0, 1.0])
binarizer2.setInputCols(["values1", "values2"]).setOutputCols(["output1", "output2"])
binarizer2.transform(df2).show()

from pyspark.ml.feature import Word2Vec

# Input data: Each row is a bag of words from a sentence or document.
documentDF = spark.createDataFrame([
    ("Hi I heard about Spark".split(" "), ),
    ("I wish Java could use case classes".split(" "), ),
    ("Logistic regression models are neat".split(" "), )
], ["text"])

# Learn a mapping from words to Vectors.
word2Vec = Word2Vec(vectorSize=3, minCount=0, inputCol="text", outputCol="result")
model = word2Vec.fit(documentDF)

result = model.transform(documentDF)
for row in result.collect():
    text, vector = row
    print("Text: [%s] => \nVector: %s\n" % (", ".join(text), str(vector)))