# if 1900 < year < 2100 and 1 <= month <= 12 \
#    and 1 <= day <= 31 and 0 <= hour < 24 \
#    and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
#         return 1

"""
object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)


object.__radd__(self, other)
object.__rsub__(self, other)
object.__rmul__(self, other)
object.__rmatmul__(self, other)
object.__rtruediv__(self, other)
object.__rfloordiv__(self, other)
object.__rmod__(self, other)
object.__rdivmod__(self, other)
object.__rpow__(self, other[, modulo])
object.__rlshift__(self, other)
object.__rrshift__(self, other)
object.__rand__(self, other)
object.__rxor__(self, other)
object.__ror__(self, other)
调用这些方法来实现具有反射（交换）操作数的二进制算术运算 (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |)。这些成员函数仅会在左操作数不支持相应运算 3 且两个操作数类型不同时被调用。4 例如，求表达式 x - y 的值，其中 y 是具有 __rsub__() 方法的类的一个实例，则当 x.__sub__(y) 返回 NotImplemented 时会调用 y.__rsub__(x)。

请注意三元版的 pow() 并不会尝试调用 __rpow__() (因为强制转换规则会太过复杂)。

注解 如果右操作数类型为左操作数类型的一个子类，且该子类提供了指定运算的反射方法，则此方法会先于左操作数的非反射方法被调用。此行为可允许子类重载其祖先类的运算符。
object.__iadd__(self, other)
object.__isub__(self, other)
object.__imul__(self, other)
object.__imatmul__(self, other)
object.__itruediv__(self, other)
object.__ifloordiv__(self, other)
object.__imod__(self, other)
object.__ipow__(self, other[, modulo])
object.__ilshift__(self, other)
object.__irshift__(self, other)
object.__iand__(self, other)
object.__ixor__(self, other)
object.__ior__(self, other)
调用这些方法来实现扩展算术赋值 (+=, -=, *=, @=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=)。这些方法应该尝试进行自身操作 (修改 self) 并返回结果 (结果应该但并非必须为 self)。如果某个方法未被定义，相应的扩展算术赋值将回退到普通方法。例如，如果 x 是具有 __iadd__() 方法的类的一个实例，则 x += y 就等价于 x = x.__iadd__(y)。否则就如 x + y 的求值一样选择 x.__add__(y) 和 y.__radd__(x)。在某些情况下，扩展赋值可导致未预期的错误 (参见 为什么 a_tuple[i] += ['item'] 会在执行加法时引发异常？)，但此行为实际上是数据模型的一个组成部分。

object.__neg__(self)
object.__pos__(self)
object.__abs__(self)
object.__invert__(self)
调用此方法以实现一元算术运算 (-, +, abs() 和 ~)。

object.__complex__(self)
object.__int__(self)
object.__float__(self)
调用这些方法以实现内置函数 complex(), int() 和 float()。应当返回一个相应类型的值。

object.__index__(self)
调用此方法以实现 operator.index() 以及 Python 需要无损地将数字对象转换为整数对象的场合（例如切片或是内置的 bin(), hex() 和 oct() 函数)。 存在此方法表明数字对象属于整数类型。 必须返回一个整数。

如果未定义 __int__(), __float__() 和 __complex__() 则相应的内置函数 int(), float() 和 complex() 将回退为 __index__()。

object.__round__(self[, ndigits])
object.__trunc__(self)
object.__floor__(self)
object.__ceil__(self)
调用这些方法以实现内置函数 round() 以及 math 函数 trunc(), floor() 和 ceil()。 除了将 ndigits 传给 __round__() 的情况之外这些方法的返回值都应当是原对象截断为 Integral (通常为 int)。

如果未定义 __int__() 则内置函数 int() 会回退到 __trunc__()。
"""