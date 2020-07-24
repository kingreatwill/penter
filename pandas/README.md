https://www.pypandas.cn/
https://pandas.pydata.org/
https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-1-pd-intro/

```
NumPy：N维数组容器

SciPy：科学计算函数库

Pandas：表格容器

非数学研究,建议直接入手pandas,包含基础的Numpy方法

Pandas:
基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。
Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。最具有统计意味的工具包，某些方面优于R软件。
数据结构有一维的Series，二维的DataFrame(类似于Excel或者SQL中的表，如果深入学习，会发现Pandas和SQL相似的地方很多，例如merge函数)，
三维的Panel（Pan（el) + da(ta) + s，知道名字的由来了吧）。

学习Pandas你要掌握的是：
1.汇总和计算描述统计，处理缺失数据 ，层次化索引
2.清理、转换、合并、重塑、GroupBy技术
3.日期和时间数据类型及工具（日期处理方便地飞起）


```

## Pandas是什么？

Pandas是一个强大的分析结构化数据的工具集；它的使用基础是Numpy（提供高性能的矩阵运算）；用于数据挖掘和数据分析，同时也提供数据清洗功能。

## 利器之一：DataFrame

DataFrame是Pandas中的一个表格型的数据结构，包含有一组有序的列，每列可以是不同的值类型(数值、字符串、布尔型等)，DataFrame即有行索引也有列索引，可以被看做是由Series组成的字典。

## 利器之一：Series

它是一种类似于一维数组的对象，是由一组数据(各种NumPy数据类型)以及一组与之相关的数据标签(即索引)组成。仅由一组数据也可产生简单的Series对象。

## 分布式计算框架

https://github.com/uber/fiber

https://github.com/mars-project/mars
Mars是由阿里云高级软件工程师秦续业等人开发的一个基于张量的大规模数据计算的统一框架，目前它已在GitHub上开源。
该工具能用于多个工作站，而且即使在单块CPU的情况下，它的矩阵运算速度也比NumPy(MKL)快。


https://github.com/databricks/koalas


https://github.com/dask/dask
关于Python性能的一个常见抱怨是全局解释器锁(GIL)。由于GIL，同一时刻只能有一个线程执行Python字节码。因此，即使在现代的多核机器上，使用线程也不会加速计算。
但当你需要并行化到多核时，你不需要放弃使用Python，Dask库可以将计算扩展到多个内核甚至多个机器。某些设置可以在数千台机器上配置Dask，每台机器都有多个内核。

https://github.com/vaexio/vaex
Vaex是一个开源的DataFrame库(类似于Pandas)，对和你硬盘空间一样大小的表格数据集，它可以有效进行可视化、探索、分析甚至进行实践机器学习。

它可以在N维网格上计算每秒超过十亿(10^9)个对象/行的统计信息，例如均值、总和、计数、标准差等。使用直方图、密度图和三维体绘制完成可视化，从而可以交互式探索大数据。
Vaex使用内存映射、零内存复制策略获得最佳性能(不浪费内存)。

为实现这些功能，Vaex 采用内存映射、高效的核外算法和延迟计算等概念。所有这些都封装为类Pandas的API，因此，任何人都能快速上手。



https://github.com/cupy/cupy
CuPy是一个借助CUDA GPU库在英伟达GPU上实现Numpy数组的库。基于Numpy数组的实现，GPU自身具有的多个CUDA核心可以促成更好的并行加速。
CuPy接口是Numpy 的一个镜像，并且在大多情况下，它可以直接替换Numpy使用。只要用兼容的CuPy代码替换Numpy代码，用户就可以实现 GPU 加速。
CuPy支持Numpy的大多数数组运算，包括索引、广播、数组数学以及各种矩阵变换。


http://docs.cython.org/en/latest/
Cython是结合了Python和C的语法的一种语言，可以简单的认为就是给Python加上了静态类型后的语法，使用者可以维持大部分的Python语法，
而不需要大幅度调整主要的程式逻辑与算法。但由于会直接编译为二进制程序，所以性能较Python会有很大提升。
```
pip install Cython

from cpython cimport array
import array
cdef array.array a = array.array('i', [1, 2, 3])
cdef int[:] ca = a
print(ca[0])
```


https://github.com/ray-project/ray