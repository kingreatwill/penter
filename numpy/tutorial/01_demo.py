import matplotlib.pyplot as plt
import numpy as np

gold, chihh = 400, 400
gold_height = 40 + 10 * np.random.randn(gold)
chihh_height = 25 + 6 * np.random.randn(chihh)

plt.hist([gold_height, chihh_height], stacked=True, color=['r', 'b'])
plt.show()

"""
我们先输入 python 中需要的模块, matplotlib 和 numpy. 然后用两个简称定义金毛和吉娃娃, gold 和 chihh, 
定义每种狗都有400个样本. 然后开始生成一些身高的数据. 我们假定金毛的平均升高时40cm, 吉娃娃是25cm, 
然后因为每只狗不一定都一样高, 所以我们用 normal distribution 给身高加上一个随机数, 
金毛的的随机幅度可能大一点, 吉娃娃的随机幅度可能小一点. 最后我们用柱状图来可视化化这些高度数据. 
红色代表金毛的高度的个数, 蓝色代表吉娃娃的高度个数.
"""
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.inner(a, b)) # 内积 Inner product
print(np.dot(a, b)) # 点积 Dot product
print(np.cross(a, b)) # 叉积  cross product
print(np.outer(a, b)) # 外积 outer product
print(a*b)
print(a@b) # 等于 np.dot(a, b)

a = np.array([1, 2, 3])
b = np.array([5, 6, 7])
print(np.inner(a, b)) # 内积 Inner product
print(np.dot(a, b))    # 点积 Dot product
print(np.cross(a, b)) # 叉积  cross product
print(np.outer(a, b)) # 外积 outer product
print(a*b)
print(a@b)
# 向量的点积=内积
