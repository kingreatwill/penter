# 堆栈
stack = [3, 4, 5]
stack.append(6)
stack.append(6)
stack.pop()
stack.pop()
# 队列
stack.pop(0)
# 也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
# 在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。


# 队列可以用 collections
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
print(queue.popleft())

# 列表推导式(集合和字典推导也支持推导式：)

## 集合
vec = {2, 4, 6}
list_v = {3 * x for x in vec}
print(list_v)

# 字典
vec = {2, 4, 6}
list_v = { x :3 * x for x in vec}
print(list_v)

## 列表
vec = [2, 4, 6]
list_v = [3 * x for x in vec]
print(list_v)

var = [[x, x ** 2] for x in vec]
print(var)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
var = [weapon.strip() for weapon in freshfruit]
print(var)

var = [3 * x for x in vec if x > 3]
print(var)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec1 for y in vec2])
print([x + y for x in vec1 for y in vec2])
print([vec1[i] * vec2[i] for i in range(len(vec1))])

print([str(round(355 / 113, i)) for i in range(1, 9)])

# 嵌套列表解析

# 以下实例将3X4的矩阵列表转换为4X3列表：
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

# or
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
# or

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
