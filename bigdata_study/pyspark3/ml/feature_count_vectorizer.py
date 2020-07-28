from pyspark.sql import SparkSession
from pyspark.ml.feature import CountVectorizer
"""
三种文本特征提取（TF-IDF/Word2Vec/CountVectorizer）

每个单词出现的频率；然后构成一个特征矩阵，每一行表示一个训练文本的词频统计结果
"""

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("CountVectorizerExample")\
        .getOrCreate()


    # Input data: Each row is a bag of words with a ID.
    df = spark.createDataFrame([
        (0, "a b c".split(" ")),
        (1, "a b b c a".split(" "))
    ], ["id", "words"])

    # fit a CountVectorizerModel from the corpus.
    cv = CountVectorizer(inputCol="words", outputCol="features", vocabSize=3, minDF=2.0)

    model = cv.fit(df)

    result = model.transform(df)
    result.show(truncate=False)


    spark.stop()
