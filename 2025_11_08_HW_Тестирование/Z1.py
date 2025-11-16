"""Задание 1
Задача: создать функцию is_palindrome(s), которая проверит, является
ли строка палиндромом (читается одинаково слева направо и справа
налево). Функция должна игнорировать регистр символов. Написать тесты для:
• палиндрома, состоящего из букв;
• палиндрома, состоящего из цифр;
• не палиндрома."""

def is_palindrome(s):
    marker = False
    s_lower = str(s).lower()
    s_lower_rew = s_lower[::-1]
    # print(s_lower)
    # print(s_lower_rew)
    if s_lower == s_lower_rew:
        marker = True
    return f"Строка '{s}' {("является" if marker else "НЕ является")} палиндромом."

str_1 = "Qwq"
str_2 = "qwe4ewq"
str_3 = 123321
str_4 = 12

print(is_palindrome(str_1))
print(is_palindrome(str_2))
print(is_palindrome(str_3))
print(is_palindrome(str_4))