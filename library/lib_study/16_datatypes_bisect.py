# 数组二分查找算法
import bisect

# bisect_left(a, x, lo=0, hi=len(a)如果 x 已经在 a 里存在，那么插入点会在已存在元素之前（也就是左边）。如果 a 是列表（list）的话，返回值是可以被放在 list.insert() 的第一个参数的
print(bisect.bisect_left([1, 2, 3, 4, 5, 6], 2))
print(bisect.bisect_right([1, 2, 3, 4, 5, 6], 2))
print(bisect.bisect([1, 2, 3, 4, 5, 6], 2))

h = [1, 2, 3, 4, 5, 6]
bisect.insort_left(h, 2)  # a.insert(bisect.bisect_left(a, x, lo, hi), x)。要注意搜索是 O(log n) 的，插入却是 O(n) 的。
print(h)

bisect.insort_right(h, 2)
bisect.insort(h, 2)


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
