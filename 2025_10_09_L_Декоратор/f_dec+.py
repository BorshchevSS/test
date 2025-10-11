# Принимает исходную функцию
# Редактирует ее и возвращает новую




def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("До вызова")
        result = func(*args, **kwargs)
        print('что-то идет после вызова функции')
        return result
    return  wrapper

@my_decorator
def hello(name):
    print("Исходная функция")
    return f"Hello, {name}"

print(hello("Kate"))