import statistics

print("-------------statistics --- 数学统计函数")
"""
平均值以及对中心位置的评估
这些函数用于计算一个总体或样本的平均值或者典型值。
mean()数据的算术平均数（“平均数”）。
fmean()快速的，浮点算数平均数。
geometric_mean()数据的几何平均数
harmonic_mean()数据的调和均值
median()数据的中位数（中间值）
median_low()数据的低中位数
median_high()数据的高中位数
median_grouped()分组数据的中位数，即第50个百分点。
mode()离散的或标称的数据的单模（最常见的值）。
multimode()离散的或标称的数据的模式列表（最常见的值）。
quantiles()将数据以相等的概率分为多个间隔。

对分散程度的评估
这些函数用于计算总体或样本与典型值或平均值的偏离程度。
pstdev()数据的总体标准差
pvariance()数据的总体方差
stdev()数据的样本标准差
variance()数据的样本方差
"""

# 返回 data 的样本算术平均数，形式为序列或迭代器。
print(statistics.mean([1, 2, 3, 4, 4]))  # 2.8
# 3.8 新版功能. 将 data 转换成浮点数并且计算算术平均数。
# print(statistics.fmean([3.5, 4.0, 5.25])) # 4.25

# 3.8 新版功能. 将 data 转换成浮点数并且计算几何平均数。
# print(statistics.geometric_mean([54, 24, 36])) # 36.000000000000014

# 返回 data 调和均值，该参数可以是序列或包含实数值的可迭代对象。
print(statistics.harmonic_mean([40, 60]))  # 48.0
print(statistics.harmonic_mean([2.5, 3, 10]))  # 3.6 For an equal investment portfolio.

# 使用普通的“取中间两数平均值”方法返回数值数据的中位数（中间值）。 如果 data 为空，则将引发 StatisticsError。 data 可以是序列或可迭代对象。
# 当数据点的总数为奇数时，将返回中间数据点：
print(statistics.median([1, 4, 5]))  # 4
# 当数据点的总数为偶数时，中位数将通过对两个中间值求平均进行插值得出：
print(statistics.median([1, 3, 5, 7]))  # 4

# 返回数值数据的低中位数
# 当数据点总数为奇数时，将返回中间值。 当其为偶数时，将返回两个中间值中较小的那个。
print(statistics.median_low([1, 4, 5]))  # 4
print(statistics.median_low([1, 3, 5, 7]))  # 3

# 返回数据的高中位数
# 当数据点总数为奇数时，将返回中间值。 当其为偶数时，将返回两个中间值中较大的那个。
print(statistics.median_high([1, 4, 5]))  # 4
print(statistics.median_high([1, 3, 5, 7]))  # 5

# 返回分组的连续数据的中位数，根据第 50 个百分点的位置使用插值来计算。 不懂！！！
print(statistics.median_grouped([52, 52, 53, 54]))  # 52.5
print(statistics.median_grouped([5, 3, 7]))  # 5.0
print(statistics.median_grouped([1, 3, 3, 5, 7]))  # 3.25
print(statistics.median_grouped([1, 2, 2, 3, 4, 4, 4, 4, 4, 5]))  # 3.7
print(statistics.median_grouped([1, 2, 2, 3, 4, 4, 4, 4, 4, 5], interval=2))  # 3.4

"""
根据离散或标称的 data 返回单个最觉的数据点。 此模式（如果存在）是最典型的值，并可用来度量中心的位置。
如果存在具有相同频率的多个模式，则返回在 data 中遇到的第一个。 如果想要其中最小或最大的一个，请使用 min(multimode(data)) 或 max(multimode(data))。 
如果输入的 data 为空，则会引发 StatisticsError。
mode 将假定是离散数据并返回一个单一的值。 这是通常的学校教学中标准的处理方式：
"""
# 返回最常见数据或出现次数最多的数据
print(statistics.mode([1, 1, 2, 3, 3, 3, 3, 4]))  # 3
print(statistics.mode(["red", "blue", "blue", "red", "green", "red", "red"]))  # red

# 3.8 新版功能.返回最频繁出现的值的列表，并按它们在 data 中首次出现的位置排序。 如果存在多种模式则将返回一个以上的模式，或者如果 data 为空则将返回空列表：
# print(statistics.multimode(["red", "blue", "blue", "red", "green", "red", "red"])) # [red]

# 返回总体标准差（总体方差的平方根）
print(statistics.pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))  # 0.986893273527251

# 返回非空序列或包含实数值的可迭代对象 data 的总体方差

data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
print(statistics.pvariance(data))  # 1.25
# 如果你已经计算过数据的平均值，你可以将其作为可选的第二个参数 mu 传入以避免重复计算：
mu = statistics.mean(data)
print(statistics.pvariance(data, mu))  # 1.25

# 返回样本标准差（样本方差的平方根）
print(statistics.stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# 返回包含至少两个实数值的可迭代对象 data 的样本方差。 方差或称相对于均值的二阶矩，是对数据变化幅度（延展度或分散度）的度量。 方差值较大表明数据的散布范围较大；方差值较小表明它紧密聚集于均值附近。
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.variance(data))
# 如果你已经计算过数据的平均值，你可以将其作为可选的第二个参数 xbar 传入以避免重复计算：
m = statistics.mean(data)
print(statistics.variance(data, m))

"""
将 data 分隔为具有相等概率的 n 个连续区间。 返回分隔这些区间的 n - 1 个分隔点的列表。

将 n 设为 4 以使用四分位（默认值）。 将 n 设为 10 以使用十分位。 将 n 设为 100 以使用百分位，即给出 99 个分隔点来将 data 分隔为 100 个大小相等的组。 如果 n 小于 1 则将引发 StatisticsError。

data 可以是包含样本数据的任意可迭代对象。 为了获得有意义的结果，data 中数据点的数量应当大于 n。 如果数据点的数量小于两个则将引发 StatisticsError。

分隔点是通过对两个最接近的数据点进行线性插值得到的。 例如，如果一个分隔点落在两个样本值 100 和 112 之间距离三分之一的位置，则分隔点的取值将为 104。

method 用于计算分位值，它会由于 data 是包含还是排除总体的最低和最高可能值而有所不同。

默认 method 是 “唯一的” 并且被用于在总体中数据采样这样可以有比样本中找到的更多的极端值。落在 m 个排序数据点的第 i-th 个以下的总体部分被计算为 i / (m + 1) 。给定九个样本值，方法排序它们并且分配一下的百分位： 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90% 。

将 method 设为 "inclusive" 可用于描述总体数据或已明确知道包含有总体数据中最极端值的样本。 data 中的最小值会被作为第 0 个百分位而最大值会被作为第 100 个百分位。 
总体数据里处于 m 个已排序数据点中 第 i 个 以下的部分会以 (i - 1) / (m - 1) 来计算。 
给定 11 个样本值，该方法会对它们进行排序并赋予以下百分位: 0%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%。
"""
# 3.8 新版功能.
data = [105, 129, 87, 86, 111, 111, 89, 81, 108, 92, 110,
        100, 75, 105, 103, 109, 76, 119, 99, 91, 103, 129,
        106, 101, 84, 111, 74, 87, 86, 103, 103, 106, 86,
        111, 75, 87, 102, 121, 111, 88, 89, 101, 106, 95,
        103, 107, 101, 81, 109, 104]
# print([round(q, 1) for q in statistics.quantiles(data, n=10)]) # [81.0, 86.2, 89.0, 99.4, 102.5, 103.6, 106.0, 109.8, 111.0]


#3.8 新版功能. class statistics.NormalDist(mu=0.0, sigma=1.0)  NormalDist 工具可用于创建和操纵 随机变量 的正态分布。 这个类将数据度量值的平均值和标准差作为单一实体来处理。
#
# temperature_february = statistics.NormalDist(5, 2.5)             # Celsius
# print(temperature_february * (9/5) + 32 )                    # Fahrenheit
# birth_weights = statistics.NormalDist.from_samples([2.5, 3.1, 2.1, 2.4, 2.7, 3.5])
