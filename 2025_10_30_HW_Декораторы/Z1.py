from functools import wraps

'''Задача 1: Декоратор для проверки прав доступа
Создайте декоратор, который проверяет, есть ли у пользователя необходимые права доступа для выполнения функции.
Если прав недостаточно, функция должна возвращать сообщение об ошибке.'''

def requires_permission(permission):
    """1. requires_permission:
   · Принимает требуемое разрешение как параметр
   · Возвращает декоратор, который проверяет наличие прав у пользователя
   · Если прав нет - возвращает сообщение об ошибке
   · Если права есть - выполняет оригинальную функцию"""
    # @wraps(permission)  Сохраняет метаданные исходной функции
    def decorator(func):
        print("Выполняется перед вызовом функции")
        def wrapper(*args, **kwargs):
            # В реальном приложении здесь была бы проверка прав пользователя
            # Для примера предположим, что текущий пользователь имеет права 'user'
            current_user_permissions = ['user']  # Только обычные права
            if permission not in current_user_permissions:
                return f"Ошибка: Недостаточно прав. Требуется: {permission}"
            return func(*args, **kwargs)
        #print("Выполняется после вызова функции") - Где расположить?
        return wrapper
    return decorator


@requires_permission('admin')
def delete_user(user_id):
    #Это моя декорируемая функция
    return f"User {user_id} deleted."

'''Задача 2: Декоратор для преобразования результата
Создайте декоратор, который преобразует результат функции в строку. Если результат уже строка, он должен возвращаться без изменений.'''

def to_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result
        return str(result)
    return wrapper

@to_string
def get_number():
    return 42

@to_string
def get_text():
    return "Hello, World!"