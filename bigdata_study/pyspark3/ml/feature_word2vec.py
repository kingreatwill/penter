from pyspark.ml.feature import Word2Vec,Word2VecModel
from pyspark.sql import SparkSession

"""
三种文本特征提取（TF-IDF/Word2Vec/CountVectorizer）

特征提取：
Word2Vec是一种著名的词嵌入（Word Embedding）方法，是google在2013年推出的一个NLP工具，他可以计算每个单词在其给定的语料库环境下的分布式词向量（Distributed Representation,亦直接被称为词向量）。
词向量表示可以在一定程度上刻画每个单词的含义。

word是顺序有意义的实体，比如文档中单词、用户依次点击的商品。
两种实现方式
Skip-gram：用一个词语作为输入，来预测它周围的上下文。同义词
CBOW ：用一个词语的上下文作为输入，来预测这个词语本身。完形填空

已实现word2vec的工具
1）Genvim，python版本
2）Spark.ml word2vec，DataFrames实现Skip-gram模型
3）Spark.mllib word2vec，RDD实现Skip-gram模型

全网新闻数据(SogouCA) 数据集下载：http://www.sogou.com/labs/resource/ca.php
"""

# http://spark.apache.org/docs/3.0.0/api/python/pyspark.ml.html#pyspark.ml.feature.Word2Vec
if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("Word2VecExample")\
        .getOrCreate()

    # Input data: Each row is a bag of words from a sentence or document.
    documentDF = spark.createDataFrame([
        ("Hi I heard about Spark".split(" "), ),
        ("I wish Java could use case classes".split(" "), ),
        ("Logistic regression models are neat".split(" "), )
    ], ["text"])



    # Learn a mapping from words to Vectors.
    word2Vec = Word2Vec(vectorSize=3, minCount=0, inputCol="text", outputCol="result")
    model = word2Vec.fit(documentDF)
    # http://spark.apache.org/docs/3.0.0/api/python/pyspark.ml.html#pyspark.ml.feature.Word2VecModel
    # 找出与单词相似度最接近的单词数目
    find_df = model.findSynonyms("about",3)
    find_df.show()

    # model.save(modelPath)
    # loadedModel = Word2VecModel.load(modelPath)

    result = model.transform(documentDF)
    for row in result.collect():
        text, vector = row
        print("Text: [%s] => \nVector: %s\n" % (", ".join(text), str(vector)))


    spark.stop()