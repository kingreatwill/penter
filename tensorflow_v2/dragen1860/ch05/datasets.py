from tensorflow.keras import datasets
datasets.mnist.load_data() # 手写数字分类 数据集 60k + 10k（28,28）
datasets.fashion_mnist.load_data() # 衣服、鞋、包包之类的图片，共10个类别 60k + 10k（28,28）
"""
0    T-shirt/top
1    Trouser
2    Pullover
3    Dress
4    Coat
5    Sandal
6    Shirt
7    Sneaker
8    Bag
9    Ankle boot
"""
datasets.cifar10.load_data() # 10 个分类,每个类的正好6000张图像, 50k + 10k（32,32,3）RGB 彩色图片
datasets.cifar100.load_data()
"""
airplane/automobile/bird/cat/deer/dog/frog/horse/ship/truck

https://www.cnblogs.com/cloud-ken/p/8456878.html
cifar100这个数据集就像CIFAR-10，除了它有100个类，每个类包含600个图像。，每类各有500个训练图像和100个测试图像。CIFAR-100中的100个类被分成20个超类。每个图像都带有一个“精细”标签（它所属的类）和一个“粗糙”标签（它所属的超类）
以下是CIFAR-100中的类别列表：
"""
datasets.imdb.load_data()
"""
电影评论分类：二分类问题（IMDB数据集）
IMDB数据集包含来自互联网的50000条严重两极分化的评论，该数据被分为用于训练的25000条评论和用于测试的25000条评论，训练集和测试集都包含50%的正面评价和50%的负面评价。
label为pos(positive)和neg(negative)。
"""
datasets.boston_housing.load_data() # （波士顿房价数据集）  特征数:13,  实例数:506 文件housing.csv中包含14个字段，具体信息如下：
"""
No	属性	    数据类型	字段描述
1	CRIM	Float	城镇人均犯罪率
2	ZN	    Float	占地面积超过2.5万平方英尺的住宅用地比例
3	INDUS	Float	城镇非零售业务地区的比例
4	CHAS	Integer	查尔斯河虚拟变量 (= 1 如果土地在河边；否则是0)
5	NOX	    Float	一氧化氮浓度（每1000万份）
6	RM	    Float	平均每居民房数
7	AGE	    Float	在1940年之前建成的所有者占用单位的比例
8	DIS	    Float	与五个波士顿就业中心的加权距离
9	RAD	    Integer	辐射状公路的可达性指数
10	TAX	    Float	每10,000美元的全额物业税率
11	PTRATIO	Float	城镇师生比例
12	B	    Float	1000（Bk - 0.63）^ 2其中Bk是城镇黑人的比例
13	LSTAT	Float	人口中地位较低人群的百分数
14	MEDV	Float	（目标变量/类别属性）以1000美元计算的自有住房的中位数
"""
datasets.reuters.load_data() # Reuters新闻分类
"""
一共有46个类别。因为有多个类别，属于多分类问题，而每条数据只属于一个类别，所以是单标签多分类问题；(如果每条数据可以被分到多个类别中，那问题则属于多标签多分类问题。)
Reuters数据集发布在1986年，一系列短新闻及对应话题的数据集；是文本分类问题最常用的小数据集。
有8982条训练集，2246条测试集。
"""