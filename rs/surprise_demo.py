from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate

# 内置数据集（Movielens, Jester）
# Load the movielens-100k dataset (download it if needed).
# 'ml-100k', 'ml-1m', and 'jester'.
data = Dataset.load_builtin('ml-100k')

# Use the famous SVD algorithm.
algo = SVD()

# Run 5-fold cross-validation and print results.
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

"""
60% Traning Set 训练数据
20% cross validate set 交叉验证数据 cv
20% Test Set 测试集
"""

# Python推荐系统库--Surprise实战 https://www.cnblogs.com/gezhuangzhuang/p/10207427.html