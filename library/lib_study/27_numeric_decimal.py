import decimal

# 十进制数也包括特殊值，例如 Infinity ，-Infinity ，和 NaN 。 该标准还区分 -0 和 +0 。
import math

print(
    decimal.getcontext())  # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
# ROUND_CEILING 、 ROUND_DOWN 、 ROUND_FLOOR 、 ROUND_HALF_DOWN, ROUND_HALF_EVEN 、 ROUND_HALF_UP 、 ROUND_UP 以及 ROUND_05UP.
# 十进制模块中的信号有：Clamped 、 InvalidOperation 、 DivisionByZero 、 Inexact 、 Rounded 、 Subnormal 、 Overflow 、 Underflow 以及 FloatOperation 。
decimal.getcontext().prec = 6
print(decimal.Decimal(1) / decimal.Decimal(7))  # 0.142857

decimal.getcontext().prec = 28
print(decimal.Decimal(1) / decimal.Decimal(7))  # 0.1428571428571428571428571429

print(decimal.Decimal(10))  # 10
print(decimal.Decimal(3.14))  # 3.140000000000000124344978758017532527446746826171875
print(decimal.Decimal("3.14"))  # 3.14

print(decimal.Decimal((0, (3, 1, 4), -2)))  # 3.14
print(decimal.Decimal(str(2.0 ** 0.5)))  # 1.4142135623730951
print(decimal.Decimal(2) ** decimal.Decimal('0.5'))  # 1.414213562373095048801688724
print(decimal.Decimal('NaN'))  # NaN
print(decimal.Decimal('-Infinity'))  # -Infinity

c = decimal.getcontext()
c.traps[decimal.FloatOperation] = True

# print(decimal.Decimal(3.14)) #异常FloatOperation
# print(decimal.Decimal('3.5') < 3.7)#异常FloatOperation

print(decimal.Decimal('3.5') == 3.5)  # true

data = list(map(decimal.Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
print(max(data))

print(decimal.Decimal(2).sqrt())

print(decimal.Decimal('7.325').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN))  # 7.32
print(decimal.Decimal('7.325').quantize(decimal.Decimal('1.'), rounding=decimal.ROUND_UP))  # 8

# myothercontext = decimal.Context(prec=60, rounding=decimal.ROUND_HALF_DOWN)
# decimal.setcontext(myothercontext)
#getcontext().clear_flags()
print(decimal.ExtendedContext)
# decimal.setcontext(decimal.ExtendedContext)
print(decimal.BasicContext)
# decimal.setcontext(decimal.BasicContext)
"""
>>> setcontext(ExtendedContext)
>>> Decimal(1) / Decimal(0)
Decimal('Infinity')
>>> getcontext().traps[DivisionByZero] = 1
>>> Decimal(1) / Decimal(0)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in -toplevel-
    Decimal(1) / Decimal(0)
DivisionByZero: x / 0
"""

#算术对十进制对象和算术对整数和浮点数有一些小的差别。 当余数运算符 % 应用于Decimal对象时，结果的符号是 被除数 的符号，而不是除数的符号:
print((-7) % 4) #1
print(decimal.Decimal(-7) % decimal.Decimal(4)) # -3

#整数除法运算符 // 的行为类似，返回真商的整数部分（截断为零）而不是它的向下取整，以便保留通常的标识 x == (x // y) * y + x % y:
print(-7 // 4) # -2
print(decimal.Decimal(-7) // decimal.Decimal(4)) #-1

print(decimal.Decimal('-3.14').adjusted())