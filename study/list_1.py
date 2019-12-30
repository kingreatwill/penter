a = [66.25, 333, 333, 1, 1234.5]
# 出现次数
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
print(a)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
b = a.copy()
print(b)
b.clear() #del b[:] # del b  是删除变量
print("----")
print(a)
print(b)
b.extend(a) # 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
print(b)
# 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。
# （方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
print(b.pop())
print(b.pop(1))
print(b)
