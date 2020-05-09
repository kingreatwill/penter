# coroutine function -- 协程函数
# 普通函数
import asyncio


def function():
    return 1


# 生成器函数
def generator():
    yield 1


# 异步函数（协程）
async def async_function():
    return 1


# 异步生成器
async def async_generator():
    yield 1


import types


# print(type(function) is types.FunctionType)
# print(type(generator()) is types.GeneratorType)
# print(type(async_function()) is types.CoroutineType)  # 有个警告
# print(type(async_generator()) is types.AsyncGeneratorType)


# async def


# async for


# with
class VOW(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = "I say: " + self.text  # add prefix
        return self  # note: return an object

    def __exit__(self, exc_type, exc_value, traceback):
        self.text = self.text + "!"  # add suffix


with VOW("I'm fine") as myvow:
    print(myvow.text)

print(myvow.text)

# async with
import asyncio


async def log(some_thing):
    print(some_thing)


class AsyncContextManager:
    async def __aenter__(self):
        await log('entering context')
        return "返回值做为c的值"

    async def __aexit__(self, exc_type, exc, tb):
        await log('exiting context')


async def run_async_with():
    async with AsyncContextManager() as c:
        print("使用 async with 来管理异步上下文")
        print(c)


loop = asyncio.get_event_loop()
loop.run_until_complete(run_async_with())


# loop.close()


# asynchronous iterator -- 异步迭代器

# awaitable -- 可等待对象

# asynchronous context manager -- 异步上下文管理器
# 此种对象通过定义 __aenter__() 和 __aexit__() 方法来对 async with 语句中的环境进行控制。由 PEP 492 引入。
# 与 with 中的上下文管理器需要定义两个方法 enter() 和 exit() 一样，异步上下文管理器同样也需要实现 aenter() 和 aexit() 方法。
# async with 异步上下文管理器同样只能在 协程函数 中使用，否则会报语法错误 ( SyntaxError )。
# 与普通上下文管理器相比，异步上下文管理器能够在其进入 enter() 和退出方法 exit() 中暂停执行。

#  __aiter__()  __anext__() __aenter__()  __aexit__()
class AsyncIteratorWrapper:
    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value


async def demoAsync():
    async for letter in AsyncIteratorWrapper("abc"):
        print(letter)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([demoAsync()]))
loop.close()
