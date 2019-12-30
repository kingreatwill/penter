import random

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10) )  # sampling without replacement
print(random.random())
print(random.randrange(6) )   # random integer chosen from range(6)