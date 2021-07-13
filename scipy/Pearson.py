import numpy as np
from scipy.stats import pearsonr
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cosine
from sklearn.preprocessing import StandardScaler
"""
Pearson相关性系数（Pearson Correlation）是衡量向量相似度的一种方法。输出范围为-1到+1, 0代表无相关性，负值为负相关，正值为正相关。
[如何理解皮尔逊相关系数（Pearson Correlation Coefficient）](https://www.zhihu.com/question/19734616/answer/349132554)

# 修改当前工作目录（也可以在ipynb上使用）
os.chdir(path)
"""