

a, b = 0, 1
while b < 20:
    print(b, end=',')
    a, b = b, a+b
print("--------")
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))



basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


def Merge(dict1, dict2):
    return (dict2.update(dict1))


# 两个字典
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# 返回  None
print(Merge(dict1, dict2))

# dict2 合并了 dict1
print(dict2)


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


# 两个字典
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)