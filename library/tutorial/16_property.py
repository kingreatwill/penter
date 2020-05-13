# 调用私有方法
class Kls():
    def public_f(self):
        print("public def")

    def __private_f(self):
        print("__private_f def")


k = Kls()
k._Kls__private_f()  # 可以调用私有方法;


class Student(object):
    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 90
print(s.score)  # 90
s.score = 100
print(s.score)  # 100
print(s._score)  # 100


class A:
    i = 100

    def print1(self):
        print("11111")

    @staticmethod
    def print2():
        print("222")

    @classmethod
    def print3(cls):
        print(cls.i)
        obj = cls.__new__(cls)
        obj.print1()


A.print1(0)  # 11111 可以调用
A.print1(A())  # 11111 可以调用

A.print3() ## 100

A().print2()  # 222
A().print1()  # 11111
a1 = A()
print(A.i)  # 100
A.i += 1
A.print3() ## 101
print(A.i)  # 101
print(a1.i)  # 101
a2 = A()
print(a2.i)  # 101
a1.i += 1
print(A.i)  # 101
print(a1.i)  # 102

A.i += 5
print(A.i)  # 106
print(a1.i)  # 102
print(a2.i)  # 106


class A2:
    i = 10

    def __init__(self):
        self.i = A2.i

    def print1(self):
        print(self.i)

    @staticmethod
    def print2():
        print(A2.i)


A2.print2()  # 10
a21 = A2()
a21.print1()  # 10
A2.i += 1
A2.print2()  # 11
a22 = A2()
a22.print1()  # 11
a21.print1()  # 10
print(a21.i)  # 10
