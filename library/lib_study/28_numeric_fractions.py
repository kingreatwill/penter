print("---------------分数")
from fractions import Fraction

print(Fraction(16, -10))  # -8/5

print(Fraction(123))  # 123

print(Fraction())  # 0

print(Fraction('3/7'))  # 3/7

print(Fraction(' -3/7 '))  # -3/7

print(Fraction('1.414213 \t\n'))  # 1414213/1000000

print(Fraction('-.125'))  # -1/8

print(Fraction('7e-6'))  # 7/1000000

print(Fraction(2.25))  # 9/4

print(Fraction(1.1))  # 2476979795053773/2251799813685248

from decimal import Decimal

print(Fraction(Decimal('1.1')))  # 11/10

print(Fraction(1.1).numerator)  # 2476979795053773 最简分数形式的分子。
print(Fraction(1.1).denominator)  # 2251799813685248 最简分数形式的分母。
# print(Fraction(1.1).as_integer_ratio()) #(2476979795053773, 2251799813685248) 3.8 新版功能. 返回由两个整数组成的元组，两数之比等于该分数的值且其分母为正数。


print(Fraction.from_float(0.3))  # 5404319552844595/18014398509481984 此类方法可构造一个 Fraction 来表示 flt 的精确值，该参数必须是一个 float
print(Fraction(0.3))  # 5404319552844595/18014398509481984
print(Fraction(3 / 10))  # 5404319552844595/18014398509481984
print(Fraction(3, 10))  # 3/10
print(Fraction('3.1415926535897932').limit_denominator(
    1000))  # 找到并返回一个 Fraction 使得其值最接近 self 并且分母不大于 max_denominator。 此方法适用于找出给定浮点数的有理数近似值：
