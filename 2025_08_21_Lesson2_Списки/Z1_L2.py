#import random                      #random.randint()
#from random import randint         #randint()
from random import randint as r     #r

from main_ import count

# num = 6
# num2 = num
# lotto = []
#
# while len(lotto) < num:
#     num = r(1, 20)
#     if num not in lotto:
#         lotto.append(num)
#
# print(lotto)


# user_input = []
# print("Введите 6 чисел от 1 до 20")
#
# while len(user_input) < num2:
#     try:
#         n = int(input((f"Num{len(user_input) + 1}: ")))
#         if n <= 0 or n > 20:
#             print("Введи положительное число в диапазоне от 1 до 20")
#             continue
#         break
#     except ValueError:
#         print("Введи целое число")
#
# print(len(user_input))
# print(num2)
# user_input = [1, 2, 3, 4, 5, 6]
#
# count = 0
# for num in user_input:
#     if num in lotto:
#         count += 1
#
# if count <=1:
#     print("Увы, не повезло!")
# elif count <=3:
#     print("Неплохо")
# elif count <= 5:
#     print("Очень близко")
# else:
#     print("Джек пот")
#
# print(lotto)
# print(user_input)
# print(count)
