x = 10 * 3.25
y = 200 * 200
print(repr((x, y, ('Google', 'Runoob'))))
print(str((x, y, ('Google', 'Runoob'))))
hello = 'hello, runoob\n'
print(hello)
print(repr(hello))

# 输出一个平方与立方的表:
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))