n = int(input("请输入一个整数"))
s = "*"
for i in range(1, n, 2):
    print((s*i).center(n))
for i in reversed(range(1, n-2,2)):
    print((s * i).center(n))
