"""Задание 5
Задача: реализовать менеджер контекста, который будет пытаться (использовать библиотеку random) несколько раз установить соединение с API в случае неудачи.
Если соединение не удаётся установить после нескольких попыток, программа должна выбросить исключение."""

import time
import random

# для имитации исключения соединения
class ConnectionError(Exception):
    pass

class ApiConnectionRetry:
    def __init__(self, max_attempts=3):
        self.max_attempts = max_attempts
        self.connection = None # объект соединения если установлено

    def attempt_connection(self):
        # с вероятностью 70% выдает ошибку (проверить логику повторов)
        # random.random() float [0.0, 1.0)
        if random.random() < 0.7:
            # 70% шанс на сбой
            raise ConnectionError("сбой соединения с API")
        return "API соединение успешное"

    def __enter__(self):
        attempts = 0
        while attempts < self.max_attempts:
            attempts += 1
            print(f"Попытка соединения №{attempts}")
            try:
                self.connection = self.attempt_connection()
                print("соединение успешное")
                return self.connection
            except ConnectionError as e:
                print(f"Не удалось соединиться: {e}")
                if attempts < self.max_attempts:
                    wait_time = random.uniform(0.5, 1.5) #случайная задержка
                    print(f"ожидание {wait_time:.2f} сек")
                    time.sleep(wait_time)
                else:
                    print("Попытки исчерпаны")
                    raise #повторно выбрасит последнее исключение
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # должен делать очистку
        if self.connection:
            print("Соединение закрыто")
            self.connection = None
        return False

print("Сценарий 1")
try:
    with ApiConnectionRetry(max_attempts=5) as api:
        print(f"Внутри. {api}")
except ConnectionError as e:
    print(f"{e} (не должно случиться)")

