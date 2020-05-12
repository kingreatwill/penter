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
print(s.score) # 90
s.score = 100
print(s.score)

