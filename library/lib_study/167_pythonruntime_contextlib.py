from contextlib import contextmanager,asynccontextmanager
# 重要：https://docs.python.org/zh-cn/3/library/contextlib.html
# https://www.jianshu.com/p/94bc38e65fff
# contextmanager 用来做事务提交
"""
def auto_commit(self):
    try:
        yield self.session.commit()
    except Exception as e:
        self.session.rollback()
        raise e

with db.auto_commit():
    db.session.add()
    ...
"""
# @contextmanager
# def managed_resource(*args, **kwds):
#     # Code to acquire resource, e.g.:
#     resource = acquire_resource(*args, **kwds)
#     try:
#         yield resource
#     finally:
#         # Code to release resource, e.g.:
#         release_resource(resource)
#
# >>> with managed_resource(timeout=3600) as resource:
# ...     # Resource is released at the end of this block,
# ...     # even if code in the block raises an exception

# yield之前就是__init__中的代码块；yield之后其实就是__exit__中的代码块

# @asynccontextmanager
# async def get_connection():
#     conn = await acquire_db_connection()
#     try:
#         yield conn
#     finally:
#         await release_db_connection(conn)
#
# async def get_all_users():
#     async with get_connection() as conn:
#         return conn.query('SELECT ...')

print("_______contextlib.closing")
"""
等效于
from contextlib import contextmanager
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
"""

# from contextlib import closing
# from urllib.request import urlopen
#
# with closing(urlopen('http://www.python.org')) as page:
#     for line in page:
#         print(line)


print("-------------contextlib.suppress(压制)  忽略异常")
import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError(
        'The operation failed because of existing state'
    )


with contextlib.suppress(NonFatalError):
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')

"""
try:
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')
except NonFatalError:
    pass
"""

print('done')


print("--------------重定向输出流")
from contextlib import redirect_stdout, redirect_stderr
import io
import sys


def misbehaving_function(a):
    sys.stdout.write('(stdout) A: {!r}\n'.format(a))
    sys.stderr.write('(stderr) A: {!r}\n'.format(a))


capture = io.StringIO()
with redirect_stdout(capture), redirect_stderr(capture):
    misbehaving_function(5)

print(capture.getvalue())