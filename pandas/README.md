https://www.pypandas.cn/
https://pandas.pydata.org/


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