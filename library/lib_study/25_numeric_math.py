import math

print(math.ceil(12.3))  # 13 于或者等于 x 的最小整数
print(math.ceil(-12.3))  # -12 于或者等于 x 的最小整数

print(math.floor(12.6))  # 12 返回 x 的向下取整，小于或等于 x 的最大整数。
print(math.floor(-12.6))  # -13 返回 x 的向下取整，小于或等于 x 的最大整数。

# 3.8 新版功能 comb(n,k) 返回不重复且无顺序地从 n 项中选择 k 项的方式总数。 当 k <= n 时取值为 n! / (k! * (n - k)!)；当 k > n 时取值为零。
# print(math.comb(2, 3)) # 0
# print(math.comb(3, 2)) # 3
print(math.factorial(3) / (math.factorial(2) * math.factorial(3 - 2)))  # 3.0 等同于math.comb(3, 2)

# 返回一个基于 x 的绝对值和 y 的符号的浮点数
print(math.copysign(-1, 2))  # 1.0
print(math.copysign(-1, 0))  # 1.0
print(math.copysign(-1, -0))  # 1.0
print(math.copysign(-1, -0.0))  # -1.0

print(math.fabs(-1.2))  # 1.2  返回 x 的绝对值

print(math.factorial(3))  # 6 返回 x 的阶乘(x!)

# 函数 fmod() 在使用浮点数时通常是首选，而Python的 x % y 在使用整数时是首选。
print(math.fmod(9, 2), 9 % 2)  # 1.0   ,1      9%2
print(math.fmod(-9, 2), -9 % 2)  # -1.0  ,1      -9%2
print(math.fmod(9, -2), 9 % -2)  # 1.0 ,-1       9%-2
print(math.fmod(-9, -2), -9 % -2)  # -1.0 ,-1      -9%-2
# print(math.fmod(-1e-100, 1e100)) 和  print(-1e-100 % 1e100) 结果不一致


# 返回 x 的尾数和指数作为对``(m, e)`` m 是一个浮点数， e 是一个整数，正好是 x == m * 2**e 如果 x 为零，则返回 (0.0, 0) ，否则返回 0.5 <= abs(m) < 1
print(math.frexp(10))  # 0.625,4
print(0.625 * 2 ** 4)

# 返回迭代中的精确浮点值。通过跟踪多个中间部分和来避免精度损失:
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))  # 0.9999999999999999
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))  # 1.0

# 返回整数 a 和 b 的最大公约数,gcd(a, b) 的值是能同时整除 a 和 b 的最大正整数
print(math.gcd(0, 0))  # 0
print(math.gcd(1, 3))  # 1

# 若 a 和 b 的值比较接近则返回 True，否则返回 False。
# rel_tol 是相对容差-它是 a 和 b 之间允许的最大差值，相对于 a 或 b 的较大绝对值。例如，要设置5％的容差，请传递 rel_tol=0.05 。默认容差为 1e-09，确保两个值在大约9位十进制数字内相同。 rel_tol 必须大于零。
# abs_tol 是最小绝对容差 —— 对于接近零的比较很有用。 abs_tol 必须至少为零。
# 如果没有错误发生，结果将是： abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
print(math.isclose(1, 2))  # false
print(math.isclose(1, 2, rel_tol=1))  # True
print(math.isclose(2, 1, abs_tol=1))  # True

# 如果 x 既不是无穷大也不是NaN，则返回 True ，否则返回 False 。 （注意 0.0 被认为 是 有限的。）
print(math.isfinite(0.0))  # True
print(math.isfinite(0.1))  # True
print(math.isfinite(-0.1))  # True
print(math.isfinite(float("inf")))  # False
print(math.isfinite(float("-inf")))  # False
print(math.isfinite(0 * float("-inf")))  # False
# 正负无穷：
print(float("inf"), float("-inf"))
# NaN
print(0 * float("inf"))
print(float('inf') / float('inf'))

print(float("inf") == float("inf"))  # True
print((0 * float("inf")) == (float('inf') / float('inf')))  # False
print((0 * float("inf")) == (0 * float("inf")))  # False
print(889 / float('inf'))  # 0

# 如果 x 是正或负无穷大，则返回 True ，否则返回 False 。
print(math.isinf(float('inf')))  # True

# 如果 x 是 NaN（不是数字），则返回 True ，否则返回 False 。
print(math.isnan(0 * float('inf')))  # True

# 3.8 新版功能.
# 返回非负整数 n 的整数平方根。 这就是对 n 的实际平方根向下取整，或者相当于使得 a² ≤ n 的最大整数 a。
# 对于某些应用来说，可以更适合取值为使得 n ≤ a² 的最小整数 a ，或者换句话说就是 n 的实际平方根向上取整。 对于正数 n，这可以使用 a = 1 + isqrt(n - 1) 来计算。
# print(math.isqrt(4)) # 2
# print(math.isqrt(5)) # 2


# 返回 x * (2**i)  这基本上是函数 frexp() 的反函数。
print(math.ldexp(*math.frexp(10)))  # 10
# print(math.frexp(10))  # 0.625,4
# print(0.625 * 2 ** 4)

# 返回 x 的小数和整数部分。两个结果都带有 x 的符号并且是浮点数。
print(math.modf(1.2))  # (0.19999999999999996, 1.0)
print(math.modf(-1.2))  # (-0.19999999999999996, -1.0)

# 返回不重复且无顺序地从 n 项中选择 k 项的方式总数。 当 k <= n 时取值为 n! / (n - k)!；当 k > n 时取值为零。 如果 k 未指定或为 None，则 k 默认值为 n 并且函数将返回 n!。
# 3.8 新版功能.
# print(math.perm(2, 3))  # 0
# print(math.perm(3, 2))  # 6
# print(math.perm(5))  # 120
# comb(n,k) 返回不重复且无顺序地从 n 项中选择 k 项的方式总数。 当 k <= n 时取值为 n! / (k! * (n - k)!)；当 k > n 时取值为零。

# 3.8 新版功能.
# math.prod(iterable, *, start=1)
# 计算输入的 iterable 中所有元素的积。 积的默认 start 值为 1。
# 当可迭代对象为空时，返回起始值。 此函数特别针对数字值使用，并会拒绝非数字类型。
# print(math.prod([1, 2, 3, 4, 5, 6]))  # 720

# 返回 IEEE 754 风格的 x 相对于 y 的余数
print(math.remainder(9, 2))  # 1.0
print(math.remainder(-9, 2))  # -1.0
print(math.remainder(9, -2))  # 1.0
print(math.remainder(-9, -2))  # -1.0
# 参考与math.fmod()，是不一样的（详细查看../stdtypes/01_stdtypes.py）


# 返回 Real 值 x 截断为 Integral （通常是整数）。 委托给 x.__trunc__()。
print(math.trunc(12.2))  # 12
print(math.trunc(-12.2))  # -12
print("-------------幂函数与对数函数")
print(math.exp(3))  # 20.085536923187668 返回 e 次 x 幂，其中 e = 2.718281... 是自然对数的基数。这通常比 math.e ** x 或 pow(math.e, x) 更精确。
print(math.e ** 3)  # 20.085536923187664
print(pow(math.e, 3))  # 20.085536923187664
print(math.pow(math.e,
               3))  # 20.085536923187664 将返回 x 的 y 次幂  与内置的 ** 运算符不同， math.pow() 将其参数转换为 float 类型。使用 ** 或内置的 pow() 函数来计算精确的整数幂。

print(math.expm1(
    3))  # 19.085536923187668 返回 e 的 x 次幂，减1. 对于小浮点数 x ， exp(x) - 1 中的减法可能导致 significant loss of precision； expm1() 函数提供了一种将此数量计算为全精度的方法:
print(math.exp(1e-5) - 1)  # 1.0000050000069649e-05 gives result accurate to 11 places
print(math.expm1(1e-5))  # 1.0000050000166667e-05 result accurate to full precision

print(math.log(3))  # 1.0986122886681098 返回 x 的自然对数（底为 e ）。
print(math.log(3, 2))  # 1.5849625007211563 使用两个参数，返回给定的 base 的对数 x ，计算为 log(x)/log(base) 。

print(math.log1p(2))  # 1.0986122886681098 返回 1+x (base e) 的自然对数。以对于接近零的 x 精确的方式计算结果。

print(math.log2(3))  # 1.584962500721156 返回 x 以2为底的对数。这通常比 log(x, 2) 更准确。

print(math.log10(3))  # 0.47712125471966244 返回 x 底为10的对数。这通常比 log(x, 10) 更准确。

print(math.pow(2, 3))  # 8.0 将返回 x 的 y 次幂  与内置的 ** 运算符不同， math.pow() 将其参数转换为 float 类型。使用 ** 或内置的 pow() 函数来计算精确的整数幂。

print(math.sqrt(4))  # 2 返回 x 的平方根。
# 区别于  math.isqrt(n)返回非负整数 n 的整数平方根。

print("-------------三角函数")
print(math.acos(0.45))  # 1.1040309877476002   以弧度为单位返回 x 的反余弦值。
print(math.asin(0.45))  # 0.4667653390472964 以弧度为单位返回 x 的反正弦值。
print(math.atan(0.45))  # 0.4228539261329407 以弧度为单位返回 x 的反正切值。
print(math.atan2(45,
                 100))  # 0.4228539261329407 以弧度为单位返回 atan(y / x)  结果是在 -pi 和 pi 之间.例如， atan(1) 和 atan2(1, 1) 都是 pi/4 ，但 atan2(-1, -1) 是 -3*pi/4 。
print(math.cos(90))  # -0.4480736161291701  返回 x 弧度的余弦值。
# print(math.dist([1, 2], [2, 3]))  # 3.8 新版功能. 1.4142135623730951 返回 p 与 q 两点之间的欧几里得距离，以一个坐标序列（或可迭代对象）的形式给出。 两个点必须具有相同的维度。 大致相当于：sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
print(math.hypot(3,
                 2))  # 3.605551275463989 返回欧几里得范数，sqrt(sum(x**2 for x in coordinates))。 这是从原点到坐标给定点的向量长度。对于一个二维点 (x, y)，这等价于使用毕达哥拉斯定义 sqrt(x*x + y*y) 计算一个直角三角形的斜边。
print(math.hypot(6, 8))  # 10 对于一个二维点 (x, y)，这等价于使用毕达哥拉斯定义 sqrt(x*x + y*y) 计算一个直角三角形的斜边。

print(math.sin(90))  # 0.8939966636005579返回 x 弧度的正弦值。
print(math.tan(90))  # -1.995200412208242 返回 x 弧度的正切值。
print("-------------角度转换")
print(math.degrees(0.45))  # 25.783100780887047 将角度 x 从弧度转换为度数。
print(math.radians(90))  # 1.5707963267948966 将角度 x 从度数转换为弧度。
print("-------------双曲函数")
print(math.acosh(90))  # 5.192925985263684 返回 x 的反双曲余弦值。
print(math.asinh(90))  # 5.192987713658941 返回 x 的反双曲正弦值。
print(math.atanh(0.45))  # 0.48470027859405174 返回 x 的反双曲正切值。
print(math.cosh(90))  # 6.102016471589204e+38 返回 x 的双曲余弦值。
print(math.sinh(90))  # 6.102016471589204e+38返回 x 的双曲正弦值。
print(math.tanh(90))  # 1 返回 x 的双曲正切值。
print("-------------特殊函数")
print(math.erf(1))  # 0.8427007929497149  x 的误差函数
print(math.erfc(1))  # 0.1572992070502851 返回 x 处的互补误差函数  1.0 - erf(x)
print(math.gamma(1))  # 1.0 返回 x 处的 伽马函数 值。
print(math.lgamma(1))  # 0.0 返回Gamma函数在 x 绝对值的自然对数。
print("-------------常数")
print(math.pi)  # 数学常数 π = 3.141592...，精确到可用精度。
print(math.tau)  # 数学常数 τ = 6.283185...，精确到可用精度。Tau 是一个圆周常数，等于 2π，圆的周长与半径之比。
print(math.e)  # 自然数常数 数学常数 e = 2.718281...，精确到可用精度。
print(math.inf)  # 浮点正无穷大。 （对于负无穷大，使用 -math.inf 。）相当于 float('inf') 的输出。
print(math.nan)  # 浮点“非数字”（NaN）值。 相当于 float('nan') 的输出。
