import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            data = await response.json()
            print(html)
            print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())