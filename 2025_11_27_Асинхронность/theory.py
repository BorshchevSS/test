import asyncio
# event loop - цикл событий, который управляет корутин
# coroutine (корутины) - асинхронные функции
# task - объекты, которые представляют выполнение корутины

async def main():
    print("hello")
    await asyncio.sleep(1) # Подожди (приостанавливает, но не блокирует весь поток программ)
    print("world")
#asyncio.run(main()) # Управляет жизненным циклом event loop

#Event Loop - работает в фоновом режиме (постоянно) и постоянно мониторит события

async def task1():
    print("task 1: start")
    await asyncio.sleep(2)
    print("task1: end")

async def task2():
    print("task 2: start")
    await asyncio.sleep(1)
    print("task2: end")

async def main(): #создали объекты Task
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    # Ждем завершения обеих задач
    await t1
    await t2

# asyncio.run(main())

# конкурентно запускают

async def coroutine():
    print("start")
    await asyncio.sleep(2)
    print("end")
    return "done"

async  def main():
    t1 = asyncio.create_task(coroutine())
    print(t1.done())
    #t2 = asyncio.create_task(coroutine())
    await t1
    print(t1.result())
    print(t1.done())
    #await t2
asyncio.run(main())

# Task
# task.done() - проверяет завершение
# task.result() - результат выполнения корутины (InvalidStateError)
# task.cancel() - отменяет выполнение таски
# task.exception() - возвращает исключение (из корутины)


