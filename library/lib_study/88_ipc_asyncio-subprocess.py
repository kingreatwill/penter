import asyncio


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')


# loop = asyncio.ProactorEventLoop()
# asyncio.set_event_loop(loop)
# Python 3.7
asyncio.set_event_loop_policy(
    asyncio.WindowsProactorEventLoopPolicy())
# Python 3.8
# The default event loop on Windows is now the ProactorEventLoop.

asyncio.run(run('where cmd'))

import asyncio
import sys


async def get_date():
    code = 'import datetime; print(datetime.datetime.now())'

    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Read one line of output.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Wait for the subprocess exit.
    await proc.wait()
    return line


date = asyncio.run(get_date())
print(f"Current date: {date}")
