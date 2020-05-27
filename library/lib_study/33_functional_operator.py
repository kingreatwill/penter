import operator

# 标准运算符替代函数
# 更多参考：https://docs.python.org/zh-cn/3/library/operator.html

# a<b
print(operator.lt(1, 2))

"""
operator.attrgetter(attr)¶
operator.attrgetter(*attrs)
返回一个可从操作数中获取 attr 的可调用对象。 如果请求了一个以上的属性，则返回一个属性元组。 属性名称还可包含点号。 例如：

在 f = attrgetter('name') 之后，调用 f(b) 将返回 b.name。

在 f = attrgetter('name', 'date') 之后，调用 f(b) 将返回 (b.name, b.date)。

在 f = attrgetter('name.first', 'name.last') 之后，调用 f(b) 将返回 (b.name.first, b.name.last)。


operator.itemgetter(item)
operator.itemgetter(*items)
返回一个使用操作数的 __getitem__() 方法从操作数中获取 item 的可调用对象。 如果指定了多个条目，则返回一个查找值的元组。 例如：

在 f = itemgetter(2) 之后，调用 f(r) 将返回 r[2]。

在 g = itemgetter(2, 5, 3) 之后，调用 g(r) 将返回 (r[2], r[5], r[3])。



operator.methodcaller(name, /, *args, **kwargs)
返回一个在操作数上调用 name 方法的可调用对象。 如果给出额外的参数和/或关键字参数，它们也将被传给该方法。 例如：

在 f = methodcaller('name') 之后，调用 f(b) 将返回 b.name()。

在 f = methodcaller('name', 'foo', bar=1) 之后，调用 f(b) 将返回 b.name('foo', bar=1)。
"""
