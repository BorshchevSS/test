"""Задание 1. Очередь обработки задач с ограничением
Ситуация: мы создаём систему обработки задач, где одновременно можно хранить только последние 5 задач для обработки. Если
добавляется новая, самая старая автоматически удаляется. Нам нужно реализовать эту систему с использованием deque.
Задача — создать класс TaskQueue, который:
1. Инициализируется с максимальной длиной очереди.
2. Имеет метод add_task(task), который добавляет новую задачу в очередь.
3. Имеет метод get_tasks(), который возвращает список текущих задач.
Используем deque с параметром maxlen для реализации."""
from asyncio import current_task
from collections import deque

class TaskQueue:
    def __init__(self, max_len=5):
        self.max_len = max_len
        self.queue: deque = deque(maxlen=max_len)

    def add_task(self, task):
        self.queue.append(task)
        if len(self.queue) == self.max_len and self.max_len > 0:
            print("возможно старая задача была уделена")

    def get_tasks(self):
        return list(self.queue)

print("Тестирование")
tasks = [1, 2, 3, 4]

task_manager = TaskQueue()
for i in range (1, 6):
    task_manager.add_task(f"Задача №{i}")
current_tasks = task_manager.get_tasks()
print(current_tasks)
print(len(current_tasks))

task_manager.add_task("Задача №6")
task_manager.add_task("Задача №7")

current_tasks = task_manager.get_tasks()
print(current_tasks)

