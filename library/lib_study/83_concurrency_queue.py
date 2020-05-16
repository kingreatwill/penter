import queue

# 一旦达到这个大小，插入就会阻塞，直到使用队列项为止。如果maxsize小于或等于零，则队列大小为无穷大。
q = queue.Queue()  # 先进先出
q.put(1)
print(q.get())  # 当没有数据时会一直等待，直到超时

# collections.deque 是无界队列的一个替代实现，具有快速的不需要锁并且支持索引的原子化 append() 和 popleft() 操作。
sq = queue.SimpleQueue()  # 无界的 FIFO 队列

# 当达到这个大小的时候，插入操作将阻塞至队列中的项目被消费掉。如果 maxsize 小于等于零，队列尺寸为无限大。
lq = queue.LifoQueue()  # 后进先出

# 如果 data 元素没有可比性，数据将被包装在一个类中，忽略数据值，仅仅比较优先级数字 ：
pq = queue.PriorityQueue()  # 优先级队列

