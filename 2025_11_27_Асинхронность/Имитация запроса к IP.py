import asyncio
async def fetch_data(task_id, delay):
    print(f"Task id {task_id} started")
    await asyncio.sleep(delay)
    print(f"Task {task_id} finished")
    return f"Data from task {task_id}"

async def main():
    task = [
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3)
    ]
    # gather запускает ПАРАЛЛЕЛЬНОЕ выполнение задач
    results = await asyncio.gather(*task) # сбор task (запускать несколько карутин одновременно и собирать результат вместе)
    print("all task finished")
    print(f"results: {results}")
asyncio.run(main())