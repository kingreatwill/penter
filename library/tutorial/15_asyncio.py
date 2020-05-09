"""
async 包与 async/await 关键字

现在你已经有了一定的异步IO的背景知识，现在来看看Python内的实现。
Python的 asyncio 包（从Python 3.4开始引入）和 async、await 两个关键字虽然用于不同的目的，但是他们共同实现了声明、构建、执行以及管理异步代码的功能。
"""
import asyncio


async def add(x, y):
    r = x + y
    return r


async def bad_call(a, b, c, d):
    a_b = await add(a, b)
    await asyncio.sleep(1)
    c_d = await add(c, d)
    print(a_b * c_d)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bad_call(1, 2, 3, 4))

from datetime import datetime
import asyncio


async def add(n):
    print(datetime.now().strftime('%H:%M:%S.%f'))
    count = 0
    for i in range(n):
        count += i
    print(datetime.now().strftime('%H:%M:%S.%f'))
    return count


async def fun(n):
    res = await add(n)
    print(f'res = {res}')


loop = asyncio.get_event_loop()
tasks = [fun(20000000), fun(30000000)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
