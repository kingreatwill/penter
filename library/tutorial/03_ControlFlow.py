# if elif else
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# for
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# 在遍历同一个集合时修改该集合的代码
"""
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
"""

# break continue
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


"""
while 和 if 条件句中可以使用任意操作，而不仅仅是比较操作。

比较操作符 in 和 not in 校验一个值是否在（或不在）一个序列里。操作符 is 和 is not 比较两个对象是不是同一个对象，这只对像列表这样的可变对象比较重要。所有的比较操作符都有相同的优先级，且这个优先级比数值运算符低。

比较操作可以传递。例如 a < b == c 会校验是否 a 小于 b 并且 b 等于 c。

比较操作可以通过布尔运算符 and 和 or 来组合，并且比较操作（或其他任何布尔运算）的结果都可以用 not 来取反。
这些操作符的优先级低于比较操作符；在它们之中，not 优先级最高， or 优先级最低，因此 A and not B or C 等价于 (A and (not B)) or C。和之前一样，你也可以在这种式子里使用圆括号。
"""
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

# pass占位符
# pass 语句什么也不做。当语法上需要一个语句，但程序需要什么动作也不做时，可以使用它
