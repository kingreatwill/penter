import numpy as np
from matplotlib import pyplot as plt


#plt.rcParams['font.family']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = np.arange(1, 11)

y = 2 * x + 5
plt.title("Matplotlib demo 你好")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)
plt.show()

