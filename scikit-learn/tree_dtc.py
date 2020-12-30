import graphviz
from sklearn import tree, datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

wine = datasets.load_wine()

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data,wine.target,test_size=0.3)

clf = tree.DecisionTreeClassifier(criterion="entropy"
                                 ,random_state=30
                                 ,splitter="random"
                                 ,max_depth=3
                                 ,min_samples_leaf=10
                                 ,min_samples_split=10
                                 )
clf = clf.fit(Xtrain, Ytrain)

feature_name = ['酒精','苹果酸','灰','灰的碱性','镁','总酚','类黄酮','非黄烷类酚类','花青素','颜色强度','色调','od280/od315稀释葡萄酒','脯氨酸']

# dot_data = tree.export_graphviz(clf
#                                ,feature_names= feature_name
#                                ,class_names=["琴酒","雪莉","贝尔摩德"]
#                                ,filled=True
#                                ,rounded=True
#                                )
# graph = graphviz.Source(dot_data)
# graph.save()

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'

plt.figure()
tree.plot_tree(clf
               , feature_names=feature_name
               , class_names=["琴酒", "雪莉", "贝尔摩德"]
               , filled=True
               , rounded=True
               )
plt.show()


