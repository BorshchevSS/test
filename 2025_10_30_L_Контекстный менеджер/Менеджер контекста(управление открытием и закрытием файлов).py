#Помошники: создание с совершения соединений

# __enter__() - При входе в with
# __exit__() - Вызывается при выходе из блока (закрывает файл)

# Свой менеджер контекста


class FileWriter:
    # def __init__(self, filename):
    #     self.filename = filename
    #     self.file = None

    def __enter__(self):
        self.file = open("log.txt", "w")
        return self

    def write(self, text):
        self.file.write(text)

                        #тип    #само исключение #объект трассировки
    def __exit__(self, exc_type, exc_val, exc_tb):

        # if self.file:
        #     self.file.close()
        if exc_type:
            print(f"Ошибка {exc_val}")
        self.file.close()
        return True

class DBCConnection:
    def __enter__(self):
        print("Открываем соединение с БД")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Ошибка {exc_val}")
        return True


# Использование
with FileWriter("output.txt") as writer:
    writer.abracadabra("Hello Worl")
    raise Exception("ошибка при записи")

