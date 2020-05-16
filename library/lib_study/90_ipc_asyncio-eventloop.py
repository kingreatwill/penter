# https://docs.python.org/zh-cn/3/library/asyncio-eventloop.html
import asyncio

# print(asyncio.get_running_loop())
import functools

print(asyncio.get_event_loop())


# loop = asyncio.ProactorEventLoop()
# asyncio.set_event_loop(loop)

# print(asyncio.get_event_loop())
# print(asyncio.new_event_loop())

async def print1():
    print("1111111111")
    return 10


loop = asyncio.get_event_loop()
f = loop.run_until_complete(print1())
print(f)  # 10

cs = loop.call_soon(print, 1, 2, 3)
loop.call_soon_threadsafe(print, 4, 5, 6)
# 如果需要传递关键字参数请使用 functools.partial()
loop.call_soon(functools.partial(print, "Hello", flush=True))
# loop.call_soon(loop.stop)
# 指定时间之后再运行
loop.call_later(1, print, 1)
#loop.call_later(2, loop.stop)
# 指定时间之后再运行
loop.call_at(loop.time() + 2, loop.stop)
loop.run_forever()

# print(loop.is_running())
# print(loop.is_closed())
# loop.stop()
# loop.run_forever()

# loop.create_task(print1)
# loop.create_future()






import asyncio
import concurrent.futures

def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('90_ipc_asyncio-eventloop.py', 'rb') as f:
        return f.read(100)

def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10 ** 7))

async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # 1. Run in the default loop's executor:
    result = await loop.run_in_executor(
        None, blocking_io)
    print('default thread pool', result)

    # 2. Run in a custom thread pool:
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, blocking_io)
        print('custom thread pool', result)

    # # 3. Run in a custom process pool:
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(
    #         pool, cpu_bound)
    #     print('custom process pool', result)

asyncio.run(main())

# async def client_connected(reader, writer):
#     # Communicate with the client with
#     # reader/writer streams.  For example:
#     await reader.readline()
#
# async def main(host, port):
#     srv = await asyncio.start_server(
#         client_connected, host, port)
#     await srv.serve_forever()
#
# asyncio.run(main('127.0.0.1', 0))






