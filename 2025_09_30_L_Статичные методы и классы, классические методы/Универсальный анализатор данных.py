"""Задача: "Универсальный анализатор данных"
Вы работаете в компании, которая получает данные из разных источников в
разных форматах: CSV, JSON и, возможно, в будущем появятся и другие. Вам
нужно разработать утилиту, которая сможет автоматически определять тип файла
и предоставлять по нему сводную информацию (например, количество записей,
список колонок и первые несколько строк).
Требования к программе:
1. Гибкость: Система должна быть легко расширяемой для поддержки новых
форматов файлов в будущем (например, XML или YAML), не изменяя
основной логики.
2. Автоматизация: Программа должна сама определять, какой обработчик
использовать, основываясь на расширении файла.
3. Надежность: Перед обработкой файла необходимо проверять, существует
ли он.
4. Информативность: Для каждого файла нужно выводить
стандартизированный отчет.
Описание решения
1. Абстрактный базовый класс (ABC) DataAnalyzer:
◦ Это "чертеж" для всех обработчиков.
◦ Он будет содержать абстрактный метод read_data(), который каждая
дочерняя реализация (для CSV, JSON и т.д.) должна будет
переопределить.
◦ Также в нем будет общий метод get_summary(), который будет
работать для любого типа данных, как только они будут прочитаны.
2. Конкретные классы-наследники CSVAnalyzer и JSONAnalyzer:
◦ Эти классы будут наследоваться от DataAnalyzer.
◦ Каждый из них реализует свою версию метода read_data(), используя
библиотеку Pandas для чтения соответствующего формата файла.
3. Статический метод validate_path():
◦ Это будет вспомогательная функция, размещенная внутри
DataAnalyzer. Она будет проверять, существует ли файл по
указанному пути. Этот метод не зависит от состояния конкретного
объекта или класса
4. Метод класса create_analyzer():
◦ Это будет метод в DataAnalyzer. Его задача - принять путь к файлу,
посмотреть на его расширение (.csv или .json) и вернуть правильный
объект-анализатор (CSVAnalyzer или JSONAnalyzer). Он оперирует
самим классом для создания нужного экземпляра."""

import pandas
from abc import ABC, abstractmethod
import os

class DataAnalyzer(ABC):
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None # Для хранения данных после чтения

    @abstractmethod
    def read_data(self):
        pass

    def get_summary(self):
        "Также в нем будет общий метод get_summary(), который будет работать для любого типа данных, как только они будут прочитаны."
        if self.data is None:
            return "Данные не загружены"
        num_rows, num_cols = self.data.shape
        columns = list(self.data.columns)

        print("----СВОДНЫЙ ОТЧЕТ----")
        print(f"Файл: {os.path.basename(self.filepath)}")
        print(f"Количество записей: {num_rows}")
        print(f"Количество колонок: {num_cols}")
        print(f"Названия колонок: {columns}")
        print("-"*30+"\n")

    @staticmethod
    def validate_data(filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Файл не найден по пути: {filepath}")
        return True

    @classmethod
    def create_analyzer(cls, filepath):
        cls.validate_data(filepath)
        _, ext = os.path.splitext(filepath)
        ext = ext.lower()
        if ext == ".csv":
            return CSVAnalyzer(filepath)
        elif ext ==".json":
            return JSONAnalyzer(filepath)
        else:
            raise ValueError(f"Неподдерживаемый тип файла: {ext}")

class CSVAnalyzer(DataAnalyzer):
    def read_data(self):
        print(f"Читаю {self.filepath}")
        self.data = pandas.read_csv(self.filepath)

class JSONAnalyzer(DataAnalyzer):
    def read_data(self):
        print(f"Читаю {self.filepath}")
        self.data = pandas.read_json(self.filepath)


# print(pandas.read_csv("data.csv"))
# print(pandas.read_csv("data.csv").shape)
# print("\n")
# print(pandas.read_json("data.json"))
# print(pandas.read_json("data.json").shape)

#get_summary
if __name__ == "__main__":
    file_to_analyze = ["data.csv", "data.json","not.txt"]

    for file in file_to_analyze:
        try:
            analyzer = DataAnalyzer.create_analyzer(file)
            analyzer.read_data()
            analyzer.get_summary()
        except(FileNotFoundError, ValueError) as e:
            print(f"Ошибка при обработке файла {file}: {e}\n")
