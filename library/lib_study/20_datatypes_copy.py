import copy

origin = [1, 2, [3, 4]]

cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)

origin[2][0] = "hey!"
print(cop1)
print(cop2)

a = [1, 2, 3]
b = a
a = [4, 5, 6]  # 赋新的值给 a
print(a)  # [4, 5, 6]

print(b)  # [1, 2, 3] # a 的值改变后，b 并没有随着 a 变
a = [1, 2, 3]
b = a
a[0], a[1], a[2] = 4, 5, 6  # 改变原来list中的元素
print(a)  # [4, 5, 6]

print(b)  # [4, 5, 6] # a 的值改变后，b 随着 a 变了
