from __future__ import print_function

import sys


from pyspark.sql import SparkSession

# $example on$
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
# $example off$

# http://spark.apache.org/docs/latest/api/python/pyspark.ml.html#module-pyspark.ml.recommendation
if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("ALSExample")\
        .getOrCreate()

    # 第一个字段为用户ID，第二个字段为电影ID，第三个字段为评分，第四个字段为时间戳
    lines = spark.read.text("data/sample_movielens_ratings.txt").rdd
    parts = lines.map(lambda row: row.value.split("::"))
    ratingsRDD = parts.map(lambda p: Row(userId=int(p[0]), movieId=int(p[1]),
                                         rating=float(p[2]), timestamp=int(p[3])))
    ratings = spark.createDataFrame(ratingsRDD)
    # 将数据随机分为训练集和测试集
    (training, test) = ratings.randomSplit([0.8, 0.2])

    # 协同过滤（CF）
    # ALS 算法是基于矩阵分解的协同过滤算法中的一种
    # ALS算法属于User-Item CF(user-cf和item-cf),也叫做混合CF,它同时考虑了User和Item两个方面
    # ALS(alternating least squares)
    # 交替最小二乘法的协同过滤算法（ALS) ->早期推荐系统常用的一种方法是SVD（奇异值分解）

    # ALS算法和训练数据集，产生推荐模型

    # Build the recommendation model using ALS on the training data
    # Note we set cold start strategy to 'drop' to ensure we don't get NaN evaluation metrics
    als = ALS(maxIter=10, # 最大迭代次数,设置太大发生java.lang.StackOverflowError（默认为10）
              regParam=0.2, # 指定ALS中的正则化参数（默认为1.0）
              userCol="userId",
              itemCol="movieId",
              ratingCol="rating",
              coldStartStrategy="drop")
    # numBlocks
    # 用户和项目将被分区为多个块的数量，以便并行化计算（默认为10）。
    # numBlocks参数已分为
    #   numItemBlocks:商品数目（正数）。
    #   numUserBlocks:用户数目（正数）。

    # rank
    # 模型中潜在因子的数量（默认为10）。
    #
    # maxIter
    # 要运行的最大迭代次数（默认为10）。
    #
    # regParam 为了防止过度拟合，加上正则化参数
    # 指定ALS中的正则化参数（默认为1.0）。
    #
    # implicitPrefs
    # 指定是使用显式反馈ALS变体还是使用适用于隐式反馈数据的变量（默认为false，这意味着使用显式反馈）。
    #
    # alpha
    # 适用于ALS的隐式反馈变量的参数，其控制偏好观察中的基线置信度（默认为1.0）。
    # nonnegative指定是否对最小二乘使用非负约束（默认为false）。
    # 因为在某些情况下，方程组的解为负数是没有意义的。虽然方程组可以得到精确解，但却不能取负值解。在这种情况下，其非负最小二乘解比方程的精确解更有意义
    """
    以上定义中，ratings指用户提供的训练数据，它包括用户id集、商品id集以及相应的打分集。
    rank表示隐含因素的数量，也即特征的数量。
    numUserBlocks和numItemBlocks分别指用户和商品的块数量，即分区数量。
    maxIter表示迭代次数。
    regParam表示最小二乘法中lambda值的大小。 
    implicitPrefs表示我们的训练数据是否是隐式反馈数据。
    Nonnegative表示求解的最小二乘的值是否是非负,根据Nonnegative的值的不同，spark使用了不同的求解方法。
    
    1 对每个userId随机初始化N（10）个factor值，由这些值影响userId的权重。
    2 对每个itemId也随机初始化N（10）个factor值。
    3 固定userId，从userFactors矩阵和rating矩阵中分解出itemFactors矩阵。即[Item Factors Matrix] = [User Factors Matrix]^-1 * [Rating Matrix].
    4 固定itemId，从itemFactors矩阵和rating矩阵中分解出userFactors矩阵。即[User Factors Matrix] = [Item Factors Matrix]^-1 * [Rating Matrix].
    5 重复迭代第3，第4步，最后可以收敛到稳定的userFactors和itemFactors。
    6 对itemId进行推断就为userFactors * itemId = rating value；对userId进行推断就为itemFactors * userId = rating value。
    """

    # 训练模型
    model = als.fit(training)

    # 模型评估：计算RMSE，均方根误差
    # RMSE（均方根误差）、MSE（均方误差）、MAE（平均绝对误差）、SD（标准差）
    # 比如考试：总分都是600，你有的满分有的不及格，那么RMSE就大，越小越好
    # Evaluate the model by computing the RMSE on the test data
    predictions = model.transform(test)
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                    predictionCol="prediction")
    rmse = evaluator.evaluate(predictions)
    print("Root-mean-square error = " + str(rmse))

    # Generate top 10 movie recommendations for each user
    userRecs = model.recommendForAllUsers(10)
    # Generate top 10 user recommendations for each movie
    movieRecs = model.recommendForAllItems(10)

    # Generate top 10 movie recommendations for a specified set of users
    users = ratings.select(als.getUserCol()).distinct().limit(3)
    userSubsetRecs = model.recommendForUserSubset(users, 10)
    # Generate top 10 user recommendations for a specified set of movies
    movies = ratings.select(als.getItemCol()).distinct().limit(3)
    movieSubSetRecs = model.recommendForItemSubset(movies, 10)
    # $example off$
    userRecs.show()
    movieRecs.show()
    userSubsetRecs.show()
    movieSubSetRecs.show()

    # model.save("data/m")
    # model.load("data/m")

    spark.stop()



"""
显性与隐性反馈
基于矩阵分解的协同过滤的标准方法将用户项矩阵中的条目视为用户对项目给出的显式偏好，例如，给予电影评级的用户。
在许多现实世界的用例中，通常只能访问隐式反馈（例如，观看，点击，购买，喜欢，分享等）。
spark.ml中用于处理此类数据的方法取自Collaborative Filtering for Implicit Feedback Datasets。
本质上，这种方法不是试图直接对评级矩阵进行建模，而是将数据视为表示用户操作观察强度的数字（例如点击次数或某人花在观看电影上的累积持续时间）。
然后，这些数字与观察到的用户偏好的置信水平相关，而不是与项目的明确评级相关。然后，该模型试图找到可用于预测用户对项目的预期偏好的潜在因素。
https://blog.csdn.net/u012834750/article/details/81560971

缩放正则化参数
我们通过用户在更新用户因素时产生的评级数或在更新产品因子时收到的产品评级数来缩小正则化参数regParam以解决每个最小二乘问题。 
这种方法被命名为“ALS-WR”，并在“Netflix奖的大规模并行协同过滤”一文中进行了讨论。 
它使regParam较少依赖于数据集的规模，因此我们可以将从采样子集中学习的最佳参数应用于完整数据集，并期望获得类似的性能。

小结
在实际应用中，由于待分解的矩阵常常是非常稀疏的，与SVD相比，ALS能有效的解决过拟合问题。
基于ALS的矩阵分解的协同过滤算法的可扩展性也优于SVD。
与随机梯度下降的求解方式相比，一般情况下随机梯度下降比ALS速度快；但有两种情况ALS更优于随机梯度下降：
- 当系统能够并行化时，ALS的扩展性优于随机梯度下降法。
- ALS-WR能够有效的处理用户对商品的隐式反馈的数据
ALS算法的缺点在于：
- 它是一个离线算法。
- 无法准确评估新加入的用户或商品。这个问题也被称为冷启动问题。

协同过滤算法之ALS：https://www.biaodianfu.com/collaborative-filtering-als.html
"""