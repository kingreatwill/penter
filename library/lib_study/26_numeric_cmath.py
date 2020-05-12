# 关于复数的数学函数
import cmath

print("-------------到极坐标和从极坐标的转换")
"""
使用 矩形坐标 或 笛卡尔坐标 在内部存储 Python 复数 z。 这完全取决于它的 实部 z.real 和 虚部 z.imag。 换句话说:
z == z.real + z.imag*1j
"""
# 将 x 的相位 (也称为 x 的 参数) 返回为一个浮点数。phase(x) 相当于 math.atan2(x.imag, x.real)。 结果处于 [-π, π] 之间
print(cmath.phase(complex(-1.0, 0.0)))  # 3.141592653589793
print(cmath.phase(complex(-1.0, -0.0)))  # -3.141592653589793

print(cmath.polar(complex(1.0,
                          0.0)))  # (1.0, 0.0) 在极坐标中返回 x 的表达方式。返回一个数对 (r, phi)，r 是 x 的模数，phi 是 x 的相位角。 polar(x) 相当于 (abs(x), phase(x))。
print(cmath.rect(1,
                 2))  # (-0.4161468365471424+0.9092974268256817j) 通过极坐标的 r 和 phi 返回复数 x。相当于 r * (math.cos(phi) + math.sin(phi)*1j)。


print("---------------------幂函数与对数函数")

print("---------------------三角函数")



print("---------------------双曲函数")




print("---------------------分类函数")

print("---------------------常数")
print(cmath.pi) # 数学常数 π ，作为一个浮点数。
print(cmath.e) # 数学常数 e ，作为一个浮点数。
print(cmath.tau) # 数学常数 τ ，作为一个浮点数。
print(cmath.inf) # 浮点正无穷大。相当于 float('inf')。
print(cmath.infj) # 具有零实部和正无穷虚部的复数。相当于 complex(0.0, float('inf'))。
print(cmath.nan) # 浮点“非数字”（NaN）值。相当于 float('nan')。
print(cmath.nanj) # 具有零实部和 NaN 虚部的复数。相当于 complex(0.0, float('nan'))。