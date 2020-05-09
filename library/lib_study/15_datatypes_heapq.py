# 堆队列算法  这个模块提供了堆队列算法的实现，也称为优先队列算法。
import heapq

h = []
heapq.heappush(h, 2)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
print(h)  # 有序的

print(heapq.heappop(h))  # 弹出并返回 heap 的最小的元素
print(h)

h1 = [3, 1, 2]
print(heapq.heappop(h1))  # 弹出并返回 heap 的最小的元素---其实就是弹出3，下标为0的
print(h1)

heapq.heappushpop(h, -1)
print(h)

heapq.heappushpop(h, 5)
print(h)

x = [7, 4, 5, 6]
heapq.heapify(x)  # 将list x 转换成堆，原地，线性时间内。
# 它使用了数组来实现：从零开始计数，对于所有的 k ，都有 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]。
print(x)
print(heapq.heappop(x))
print(heapq.heappop(x))
print(heapq.heappop(x))
print(heapq.heappop(x))

h2 = [3, 1, 2]
print(heapq.heapreplace(h2, -1))
print(h2)
print(heapq.heapreplace(h2, 5))
print(h2)
# heapreplace返回的值可能会比添加的 item 更大。 如果不希望如此，可考虑改用 heappushpop()。 它的 push/pop 组合会返回两个值中较小的一个，将较大的值留在堆中。
#  heapreplace先heappop() 再 heappush()
# heappushpop先调用  heappush() 再调用 heappop()
h3 = [3, 1, 2]
print(heapq.heappushpop(h3, -1))
print(h3)
print(heapq.heappushpop(h3, 5))
print(h3)

h8 = [1, 2, 3]
for i in heapq.merge([4, 5, 6], h8, ):
    print(i)

print(heapq.nlargest(2, [3, 1, 2]))

print(heapq.nsmallest(2, [3, 1, 2]))


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# 堆元素可以为元组。 这适用于将比较值（例如任务优先级）与跟踪的主记录进行赋值的场合:

h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(heapq.heappop(h))

import itertools

pq = []  # list of entries arranged in a heap
entry_finder = {}  # mapping of tasks to entries
REMOVED = '<removed-task>'  # placeholder for a removed task
counter = itertools.count()  # unique sequence count


def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)


def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

add_task(132,2)
add_task("xxxx",1)
print(pop_task())
