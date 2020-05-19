from abc import ABC, abstractmethod


class C(ABC):
    @property
    @abstractmethod
    def my_abstract_property(self):
        ...

from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    pass
