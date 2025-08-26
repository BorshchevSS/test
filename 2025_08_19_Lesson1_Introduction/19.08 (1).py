# CamelCase -
# snake_case
#
# x = 10 #int
# y = 3.5 #float
# t = True #bool
# f = False #bool
# s = "stroka"#str
# l = [1, 4, True, 'str'] #list
# t = (4, 2, 5, 6) #tuple
# se = {5, 6, 8, 4} #set
# d = {'a': 5, 'b': 6, 'c': 7} #dict
#
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(type(name))
# print(type(age))
#
# if age > 18:
#     print("You are old.")
# elif  age >=0  and age <= 18:
#     print("You are young.")
# # && || !
# # and  or not
# else:
#     print('Invalid age')
# # print('Name: ', name, 'age: ', age)
# print(f'Name: {name}, age: {age}')

# + - / * **
# // %
# print(5 // 2)
# print(9 // 4)
# print(9 % 3) #0
# print(10 % 4)
# print(6 % 9)
# elif
# else
#
# login = 'Seal_al'
# password = '1234'
# user_login = input('Enter login: ')
# if login == user_login:
#     user_pass = input('Enter password: ')
#     if password == user_pass:
#         print('Login successful')
#     else:
#         print('Password incorrect')
# else:
#     print('Login failed')

# Задача 3 (условия)
# amount = float(input('Сумма покупки: '))
# age = int(input('Ваш возраст: '))
#
# discount = 0 #базовая скидка (процент)
#
# if amount > 100:
#     discount += 10  #discount = discount + 10
#
# if age > 65:
#     discount += 5
#
# final_price = amount * (1 - discount / 100)
# if discount == 0:
#     print('Скидки нет')
# else:
#     print(f'Общая скидка: {discount}. \n Сумма: {final_price:.2f} ')
#
# for (let i = 0; i < 10; i++)
# for i in range(5, 1, -1):
#     print(i)
# range(n, k, step)
# range(k)
# range(n, k)
# n-начало диапозона (0)
# k-конец диапозона не включая значение
# step - шаг (1)

# a = 'hello'
# print(id(a))
# b = 'hello'
# print(id(b))
# a = 'hello!'
# print(id(a))
#
# str1 = 'abracadabra'
# for char in str1:
#     print(char)
#
# for ch in range(len(str1)):
#     print(f'{ch}: {str1[ch]}')
#
# count = 1
# while count < 20:
#     # if count == 5:
#     #     break
#     # count += 1
#     if count == 2 or count == 10 or count == 15:
#         count += 1
#         continue
#     print(count)
#     count += 1

#
# try:
#     n = int(input('введите число'))
#     print(10/n)
# except ZeroDivisionError:
#     print("Делить на ноль нельзя")
# except KeyboardInterrupt:
#     print('Введите значение')
# except ValueError:
#     print('Введите значение')

# Задача 3 (циклы)

while True:
    try:
        days = int(input('Введите кол-во дней: '))
        if days <= 0:
            print('Введите положительное число')
            continue
        break
    except ValueError:
        print('Введите целое число')

total_goods = 0

for i in range(1, days + 1):
    while True:
        try:
            goods = int(input(f'Кол-во товаров за день {i}:'))
            if goods < 0:
                print('введите положительное')
                continue
            total_goods += goods
            break
        except ValueError:
            print('введите число')

avg = total_goods / days
print(f'AVG товара за день: {avg:.2f}')




