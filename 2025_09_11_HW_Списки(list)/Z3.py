"""Задача 3. «Охота за сокровищами»
1. 2. 3. 4. Создайте список из 10 элементов, где 1 элемент =
«сокровище» (например, "X"), а остальные – ".".
Перемешайте список (сокровище в случайной позиции).
Пользователь вводит номер ячейки от 1 до 10.
Если там "X" → «Поздравляем, вы нашли сокровище!»,
иначе →
«Пусто. Попробуйте снова.»
5. Дать пользователю 3 попытки."""
import random

baseList = ["X", ".", ".", ".", ".", ".", ".", ".", ".", "."]
lenBaseList = len(baseList) #Длина исходного листа
randomList = []             #пустой список(list) в которы мы положим символы
numOfAttempts = 3 #Количество попыток

#Перемешиваем список
while len(randomList) < lenBaseList: #пока кол-во символов в создаваемом списке меньше исходного делай
    randomNum = random.randint(0, len(baseList) - 1)
    randomList.append(baseList[randomNum]) #Наполняю пустой список выбраными символами
    baseList.pop(randomNum) #Удаляю выбранный символ из начального списка
print(randomList)

# Запрос у пользователя номера ячейки (от 1 до 10), проверка
def inputNum():
    while True:
        try:
            selectNum = int(input(f'Введите число(индекс) места где находится сокровище : '))
            if selectNum <= 0 or selectNum > len(randomList) :
                print(f"Введи положительное число меньше либо равное {len(randomList)}")
                continue
            break
        except ValueError:
            print("Введи целое число")
    return selectNum

# Проверка результата нашел/неНашел сокровище
i = 0
while i < numOfAttempts:
    selectNum = inputNum()
    if randomList[selectNum-1] == "X":
        print("Поздравляем, вы нашли сокровище!")
        break
    else:
        i += 1
        if i == numOfAttempts:
            print("К сожалению, попытки израсходованы. Вы проиграли!")
            break
        print(f"Неудачная попытка (осталось попыток: {numOfAttempts-i}), попробуй еще!")
