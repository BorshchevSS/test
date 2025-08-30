import random

#Перемешиваем список
def shuffleTheList (originalList):
    randomList = []
    baseList = originalList  # хранятся неиспользованные символы
    while len(baseList) > 0: # пока в базавом списке есть неиспользованнные символы делай
        randomNum = random.randint(0, len(baseList) - 1)
        randomList.append(baseList[randomNum]) #Наполняю пустой список выбранными символами
        baseList.pop(randomNum) #Удаляю выбранный символ из начального списка
    return randomList

print(shuffleTheList (['s', 'F', '1', '^', 'k', 'N', '1', '*', 'i', 'B']))