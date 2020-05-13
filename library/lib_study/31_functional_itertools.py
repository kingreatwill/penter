# 为高效循环而创建迭代器的函数
import itertools

# 创建一个迭代器，返回累积汇总值或其他双目运算函数的累积结果值
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(list(itertools.accumulate(data)))  # [3, 7, 13, 15, 16, 25, 25, 32, 37, 45]

# 创建一个迭代器，它首先返回第一个可迭代对象中所有元素，接着返回下一个可迭代对象中所有元素，直到耗尽所有可迭代对象中的元素。
c = itertools.chain(data, [10, 13, 12])
print(list(c))  # [3, 4, 6, 2, 1, 9, 0, 7, 5, 8, 10, 13, 12]

# 返回由输入 iterable 中元素组成长度为 r 的子序列。

print(list(itertools.combinations([1, 2, 3, 4, 5, 6],
                                  r=5)))  # [(1, 2, 3, 4, 5), (1, 2, 3, 4, 6), (1, 2, 3, 5, 6), (1, 2, 4, 5, 6), (1, 3, 4, 5, 6), (2, 3, 4, 5, 6)]

# 返回由输入 iterable 中元素组成的长度为 r 的子序列，允许每个元素可重复出现。
print(list(itertools.combinations_with_replacement([1, 2, 3, 4, 5, 6], r=5)))

# 创建一个迭代器，它返回 data 中经 selectors 真值测试为 True 的元素。

print(list(itertools.compress([1, 2, 3, 4, 5], [True, 0, 1])))  # [1, 3]

# 创建一个迭代器，它从 start 值开始，返回均匀间隔的值。 停不下来的循环
# for i in itertools.count(10):
#     print(i)


# 创建一个迭代器，返回 iterable 中所有元素并保存一个副本。当取完 iterable 中所有元素，返回副本中的所有元素。无限重复。停不下来的循环
#
# for i in itertools.cycle([1,2,3]):
#     print(i)


# 创建一个迭代器，如果 predicate 为true，迭代器丢弃这些元素，然后返回其他元素。注意，迭代器在 predicate 首次为false之前不会产生任何输出，所以可能需要一定长度的启动时间。
print(list(itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))  # [6, 4, 1]

# 创建一个迭代器，只返回 iterable 中 predicate 为 False 的元素。如果 predicate 是 None，返回真值测试为false的元素。
print(list(itertools.filterfalse(lambda x: x % 2, range(10))))  # [0, 2, 4, 6, 8]

# 创建一个迭代器，返回 iterable 中连续的键和组。key 是一个计算元素键值函数。如果未指定或为 None，key 缺省为恒等函数（identity function），返回元素不变。
# 需要先排序
print(list(itertools.groupby([1, 11, 2, 22, 3, 3, 33])))
from operator import itemgetter
from itertools import groupby

students = [
    {'name': 'Peter', 'age': 19, 'score': 95},
    {'name': 'Lily', 'age': 22, 'score': 90},
    {'name': 'Stanley', 'age': 22, 'score': 92},
    {'name': 'Bob', 'age': 20, 'score': 88},
    {'name': 'Well', 'age': 20, 'score': 82}
]
for key, group in groupby(sorted(students, key=itemgetter("age")), key=itemgetter("age")):
    # groupby()函数同时返回分组关键字和一个与关键字相对应的可迭代对象
    # itemgetter()同样可以接收多个关键字，也可以使用匿名函数代替此函数，但速度相比之下较慢
    print("Age: %s" % key)
    for g in group:
        print(g)

# 创建一个迭代器，返回从 iterable 里选中的元素。如果 start 不是0，跳过 iterable 中的元素，直到到达 start 这个位置。
# 之后迭代器连续返回元素，除非 step 设置的值很高导致被跳过。
# 如果 stop 为 None，迭代器耗光为止；否则，在指定的位置停止。与普通的切片不同，islice() 不支持将 start ， stop ，或 step 设为负值。
# 可用来从内部数据结构被压平的数据中提取相关字段（例如一个多行报告，它的名称字段出现在每三行上）。
print(list(itertools.islice('ABCDEFG', 2)))  # ['A', 'B']
print(list(itertools.islice('ABCDEFG', 2, 4)))  # ['C', 'D']
print(list(itertools.islice('ABCDEFG', 2, None)))  # ['C', 'D', 'E', 'F', 'G']
print(list(itertools.islice('ABCDEFG', 0, None, 2)))  # ['A', 'C', 'E', 'G']

# 连续返回由 iterable 元素生成长度为 r 的排列。
# 如果 r 未指定或为 None ，r 默认设置为 iterable 的长度，这种情况下，生成所有全长排列。
# 排列依字典序发出。因此，如果 iterable 是已排序的，排列元组将有序地产出。
# 即使元素的值相同，不同位置的元素也被认为是不同的。如果元素值都不同，每个排列中的元素值不会重复。
print(list(itertools.permutations('ABCD', 2)))
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
print(list(itertools.permutations(range(3))))
# [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

# 可迭代对象输入的笛卡儿积。
# 大致相当于生成器表达式中的嵌套循环。例如， product(A, B) 和 ((x,y) for x in A for y in B) 返回结果一样。
# 嵌套循环像里程表那样循环变动，每次迭代时将最右侧的元素向后迭代。这种模式形成了一种字典序，因此如果输入的可迭代对象是已排序的，笛卡尔积元组依次序发出。
# 要计算可迭代对象自身的笛卡尔积，将可选参数 repeat 设定为要重复的次数。例如，product(A, repeat=4) 和 product(A, A, A, A) 是一样的。
print(list(itertools.product('ABCD', 'xy')))
# [('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), ('C', 'x'), ('C', 'y'), ('D', 'x'), ('D', 'y')]
print(list(itertools.product(range(2), repeat=3)))
# [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

# 创建一个迭代器，不断重复 object 。除非设定参数 times ，否则将无限重复。
print(list(itertools.repeat(10, 3)))  # [10, 10, 10]
# print(list(itertools.repeat(10))) 无限循环

# 创建一个迭代器，使用从可迭代对象中获取的参数来计算该函数。
print(list(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)])))  # [32, 9, 1000]

# 创建一个迭代器，只要 predicate 为真就从可迭代对象中返回元素。
print(list(itertools.takewhile(lambda x: x < 5, [1, 4, 6, 3, 2])))  # [1, 4]

# 从一个可迭代对象中返回 n 个独立的迭代器。 tee 迭代器不是线程安全的
for i in itertools.tee([1, 2, 3]):
    print(list(i))
# 输出两个[1, 2, 3]

# 创建一个迭代器，从每个可迭代对象中收集元素。如果可迭代对象的长度未对齐，将根据 fillvalue 填充缺失值。迭代持续到耗光最长的可迭代对象。
print(list(itertools.zip_longest('ABCD', 'xy', fillvalue='-')))
# [('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')]





# pip install more-itertools https://github.com/more-itertools/more-itertools
