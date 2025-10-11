# Принимает исходную функцию
# Редактирует ее и возвращает новую




def my_decorator(func):
    def wrapper():
        print("До вызова")
        func()
        print('то-то идет после вызова функции')
    return  wrapper

@my_decorator
def hello():
    print("Исходная функция")

print(hello("Kate"))