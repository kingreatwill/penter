print("------------class enum.Enum")
from enum import Enum, unique, auto


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(type(Color.RED))
print(isinstance(Color.GREEN, Color))  # True
print(repr(Color.RED))
print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)
print(Color.RED == 1)  # False
print(Color(1))
print(Color(1) == Color.RED)  # True
print(Color['RED'])
print(Color['RED'] == Color.RED)  # True


# 枚举支持按照定义顺序进行迭代:
# @unique 加上这个就报错，因为VANILLA跟VANILLA_2重复了
class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3
    VANILLA_2 = 7
    AUTO = auto()
    AUTO2 = auto()


print(Shake.AUTO.value)  # 8
print(Shake.AUTO2.value)  # 9 注意了，auto为上一个值+1,初始值从 1 开始

print(Shake.VANILLA_2)  # Shake.VANILLA
for shake in Shake:
    print(shake)

Animal = Enum('Animal', 'ANT BEE CAT DOG')
print(list(Animal))

print("------------")


# 值将由 _generate_next_value_() 来选择，该函数可以被重载:
class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


print(Ordinal.EAST.value)  # EAST 不是数字哦

print(list(Ordinal))

print("--------------------迭代")

for o in Ordinal:
    print(o)

for name, member in Shake.__members__.items():
    print(name, member)
# 找出所有别名:
print([name for name, member in Shake.__members__.items() if member.name != name])
print("--------------------比较")
print(isinstance(Color.RED, Color))  # True
print(Color.RED is Color)  # False
print(Color.RED is Color.RED)  # True
print(Color.RED is Color.BLUE)  # False
print(Color.RED is not Color.BLUE)  # True
print(Color.RED != Color.BLUE)  # True
print(Color.RED == 1)  # False

print("----------允许的枚举成员和属性")


class Mood(Enum):
    FUNKY = 1
    HAPPY = 3

    def describe(self):
        # self is the member here
        return self.name, self.value

    def __str__(self):
        return 'my custom str! {0}'.format(self.value)

    @classmethod
    def favorite_mood(cls):
        # cls here is the enumeration
        return cls.HAPPY


class Foo1(Enum):
    HAPPY1 = 1


class Foo2(Enum):
    def some_behavior(self):
        pass


# class Bar1(Foo1): # 不允许
#     HAPPY2 = 2
#     HAPPY3 = 3

class Bar2(Foo2):
    HAPPY2 = 2
    HAPPY3 = 3


print("---------------枚举可以被封存与解封: 通过在枚举类中定义 __reduce_ex__() 可以对 Enum 成员的封存/解封方式进行修改。")
from test.test_enum import Fruit
from pickle import dumps, loads

print(Fruit.TOMATO is loads(dumps(Fruit.TOMATO)))  # true

print("------")
import sys

Animal1 = Enum('Animal', 'ANT BEE CAT DOG', module=__name__)  # 指定模块名字
Animal2 = Enum('Animal', 'ANT BEE CAT DOG', module=sys)  # 指定模块名字

print("-------------IntEnum")

from enum import IntEnum


class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2


class Request(IntEnum):
    POST = 1
    GET = 2


print(Shape == 1)  # False
print(Shape.CIRCLE == 1)  # True
print(Shape.CIRCLE == Request.POST)  # True
print(['a', 'b', 'c'][Shape.CIRCLE])

print("------------------IntFlag")
from enum import IntFlag


class Perm(IntFlag):
    R = 4
    W = 2
    X = 1


print(Perm.R | Perm.W)

print(Perm.R + Perm.W) # 6

RW = Perm.R | Perm.W
print(Perm.R in RW) # True

print(4&1) # 0
print(Perm.R & Perm.X) # Perm.0
print(bool(Perm.R & Perm.X)) # False     IntFlag 和 Enum 的另一个重要区别在于如果没有设置任何旗标（值为 0），则其布尔值为 False:



class Perm2(IntFlag):
    R = 4
    W = 2
    X = 1
    RWX = 7
print(Perm2.RWX)

print(~Perm2.RWX)

print("--------------Flag  对于大多数新代码，强烈推荐使用 Enum 和 Flag")

from enum import Flag, auto
class Color(Flag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

print(Color.RED & Color.GREEN) # Color.0

print(bool(Color.RED & Color.GREEN)) # False  # 与 IntFlag 类似，如果 Flag 成员的某种组合导致没有设置任何旗标，则其布尔值为 False:

class Color(Flag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    WHITE = RED | BLUE | GREEN

print(Color.WHITE) #Color.WHITE


print("---------------")
class Coordinate(bytes, Enum):
    """
    Coordinate with binary codes that can be indexed by the int code.
    """
    def __new__(cls, value, label, unit):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        obj.unit = unit
        return obj
    PX = (0, 'P.X', 'km')
    PY = (1, 'P.Y', 'km')
    VX = (2, 'V.X', 'km/s')
    VY = (3, 'V.Y', 'km/s')


print(Coordinate['PY'])

print(Coordinate(3))
# 当你想要定制 Enum 成员的实际值时必须使用 __new__()。 任何其他修改可以用 __new__() 也可以用 __init__()，应优先使用 __init__()。




class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

class Grade(OrderedEnum):
    A = 5
    B = 4
    C = 3
    D = 2
    F = 1

print(Grade.C < Grade.A)





class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27,   7.1492e7)
    SATURN  = (5.688e+26, 6.0268e7)
    URANUS  = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)
    def __init__(self, mass, radius):
        self.mass = mass       # in kilograms
        self.radius = radius   # in meters
    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)

print(Planet.EARTH.value)

print(Planet.EARTH.surface_gravity)



from datetime import timedelta
class Period(timedelta, Enum):
    "different lengths of time"
    _ignore_ = 'Period i'
    Period = vars()
    for i in range(367):
        Period['day_%d' % i] = i

print(list(Period)[:2])

print(list(Period)[-2:])



