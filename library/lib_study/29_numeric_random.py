import random

print("-------------random --- 生成伪随机数")

random.seed(1)
print(random.getstate())
random.setstate(random.getstate())
print(random.getrandbits(10))

print("--------------")
print(random.randrange(20))
print(random.randrange(20))  # 这相当于 choice(range(start, stop, step))

print(random.randint(1, 10))  # 返回随机整数 N 满足 a <= N <= b。相当于 randrange(a, b+1)。

print(random.choice([1, 3, 5]))

print(random.choices(['red', 'black', 'green'], [18, 18, 2], k=6))  # 如果指定了 weight 序列，则根据相对权重进行选择。 返回大小为 k 的元素列表

l = [1, 2, 3]
random.shuffle(l)  # 将序列 x 随机打乱位置。
print(l)

print(random.sample(range(10), k=10))  # 返回从总体序列或集合中选择的唯一元素的 k 长度列表。 用于无重复的随机抽样。

print(random.random())  # 返回 [0.0, 1.0) 范围内的下一个随机浮点数。

# 返回一个随机浮点数 N ，当 a <= b 时 a <= N <= b ，当 b < a 时 b <= N <= a 。 取决于等式 a + (b-a) * random() 中的浮点舍入，终点 b 可以包括或不包括在该范围内。
print(random.uniform(1, 2))

# 返回一个随机浮点数 N ，使得 low <= N <= high 并在这些边界之间使用指定的 mode 。 low 和 high 边界默认为零和一。 mode 参数默认为边界之间的中点，给出对称分布。
print(random.triangular(1, 2, 3))

print(random.betavariate(1, 2))  # Beta 分布。 参数的条件是 alpha > 0 和 beta > 0。 返回值的范围介于 0 和 1 之间。

# 指数分布。 lambd 是 1.0 除以所需的平均值，它应该是非零的。 （该参数本应命名为 “lambda” ，但这是 Python 中的保留字。）如果 lambd 为正，则返回值的范围为 0 到正无穷大；如果 lambd 为负，则返回值从负无穷大到 0。
print(random.expovariate(1))

"""
random.gammavariate(alpha, beta)
Gamma 分布。 （ 不是 gamma 函数！ ） 参数的条件是 alpha > 0 和 beta > 0。

概率分布函数是:

          x ** (alpha - 1) * math.exp(-x / beta)
pdf(x) =  --------------------------------------
            math.gamma(alpha) * beta ** alpha

random.gauss(mu, sigma)
高斯分布。 mu 是平均值，sigma 是标准差。 这比下面定义的 normalvariate() 函数略快。

random.lognormvariate(mu, sigma)
对数正态分布。 如果你采用这个分布的自然对数，你将得到一个正态分布，平均值为 mu 和标准差为 sigma 。 mu 可以是任何值，sigma 必须大于零。

random.normalvariate(mu, sigma)
正态分布。 mu 是平均值，sigma 是标准差。

random.vonmisesvariate(mu, kappa)
冯·米塞斯（von Mises）分布。 mu 是平均角度，以弧度表示，介于0和 2*pi 之间，kappa 是浓度参数，必须大于或等于零。 如果 kappa 等于零，则该分布在 0 到 2*pi 的范围内减小到均匀的随机角度。

random.paretovariate(alpha)
帕累托分布。 alpha 是形状参数。

random.weibullvariate(alpha, beta)
威布尔分布。 alpha 是比例参数，beta 是形状参数。
"""


r = random.Random(1)
print(r.random())

sr = random.SystemRandom(1)
print(sr.random())


"""
# statistical bootstrapping 的示例，使用重新采样和替换来估计一个样本的均值的置信区间:
# http://statistics.about.com/od/Applications/a/Example-Of-Bootstrapping.htm
from statistics import fmean as mean
from random import choices

data = [41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]
means = sorted(mean(choices(data, k=len(data))) for i in range(100))
print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
      f'interval from {means[5]:.1f} to {means[94]:.1f}')
      
使用 重新采样排列测试 来确定统计学显著性或者使用 p-值 来观察药物与安慰剂的作用之间差异的示例:

# Example from "Statistics is Easy" by Dennis Shasha and Manda Wilson
from statistics import fmean as mean
from random import shuffle

drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
observed_diff = mean(drug) - mean(placebo)

n = 10_000
count = 0
combined = drug + placebo
for i in range(n):
    shuffle(combined)
    new_diff = mean(combined[:len(drug)]) - mean(combined[len(drug):])
    count += (new_diff >= observed_diff)

print(f'{n} label reshufflings produced only {count} instances with a difference')
print(f'at least as extreme as the observed difference of {observed_diff:.1f}.')
print(f'The one-sided p-value of {count / n:.4f} leads us to reject the null')
print(f'hypothesis that there is no difference between the drug and the placebo.')
"""

#多服务器队列的到达时间和服务交付模拟:
from heapq import heappush, heappop
from random import expovariate, gauss
from statistics import mean, median, stdev

average_arrival_interval = 5.6
average_service_time = 15.0
stdev_service_time = 3.5
num_servers = 3

waits = []
arrival_time = 0.0
servers = [0.0] * num_servers  # time when each server becomes available
for i in range(100_000):
    arrival_time += expovariate(1.0 / average_arrival_interval)
    next_server_available = heappop(servers)
    wait = max(0.0, next_server_available - arrival_time)
    waits.append(wait)
    service_duration = gauss(average_service_time, stdev_service_time)
    service_completed = arrival_time + wait + service_duration
    heappush(servers, service_completed)

print(f'Mean wait: {mean(waits):.1f}.  Stdev wait: {stdev(waits):.1f}.')
print(f'Median wait: {median(waits):.1f}.  Max wait: {max(waits):.1f}.')