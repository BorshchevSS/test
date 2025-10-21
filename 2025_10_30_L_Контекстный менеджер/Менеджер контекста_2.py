# __enter__() - при входе в with
# __exit__() вызывается при выходе из with
# свой менеджер контекста
class FileWriter:
    # def __init__(self, filename):
    #     self.filename = filename
    #     self.file = None

    def __enter__(self):
        self.file = open('log.txt', 'w')
        return self

    def abracadabra(self, text):
        self.file.write(text)
                        #тип  само исключение  объект трассировки(для диагностики)
    def __exit__(self, exc_type, exc_val, exc_tb):
        # if self.file:
        self.file.close()
        if exc_type:
            print(f'Ошибка {exc_val}')
        # self.file.close()
        return True

class DBConnection:
    def __enter__(self):
        print('открываем соединение с бд')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('закрываем соединение с БД')
        if exc_type:
            print(f'Ошибка {exc_val}')
        return True


#использование
with FileWriter() as writer, DBConnection() as db:
    writer.abracadabra('Hello World')
    #raise Exception('ошибка при записи')
    print("Работа с БД")
