import sys

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
print (next(it))   # 输出迭代器的下一个元素
# 迭代器对象可以使用常规for语句进行遍历
for x in iter(list):
    print (x, end=",")

print()
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

