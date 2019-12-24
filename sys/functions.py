
def test2():
    i = 1
    # 此函数会在调用时将你陷入调试器中
    breakpoint()

def test1():
    print(abs(-123))
    # string，list，tuple，dict，file，xrange都是可迭代的，都属于iterable对象，可迭代的对象都是可以遍历的
    print(all([False,2,3]))
    print(any([False,2,False]))
    print(ascii("ASCII 编码"))
    print(bin(14))
    # 如果不一定需要前缀“0b”，还可以使用如下的方法。
    print(format(14, '#b'))
    print(format(14, 'b'))
    print(bool(0))


test1()