import aiohttp
import asyncio
import time

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Загружена {url}, длина: {len(await response.text())}")
            return await response.text()

async def main():
    urls = ["https://example.com", "https://httpbin.org/get", "https://httpbin.org/get"]
    results = await asyncio.gather(*(fetch(url) for url in urls))
    print(results)

start_time = time.time()
asyncio.run(main())

print(f"Время выполнения: {time.time() - start_time}")