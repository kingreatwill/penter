# 1. 重复元素判定
def all_unique(lst):
    return len(lst) == len(set(lst))


# 2. 字符元素组成判定
def anagram(first, second):
    from collections import Counter
    return Counter(first) == Counter(second)


# 3. 内存占用
def sizeof(obj):
    import sys
    return sys.getsizeof(obj)


# 4. 字节占用
def byte_size(string):
    return (len(string.encode('utf-8')))


# 分块
def chunk(lst, size):
    from math import ceil
    return list(map(lambda x: lst[x * size:x * size + size], list(range(0, ceil(len(lst) / size)))))


# 压缩
def compact(lst):
    return list(filter(bool, lst))


# 首字母小写
def decapitalize(string):
    return string[:1].lower() + string[1:]


# 展开列表
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


# 展开列表
def deep_flatten(lst):
    result = []
    result.extend(spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result


# 列表的差 该方法将返回第一个列表的元素，其不在第二个列表内。如果同时要反馈第二个列表独有的元素，还需要加一句 set_b.difference(set_a)。
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


# 通过函数取差
def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


# 回文序列
def palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]


if __name__ == '__main__':
    # 1. 重复元素判定
    x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5]
    print(all_unique(x))  # false
    print(all_unique(y))  # true
    # 2. 字符元素组成判定
    print(anagram("abcd3", "3acdb"))  # true
    # 3. 内存占用
    variable = 30
    print(sizeof(variable))
    # 4. 字节占用
    print(byte_size(''))  # 0
    print(byte_size('Hello World'))  # 11
    # 大写第一个字母
    s = "programming is awesome"
    print(s.title())  # Programming Is Awesome
    # 分块 给定具体的大小，定义一个函数以按照这个大小切割列表。
    print(chunk([1, 2, 3, 4, 5], 2))  # [[1,2],[3,4],[5]]

    # 压缩 这个方法可以将布尔型的值去掉，例如（False，None，0，“”），它使用 filter() 函数。
    print(compact([0, 1, False, 2, '', 3, 'a', 's', 34]))  # [ 1, 2, 3, 'a', 's', 34 ]
    # 链式对比
    a = 3
    print(2 < a < 8)  # True
    print(1 == a < 2)  # False
    # 首字母小写
    print(decapitalize('FooBar'))
    # 展开列表
    print(deep_flatten([1, [2], [[3], 4], 5]))  # [1,2,3,4,5]

    # 列表的差
    print(difference([1, 2, 3], [1, 2, 4]))  # [3]

    # 通过函数取差 如下方法首先会应用一个给定的函数，然后再返回应用函数后结果有差别的列表元素。
    from math import floor

    print(difference_by([2.1, 1.2], [2.3, 3.4], floor))  # [1.2]
    print(difference_by([{'x': 2}, {'x': 1}], [{'x': 1}], lambda v: v['x']))  # [ { x: 2 } ]


    # 链式函数调用
    def add(a, b):
        return a + b


    def subtract(a, b):
        return a - b


    a, b = 4, 5
    print((subtract if a > b else add)(a, b))  # 9

    # 合并两个字典

    a = {'x': 1, 'y': 2}
    b = {'y': 3, 'z': 4}
    print({**a, **b})  # {'x': 1, 'y': 3, 'z': 4}
    # 将两个列表转化为字典
    keys = ["a", "b", "c"]
    values = [2, 3, 4]
    print(dict(zip(keys, values)))  # {'a': 2, 'c': 4, 'b': 3}

    # 循环列表索引
    list2 = ["a", "b", "c", "d"]
    for index, element in enumerate(list2):
        print("Value", element, "Index ", index, )

    # start_time = time.time()
    # ...
    # end_time = time.time()
    # total_time = end_time - start_time
    # print("Time: ", total_time)# ('Time: ', 1.1205673217773438e-05)

    # 下面的方法会根据元素频率取列表中最常见的元素
    list3 = [1, 2, 1, 2, 3, 2, 1, 4, 2]
    print(max(set(list3), key=list3.count))  # 2

    # 回文序列
    print(palindrome('tacocat'))  # True

    # 不使用 if-else 的计算子
    import operator

    action = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul, "**": pow}
    print(action['-'](50, 25))  # 25

    # 打乱列表元素的顺序
    from copy import deepcopy
    from random import randint

    # 可能跟原序列相同
    def shuffle(lst):
        temp_lst = deepcopy(lst)
        m = len(temp_lst)
        while (m):
            m -= 1
            i = randint(0, m)
            temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
        return temp_lst


    foo = [1, 2, 3]
    print(shuffle(foo))  # [2,3,1] , foo = [1,2,3]
