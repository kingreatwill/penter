from sklearn import datasets  #从sklearn包中加载数据集模块
from sklearn import svm
import pickle
#iris = datasets.load_iris()  #加载鸢尾花数据集
digits = datasets.load_digits() #加载数字图像数据集 ,原始的样例是一张（8 x 8）的图片 digits.images[0]

"""
对于digits数据集，digits.data可以访问得到用来对数字进行分类的特征：
digits.target 就是数字数据集各样例对应的真实数字值。也就是我们的程序要学习的。
"""

# 算法，模型选择
clf = svm.SVC(gamma=0.001, C=100.)
#训练
clf.fit(digits.data[:-1], digits.target[:-1])

#预测，我们可以让这个训练器预测没有作为训练数据使用的最后一张图像是什么数字。
print(clf.predict(digits.data[-1:]))

print(digits.target[-1])

# 模型持久化
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print(clf2.predict(digits.data[-1:]))

# 练习
iris = datasets.load_iris()
clf_iris = svm.SVC()
clf_iris.fit(iris.data[:-1], iris.target[:-1])
print(clf_iris.predict(iris.data[-1:]))
print(iris.target[-1])
