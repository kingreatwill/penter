import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rc('font', family='Avenir')
plt.figure(figsize=(8, 7), dpi=100)
plt.title("Anacomy of a figure", fontsize=20, fontweight='heavy')

ax = plt.gca()  # 把刻度读取出来，意思是Get Current Axes
ax.set_xlim(0, 4)  # ax.set_xlim设置x坐标轴范围
ax.set_ylim(0, 4)  # ax.set_ylim设置y坐标轴范围

# 一个坐标轴，分为主副两个刻度。
xmajorLocator = MultipleLocator(1)
ax.xaxis.set_major_locator(xmajorLocator)
ymajorLocator = MultipleLocator(1)
ax.yaxis.set_major_locator(ymajorLocator)

xminorLocator = MultipleLocator(0.25)
ax.xaxis.set_minor_locator(xminorLocator)
yminorLocator = MultipleLocator(0.25)
ax.yaxis.set_minor_locator(yminorLocator)

# 显示副刻度
xminorFormatter = FormatStrFormatter('%0.2f')
ax.xaxis.set_minor_formatter(xminorFormatter)

# 主副刻度线的长度（刻度线出来的长度）
plt.tick_params(which='major', length=16)
plt.tick_params(which='minor', length=4)

# 网格线设置
ax.xaxis.grid(True, which='major', linestyle=(0, (8, 4)))  # 竖着的虚线
ax.yaxis.grid(True, which='major', linestyle=(0, (8, 4)))  # 横着的虚线

# 坐标轴文字
ax.set_xlabel("X axis label", fontsize=12)
ax.set_ylabel("Y axis label", fontsize=12)

# 添加图形 使用ax.plot和ax.scatter分别制作折线图和散点图
x = list(np.arange(0.5, 3.3, 0.1))
y1 = [-0.04658 * i ** 3 + 0.5494 * i ** 2 - 1.3151 * i + 1.415 for i in x]
ax.plot(x, y1, color='red', alpha=0.7, linewidth=2.3)

x = list(np.arange(0.5, 3.5, 0.1))
y2 = [0.1545 * i ** 3 - 0.799 * i ** 2 + 0.4316 * i + 3.744 for i in x]
ax.plot(x, y2, color='blue', alpha=0.7, linewidth=2.3)

A = np.random.randn(1000)
B = np.random.randn(1000)
ax.scatter(A, B, marker='o', color="w", edgecolors='black')

# 添加图例 使用plt.legend()或者ax.legend()都可
plt.legend(["Blue signal","Red signal"])
# 添加文字
ax.text(2.9,2.7,"Gird",family = "DejaVu Sans",fontsize = 11,color = 'blue',weight='heavy')
ax.text(3.45,3.45,"Legend",family = "DejaVu Sans",fontsize = 10,color = 'blue',weight='heavy')
ax.text(1.5,3.85,"Title",family = "DejaVu Sans",fontsize = 11,color = 'blue',weight='heavy')
ax.text(-0.25,3.75,"Major tick",family = "DejaVu Sans",fontsize = 10,color = 'blue',weight='heavy')
ax.text(-0.25,3.25,"Minor tick",family = "DejaVu Sans",fontsize = 10,color = 'blue',weight='heavy')
ax.text(-0.45,2.75,"Major tick label",family = "DejaVu Sans",fontsize = 10,color = 'blue',weight='heavy')
ax.text(0.12,-0.5,"Minor tick label",family = "DejaVu Sans",fontsize = 10,color = 'blue',weight='heavy')

# 其中箭头是通过ax.arrow做出来的，使用方法和ax.text一样通过调整坐标控制
ax.arrow(3.3,0.41,-0.15,-0.33,ec='blue',head_width=0.04)
ax.arrow(3.6,0.41,0.32,-0.15,ec='blue',head_width=0.04)

# 添加自定义图片
# arr_lena = mpimg.imread('/Users/liuhuanshuo/Desktop/WechatIMG2278.png')
# imagebox = OffsetImage(arr_lena, zoom=0.38)
# a1 = AnnotationBbox(imagebox, (0, 4), frameon = False) # 设置图片位置
# ax.add_artist(a1) #就能添加一个空心圆在左上角

plt.show()
