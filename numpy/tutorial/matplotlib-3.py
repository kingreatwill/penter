import numpy as np
from matplotlib import pyplot as plt

# https://matplotlib.org/tutorials/introductory/sample_plots.html

def f1():
    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    # o 显示圆来代表点, r 蓝色
    plt.plot(x, y, "or")
    plt.show()

# 绘制正弦波
# 计算正弦曲线上点的 x 和 y 坐标
def f2():
    x = np.arange(0,  3  * np.pi,  0.1)
    y = np.sin(x)
    plt.title("sine wave form")
    # 使用 matplotlib 来绘制点
    plt.plot(x, y)
    plt.show()

# subplot() 函数允许你在同一图中绘制不同的东西。
#
# 以下实例绘制正弦和余弦值:
def f3():
    # 计算正弦和余弦曲线上的点的 x 和 y 坐标
    x = np.arange(0,  3  * np.pi,  0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    # 建立 subplot 网格，高为 2，宽为 1
    # 激活第一个 subplot
    plt.subplot(3,  1,  1)
    # 绘制第一个图像
    plt.plot(x, y_sin)
    plt.title('Sine')
    # 将第二个 subplot 激活，并绘制第二个图像
    plt.subplot(3,  1,  2)
    plt.plot(x, y_cos)
    plt.title('Cosine')

    # 将第三个 subplot 激活，并绘制第三个图像
    plt.subplot(3, 1, 3)
    y = 2 * x + 5
    plt.plot(x, y)
    plt.title('Cosine')
    # 展示图像
    plt.show()

# pyplot 子模块提供 bar() 函数来生成条形图。
#
# 以下实例生成两组 x 和 y 数组的条形图。
def f4():
    x = [5, 8, 10]
    y = [12, 16, 6]
    x2 = [6, 9, 11]
    y2 = [6, 15, 7]
    plt.bar(x, y, align='center')
    plt.bar(x2, y2, color='g', align='center')
    plt.title('Bar graph')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()

# numpy.histogram()
# numpy.histogram() 函数是数据的频率分布的图形表示。 水平尺寸相等的矩形对应于类间隔，称为 bin，变量 height 对应于频率。
#
# numpy.histogram()函数将输入数组和 bin 作为两个参数。 bin 数组中的连续元素用作每个 bin 的边界。
def f5():
    a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
    hist, bins = np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
    print(hist)
    print(bins)
    # Matplotlib 可以将直方图的数字表示转换为图形。 pyplot 子模块的 plt() 函数将包含数据和 bin 数组的数组作为参数，并转换为直方图。
    plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
    plt.title("histogram")
    plt.show()
# [3 4 5 2 1]  0-20 出现3次   【20-40 4次  。。。。
# [  0  20  40  60  80 100]

# Subplot example
# Many plot types can be combined in one figure to create powerful and flexible representations of data.
def f6():
    np.random.seed(19680801)
    data = np.random.randn(2, 100)

    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    axs[0, 0].hist(data[0])
    axs[1, 0].scatter(data[0], data[1])
    axs[0, 1].plot(data[0], data[1])
    axs[1, 1].hist2d(data[0], data[1])

    plt.show()

if __name__ == '__main__':
    f6()