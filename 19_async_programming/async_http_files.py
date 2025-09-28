import asyncio
import aiohttp
import aiofiles

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f"Error fetching {url}: {e}"

async def write_file_async(filename, content):
    async with aiofiles.open(filename, 'w') as file:
        await file.write(content)

async def read_file_async(filename):
    async with aiofiles.open(filename, 'r') as file:
        return await file.read()

async def producer(queue, items):
    for item in items:
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.1)

async def consumer(queue, name):
    while True:
        try:
            item = await asyncio.wait_for(queue.get(), timeout=1.0)
            print(f"Consumer {name} consumed: {item}")
            queue.task_done()
            await asyncio.sleep(0.2)
        except asyncio.TimeoutError:
            print(f"Consumer {name} timed out")
            break

async def main():
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/1'
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for i, result in enumerate(results):
            print(f"Result {i}: {len(str(result))} characters")
    
    queue = asyncio.Queue()
    
    items = ['item1', 'item2', 'item3', 'item4', 'item5']
    
    producer_task = asyncio.create_task(producer(queue, items))
    consumer_tasks = [
        asyncio.create_task(consumer(queue, 'A')),
        asyncio.create_task(consumer(queue, 'B'))
    ]
    
    await producer_task
    await queue.join()
    
    for task in consumer_tasks:
        task.cancel()

if __name__ == "__main__":
    asyncio.run(main())
