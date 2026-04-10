import aiohttp
import asyncio
import time

urls = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.nasa.gov",
    "https://www.weather.gov",
    "https://www.cats.com",
    "https://www.reddit.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
]

async def fetch(session, url):
    response = await session.get(url, timeout=aiohttp.ClientTimeout(total=10))
    print(f"{url} -> {response.status}")
    await response.release()

async def main():
    start = time.time()

    connector = aiohttp.TCPConnector(ssl=False)
    session = aiohttp.ClientSession(connector=connector)

    tasks = []
    for url in urls:
        tasks.append(fetch(session, url))

    await asyncio.gather(*tasks)

    end = time.time()
    print(f"Concurrent time: {end - start:.2f}s")

    await session.close()

if __name__ == "__main__":
    asyncio.run(main())
