import random

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10) )  # sampling without replacement
print(random.random())
print(random.randrange(6) )   # random integer chosen from range(6)

print(random.randint(1,10)) # 函数返回数字 N ，N 为 a 到 b 之间的数字（a <= N <= b），包含 a 和 b。