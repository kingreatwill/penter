from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.sql import SparkSession
"""
三种文本特征提取（TF-IDF/Word2Vec/CountVectorizer）
tf-idf (term frequency - inverse document frequency) 词频-反向文档频率

举个栗子 来说，有一篇100字的短文，其中「猫」这个词出现了3次。那么这篇短文中「猫」的词频tf = 3/100 = 0.03,
如果这里有1000,0000篇文章，其中有「猫」这个词的却文章只有1000个，那么「猫」对应所有文本，也就是整个语料库的逆向文件頻率idf = log(10000000/1000) = log(10000) = 4
这样就可以计算得到「猫」在这篇文章中的tf-idf = 0.03*4 = 0.12 。

现在假设在同一篇文章中，「是」这个词出现了20次，因此「是」这个字的词频为0.2。如果只计算词频的话，在这篇文章中明显「是」是比「猫」重要的。
但我们还有逆向文件頻率，了解到「是」这个字在全部的1000,0000篇文章都出现过了（这样假设可以吗？），那么「是」的逆向文件頻率就是log(10000000/10000000) = 0。
这样综合下来，「是」这个字的 tf-idf 就只有 0了，远不及「猫」重要。
"""
# http://spark.apache.org/docs/3.0.0/api/python/pyspark.ml.html#pyspark.ml.feature.HashingTF
# http://spark.apache.org/docs/3.0.0/api/python/pyspark.ml.html#pyspark.ml.feature.IDF
# http://spark.apache.org/docs/3.0.0/api/python/pyspark.ml.html#pyspark.ml.feature.IDFModel
if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("TfIdfExample")\
        .getOrCreate()


    sentenceData = spark.createDataFrame([
        (0.0, "Hi I heard about Spark"),
        (0.0, "I wish Java could use case classes"),
        (1.0, "Logistic regression models are neat Java")
    ], ["label", "sentence"])

    sentenceData.show(truncate=200)

    tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
    wordsData = tokenizer.transform(sentenceData)
    wordsData.show(truncate=200)

    # 根据给传入的各篇已经分好词的文章，对里面的每个词进行hashing计算，每个hashing值对应词表的一个位置，以及对每个词在每篇文章中的一个统计
    # setBinary(false):多项式分布计算，一个词在一篇文章中出现多少次，计算多少次；
    # setBinary(true):伯努利分布计算，一个词在一篇文章中，不管多少次，只要出现了，就为1，否则为0
    hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
    #  实例化HashingTF之后，使用transform就可以计算词频（TF）。TF的计算
    featurizedData = hashingTF.transform(wordsData)
    featurizedData.show(truncate=200)
    # alternatively, CountVectorizer can also be used to get term frequency vectors
    # IDF的计算
    idf = IDF(inputCol="rawFeatures", outputCol="features")
    idfModel = idf.fit(featurizedData)
    # TF-IDF
    rescaledData = idfModel.transform(featurizedData)
    rescaledData.show(truncate=200)
    rescaledData.select("label", "features").show(truncate=200)


    spark.stop()
