# https://docs.python.org/zh-cn/3/library/collections.abc.html
# collections.abc --- 容器的抽象基类
import collections

class ListBasedSet(collections.abc.Set):
    ''' Alternate set implementation favoring space over speed
        and not requiring the set elements to be hashable. '''
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')
for i in s1:
    print(i,end='')
print()
overlap = s1 & s2            # The __and__() method is supported automatically
for i in overlap:
    print(i,end='')



