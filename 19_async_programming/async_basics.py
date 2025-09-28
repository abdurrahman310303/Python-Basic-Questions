import asyncio

async def fetch_data(url, delay):
    print(f"Fetching data from {url}")
    await asyncio.sleep(delay)
    print(f"Data fetched from {url}")
    return f"Data from {url}"

async def main():
    tasks = [
        fetch_data("https://api1.example.com", 2),
        fetch_data("https://api2.example.com", 1),
        fetch_data("https://api3.example.com", 3)
    ]
    
    results = await asyncio.gather(*tasks)
    print("All data fetched:")
    for result in results:
        print(result)

asyncio.run(main())

async def countdown(n):
    for i in range(n, 0, -1):
        print(f"Countdown: {i}")
        await asyncio.sleep(1)
    print("Done!")

async def counter(name, delay):
    for i in range(5):
        print(f"{name}: {i}")
        await asyncio.sleep(delay)

async def run_concurrent():
    await asyncio.gather(
        countdown(3),
        counter("Counter-A", 0.5),
        counter("Counter-B", 0.8)
    )

asyncio.run(run_concurrent())
