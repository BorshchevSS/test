"""```python
# Задача 1: Декоратор для проверки прав доступа
def requires_permission(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # В реальном приложении здесь была бы проверка прав пользователя
            # Для примера предположим, что текущий пользователь имеет права 'user'
            current_user_permissions = ['user']  # Только обычные права

            if permission not in current_user_permissions:
                return f"Ошибка: Недостаточно прав. Требуется: {permission}"
            return func(*args, **kwargs)
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(user_id):
    return f"User {user_id} deleted."

# Задача 2: Декоратор для преобразования результата
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

# Тестирование
if __name__ == "__main__":
    # Тест декоратора проверки прав
    print("Тест проверки прав:")
    print(delete_user(1))  # Должен вернуть ошибку, так нет прав 'admin'

    # Тест декоратора преобразования в строку
    print("\nТест преобразования в строку:")
    print(f"get_number(): {get_number()} (тип: {type(get_number())})")
    print(f"get_text(): {get_text()} (тип: {type(get_text())})")
```

Результат выполнения:

```
Тест проверки прав:
Ошибка: Недостаточно прав. Требуется: admin

Тест преобразования в строку:
get_number(): 42 (тип: <class 'str'>)
get_text(): Hello, World! (тип: <class 'str'>)
```

Объяснение:

1. requires_permission:
   · Принимает требуемое разрешение как параметр
   · Возвращает декоратор, который проверяет наличие прав у пользователя
   · Если прав нет - возвращает сообщение об ошибке
   · Если права есть - выполняет оригинальную функцию
2. to_string:
   · Выполняет оригинальную функцию
   · Проверяет тип результата
   · Если результат не строка - преобразует его в строку
   · Если результат уже строка - возвращает без изменений

Оба декоратора используют стандартный паттерн с тремя уровнями вложенности для работы с параметрами."""