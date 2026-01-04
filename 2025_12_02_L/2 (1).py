import asyncio
import random
import time

URLS = ['page_A', 'page_B', 'page_C', 'page_D', 'page_E']

async def check_url_availability(url):
    delay = random.uniform(1.0, 5.0)
    print(f'url: {url}. Ожидание: {delay:.2f}сек.')
    await asyncio.sleep(delay)
    status = 'OK(200)' if random.choice([True, False, True]) else 'Error(404)'
    print(f'url: {url}. готово. статус: {status}. обработан за {delay:.2f} сек')
    return status

async def main():
    tasks = [check_url_availability(url) for url in URLS]
    results = await asyncio.gather(*tasks)
    print('все адреса обработаны')
    for status in results:
        print(status)

if __name__ == '__main__':
    asyncio.run(main())