from Z1 import delete_user, get_text,get_number


if __name__ == "__main__":
    # Тест декоратора проверки прав
    print("Тест проверки прав:")
    print(delete_user(1))  # Должен вернуть ошибку, так нет прав 'admin'

    # Тест декоратора преобразования в строку
    print("\nТест преобразования в строку:")
    print(f"get_number(): {get_number()} (тип: {type(get_number())})")
    print(f"get_text(): {get_text()} (тип: {type(get_text())})")