CPython（标准的python实现）有一个名为GIL（全局解释器锁）的东西，它阻止两个线程在同一个程序中同时执行。
有些人对此感到不安，而其他人则狠狠地为此辩护。
但是，有一些解决方法，像Numpy这样的库通过在C中运行外部代码来绕过这个限制。

## 何时使用线程与进程？
- 进程加速了CPU密集型的Python操作，因为它们受益于多个内核并避免使用GIL。
- 线程最适合IO任务或涉及外部系统的任务，因为线程可以更有效地组合他们的工作。 进程需要挑选他们的结果来组合它们需要时间。

# Python的GIL是什么鬼，多线程性能究竟如何 http://cenalulu.github.io/python/gil-in-python/
# Python GIL全局解释器锁详解（深度剖析）  http://c.biancheng.net/view/5537.html

GIL是什么

首先需要明确的一点是GIL并不是Python的特性，它是在实现Python解析器(CPython)时所引入的一个概念。就好比C++是一套语言（语法）标准，但是可以用不同的编译器来编译成可执行代码。
有名的编译器例如GCC，INTEL C++，Visual C++等。Python也一样，同样一段代码可以通过CPython，PyPy，Psyco等不同的Python执行环境来执行。像其中的JPython就没有GIL。
然而因为CPython是大部分环境下默认的Python执行环境。所以在很多人的概念里CPython就是Python，也就想当然的把GIL归结为Python语言的缺陷。
所以这里要先明确一点：GIL并不是Python的特性，Python完全可以不依赖于GIL

那么CPython实现中的GIL又是什么呢？GIL全称Global Interpreter Lock为了避免误导，我们还是来看一下官方给出的解释：

In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple native threads from executing Python bytecodes at once.
This lock is necessary mainly because CPython’s memory management is not thread-safe.
(However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)

好吧，是不是看上去很糟糕？一个防止多线程并发执行机器码的一个Mutex，乍一看就是个BUG般存在的全局锁嘛！别急，我们下面慢慢的分析。





由于GIL全局解释器锁的存在，意味着在任何一个时刻，只有一个线程处于执行状态。

(1)执行栈：

因为python是单线程的，同一时间只能执行一个方法，所以当一系列的方法被依次调用的时候，python会先解析这些方法，把其中的同步任务按照执行顺序排队到一个地方，这个地方叫做执行栈。



(2)事件队列(任务队列):

主线程之外，还存在一个"任务队列"（task queue）。当遇到异步任务时，异步任务会被挂起，继续执行执行栈中任务，等异步任务返回结果后，再按照执行顺序排列到‘’事件队列中‘’。



(3)一旦"执行栈"中的所有同步任务执行完毕，系统就会读取"任务队列"，看看里面有哪些事件。如果有，就将第一个事件对应的回调推到执行栈中执行，若在执行过程中遇到异步任务，则继续将这个异步任务排列到事件队列中。



(4)主线程每次将执行栈清空后，就去事件队列中检查是否有任务，如果有，就每次取出一个推到执行栈中执行，这个过程是循环往复的... ...，这个过程被称为“Event Loop 事件循环”。

注：

"任务队列"是一个先进先出的数据结构，排在前面的事件，优先被主线程读取。主线程的读取过程基本上是自动的，只要执行栈一清空，"任务队列"上第一位的事件就自动进入主线程。

所谓"回调函数"（callback），就是那些会被主线程挂起来的代码。异步任务必须指定回调函数，当主线程开始执行异步任务，就是执行对应的回调函数。

"任务队列"中的事件，除了IO设备的事件以外，还包括一些用户产生的事件（比如鼠标点击、页面滚动等等）。只要指定过回调函数，这些事件发生时就会进入"任务队列"，等待主线程读取。