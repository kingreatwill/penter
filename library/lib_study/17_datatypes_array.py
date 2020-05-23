# 高效的数值数组
import array

# https://docs.python.org/zh-cn/3/library/array.html
"""
python中的list是python的内置数据类型，list中的数据类不必相同的，而array的中的类型必须全部相同。
在list中的数据类型保存的是数据的存放的地址，简单的说就是指针，并非数据，这样保存一个list就太麻烦了，
例如list1=[1,2,3,'a']需要4个指针和四个数据，增加了存储和消耗cpu。
numpy中封装的array有很强大的功能，里面存放的都是相同的数据类型

计算机为数组分配一段连续的内存，从而支持对数组随机访问；
由于项的地址在编号上是连续的，数组某一项的地址可以通过将两个值相加得出，即将数组的基本地址和项的偏移地址相加。
数组的基本地址就是数组的第一项的机器地址。一个项的偏移地址就等于它的索引乘以数组的一个项所需要的内存单元数目的一个常量表示（在python中，这个值总是1）

关于动态数组（高效率的随机访问）的实现，题主可以参考 C++ 中 std::vector。
简单来说与 @rushcheyo 的说法类似，初始时系统会分配一块内存，每当数组中的元素个数达到上限时，
就会再次分配一块更大的内存（增加的速率由算法决定），然后将原有的元素移动到新分配的内存中去（当然如果数组的元素类型不支持移动构造函数（move constructor），则会拷贝数组中的元素到新内存中）。
其实现效率并不低。另外 C++11 中引入了右值引用（rvalue reference）可以有效的减少在移动数组时拷贝的发生。

需要注意的是 std::vector 对于在数组中间的插入/删除操作是相对低效率的（一般情况下仍然可以接受），它会移动被插入/删除元素后面的所有元素。

对于 Python 中的 List，根据官方文档可知，也是按照类似的方法进行设计的。根据这篇博文，在 Python 最常见实现的 CPython 中，List 是通过一个变长数组实现的，数组的元素是指向 List 中元素的指针。

Python的实现：
[https://github.com/python/cpython/blob/master/Include/listobject.h#L23-L40]
[https://github.com/python/cpython/blob/master/Objects/listobject.c]
Python里面内置List的实现方式很简单，就是一个指针数组，分配在堆上，加一个allocated字段保存指针数组当前已经分配的内存数和一个ob_size字段保存当前已经占用的内存数。
Python中List操作若涉及长度变化就会判断当前List已经分配的内存数是否足够，如果不够就realloc重新分配内存，够了就直接用已经分配的内存。
"""
print(array.typecodes) # 包含所有可用类型码的字符串。

a = array.array('f')
a.append(1)
print(a)

a = array.array('B') # 0-255
a.append(255)
a.append(250)
print(a)

for a1 in a:
    print(a1)

print(a[1])

print(a.typecode)
print(a.itemsize)

"""
array('l')
array('u', 'hello \u2641')
array('l', [1, 2, 3, 4, 5])
array('d', [1.0, 2.0, 3.14])
"""



