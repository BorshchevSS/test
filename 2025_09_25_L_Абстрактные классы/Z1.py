from abc import ABC, abstractmethod

class DataManager(ABC):
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass


class FileDataManager(DataManager):
    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Файл не найден"

    def write_data(self, data):
        with open(self.file_name, "w", encoding="utf-8") as f:
            f.write(data)
        return "Данные записаны в файл"


class DatabaseDataManager(DataManager):
    def __init__(self):
        self.database = {}

    def read_data(self):
        return self.database

    def write_data(self, data):
        if isinstance(data, dict):
            self.database.update(data) #дополняет
            return "Данные добавлены в БД"
        return "Ошибка! ожидается словарь"


if __name__== "__main__":
    file_manager = FileDataManager("data.txt")
    db_manager = DatabaseDataManager()

    print(file_manager.write_data("Пример данных"))
    print("Содержимое файла: ", file_manager.read_data())

    print(db_manager.write_data({"user": "admin", "password": 1234}))
    print("Содержимое БД", db_manager.read_data())