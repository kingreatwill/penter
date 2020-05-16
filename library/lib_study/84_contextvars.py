import contextvars

var = contextvars.ContextVar('var', default=42)

print(var.get())
var.set(10)
token = var.set(20)
print(token)
print(token.var)
print(token.old_value)
print(var.get())

var.reset(token)  # 重置到当时的
print(var.get())

# 返回当前上下文对象的副本。
ctx = contextvars.copy_context()
print(ctx.items())
print("---------------")
var = contextvars.ContextVar('var')
var.set('spam')


def main():
    # 'var' was set to 'spam' before
    # calling 'copy_context()' and 'ctx.run(main)', so:
    # var.get() == ctx[var] == 'spam'

    var.set('ham')

    # Now, after setting 'var' to 'ham':
    # var.get() == ctx[var] == 'ham'


ctx = contextvars.copy_context()

# Any changes that the 'main' function makes to 'var'
# will be contained in 'ctx'.
ctx.run(main)

print(ctx[var])
print(ctx.get(var))
print(var.get())
# The 'main()' function was run in the 'ctx' context,
# so changes to 'var' are contained in it:
# ctx[var] == 'ham'

# However, outside of 'ctx', 'var' is still set to 'spam':
# var.get() == 'spam'


print("---------------------")

import asyncio
import contextvars

client_addr_var = contextvars.ContextVar('client_addr', default="游客")


def render_goodbye():
    # The address of the currently handled client can be accessed
    # without passing it explicitly to this function.

    client_addr = client_addr_var.get()
    return f'Good bye, client @ {client_addr}\n'.encode()


async def handle_request(reader, writer):
    addr = writer.transport.get_extra_info('socket').getpeername()
    print(addr, " 连接上了")

    # In any code that we call is now possible to get
    # client's address by calling 'client_addr_var.get()'.
    name = await reader.readline()
    client_addr_var.set(name)
    print(name, " 名称")
    while True:
        line = await reader.readline()
        print("客户端 问：", line)
        if not line.strip():
            break
        writer.write(b"server "+line)

    writer.write(render_goodbye())
    writer.close()


async def main2():
    srv = await asyncio.start_server(
        handle_request, '127.0.0.1', 8081)

    async with srv:
        await srv.serve_forever()


asyncio.run(main2())

# To test it you can use telnet:
#     telnet 127.0.0.1 8081
