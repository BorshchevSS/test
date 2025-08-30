import string
import random
from runpy import run_path

minLengthPassword = 4  # Читай условие задачи

# Функцию для ввода и проверки длины
def inputAndVerificationLengthPassword ():
    while True:
        try:
            lengthPassword = input(f"Введи длину пароля (значение должно быть больше {minLengthPassword}): ")
            lengthPassword = int(lengthPassword)
            if lengthPassword < minLengthPassword:
                print(f"Вы ввели '{lengthPassword}', введи число больше или равное {minLengthPassword}")
                continue
            break
        except ValueError:
            print(f"Вы ввели '{lengthPassword}', введи целое число")
    return lengthPassword

#Перемешиваем список
def shuffleTheList (originalList):
    randomList = []
    baseList = originalList  # хранятся неиспользованные символы
    while len(baseList) > 0: # пока в базавом списке есть неиспользованнные символы делай
        randomNum = random.randint(0, len(baseList) - 1)
        randomList.append(baseList[randomNum]) #Наполняю пустой список выбранными символами
        baseList.pop(randomNum) #Удаляю выбранный символ из начального списка
    return randomList

def passwordGeneration ():
    lengthPassword = inputAndVerificationLengthPassword()

    #Строки, содержащие символы для формирования пароля
    symbolsInLowerCase = string.ascii_lowercase #abcdefghijklmnopqrstuvwxyz
    symbolsInUpperCase = string.ascii_uppercase #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    symbolsDigits = string.digits #"0123456789" - строка содержащая символы цифр(не ЧИСЛА!!!)
    symbolsSpecial = "!@#$%^&*()"

    # наполняю массив символами (поочерёдно добавляю символ каждого типа)
    passwordRandom_1 = []
    for i in range(lengthPassword):
        if len(passwordRandom_1) < lengthPassword:
            passwordRandom_1.append(random.choice(symbolsInLowerCase))
        else:
            break
        if len(passwordRandom_1) < lengthPassword:
            passwordRandom_1.append(random.choice(symbolsInUpperCase))
        else:
            break
        if len(passwordRandom_1) < lengthPassword:
            passwordRandom_1.append(random.choice(symbolsDigits))
        else:
            break
        if len(passwordRandom_1) < lengthPassword:
            passwordRandom_1.append(random.choice(symbolsSpecial))
        else:
            break
      # print(passwordRandom_1)
    passwordRandom_2 = shuffleTheList(passwordRandom_1) # Перемешиваем список
    passwordRandom = "".join(passwordRandom_2) # Преобразование списка в строку
    return passwordRandom

print(passwordGeneration())