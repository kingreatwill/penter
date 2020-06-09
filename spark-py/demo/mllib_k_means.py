from numpy import array

from pyspark import SparkContext
from pyspark.mllib.clustering import BisectingKMeans, BisectingKMeansModel

# spark-submit mllib_k_means.py

# 二分KMeans
# K-Means是聚类算法中的最常用的一种，算法最大的特点是简单，好理解，运算速度快
# K-Means算法是一种无监督分类算法
if __name__ == "__main__":
    sc = SparkContext(appName="KMeansExample")

    data = sc.textFile("kmeans_data.txt")
    parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))

    model = BisectingKMeans.train(parsedData, 2, maxIterations=5)

    cost = model.computeCost(parsedData)
    print("Final centers: " + str(model.clusterCenters))
    print("Bisecting K-means Cost = " + str(cost))
    sc.stop()
