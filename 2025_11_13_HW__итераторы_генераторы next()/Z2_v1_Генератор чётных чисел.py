"""Задача 2: Генератор чётных чисел
Ситуация: мы хотим разработать генератор, который выводит только чётные числа в заданном диапазоне. Это полезно для экономии времени и ресурсов, когда нужны только определённые данные из большого набора.
Задача: напишите генератор even_numbers(start, end), который принимает два аргумента:
• start — начало диапазона.
• end — конец диапазона. Генератор должен возвращать только чётные числа в указанном диапазоне. Ожидаемый результат: Если пользователь ввёл start = 5 и end = 12, вывод: Чётные числа от 5 до 12: 6 8 10 12"""


class EvenNumbersGenerator:
    """
    Класс-генератор для чётных чисел с использованием next()
    """

    def __init__(self, start, end):
        """
        Инициализация генератора

        Args:
            start (int): Начало диапазона
            end (int): Конец диапазона
        """
        self.start = start
        self.end = end
        self._reset()

    def _reset(self):
        """Внутренний метод для сброса состояния"""
        # Находим первое чётное число в диапазоне
        self.current = self.start if self.start % 2 == 0 else self.start + 1

    def __iter__(self):
        """
        Возвращает итератор (self), так как класс реализует __next__
        """
        self._reset()  # Сбрасываем состояние при каждом новом итераторе
        return self

    def __next__(self):
        """
        Возвращает следующее чётное число с помощью next()

        Returns:
            int: Следующее чётное число

        Raises:
            StopIteration: Когда числа закончились
        """
        if self.current > self.end:
            raise StopIteration

        result = self.current
        self.current += 2
        return result

    def next(self):
        """
        Альтернативный метод для получения следующего числа
        (для явного вызова next())
        """
        return self.__next__()

    def get_count(self):
        """Возвращает количество чётных чисел в диапазоне"""
        first_even = self.start if self.start % 2 == 0 else self.start + 1
        if first_even > self.end:
            return 0
        return (self.end - first_even) // 2 + 1

    def get_remaining(self):
        """Возвращает список оставшихся чисел (для отладки)"""
        remaining = []
        temp_current = self.current
        while temp_current <= self.end:
            remaining.append(temp_current)
            temp_current += 2
        return remaining


# Демонстрация работы с next()
def demo_with_next():
    print("ДЕМОНСТРАЦИЯ РАБОТЫ")
    print("=" * 40)

    # Создаем генератор
    generator = EvenNumbersGenerator(5, 12)

    print("Способ 1: Использование next() в цикле while:")
    gen_iter = iter(generator)  # Получаем итератор
    try:
        while True:
            num = next(gen_iter)  # Явный вызов next()
            print(num, end=" ")
    except StopIteration:
        print("\nКонец последовательности")

    print("\n" + "-" * 40)

    print("Способ 2: Использование метода next():")
    generator2 = EvenNumbersGenerator(3, 9)
    try:
        while True:
            num = generator2.next()  # Вызов метода next()
            print(num, end=" ")
    except StopIteration:
        print("\nКонец последовательности")

    print("\n" + "-" * 40)

    print("Способ 3: Ручное управление с next():")
    generator3 = EvenNumbersGenerator(10, 16)
    print("Оставшиеся числа:", generator3.get_remaining())

    # Ручное получение чисел
    try:
        print("Первое число:", next(generator3))  # 10
        print("Второе число:", next(generator3))  # 12
        print("Третье число:", next(generator3))  # 14
        print("Оставшиеся числа:", generator3.get_remaining())  # [16]
        print("Четвертое число:", next(generator3))  # 16
        print("Пятое число:", next(generator3))  # StopIteration
    except StopIteration:
        print("Достигнут конец последовательности!")

demo_with_next()
