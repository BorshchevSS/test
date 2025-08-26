"""Условие:
Пользователь вводит пароль. Нужно проверить, соответствует ли он требованиям:
• длина ≥ 8 символов
• содержит хотя бы одну заглавную букву
• содержит хотя бы одну цифру
• не содержит пробелов
Если пароль не соответствует требованиям, вывести, какие именно правила нарушены.
Пример:
Введите пароль: qwerty1
Ошибка: пароль слишком короткий
Ошибка: нет заглавной буквы"""

password = input("Введите пароль для проверки: ")
errors = [] #сохраним ошибки сюда

#Проверка количества символов
if len(password) < 8:
    errors.append("Пароль слишком короткий")

#Проверка наличия заглавной буквы
has_upper = False #флажек
for char in password:
    if char.isupper():
        has_upper = True
        break
if not has_upper:
    errors.append("Нет заглавной буквы")

#проверка наличия цифры
has_difit = False #флажек
for char in password:
    if char.isdigit():
        has_difit = True
        break
if not has_difit:
    errors.append("Нет цифры")

#Не должно быть пробела
if " " in password:
    errors.append("В пароле излишне присутствует пробел!")

if len(errors)>0:
    for err in errors:
        print(f"Ошибка:  {err}")
else:
    print("Пароль подходит")