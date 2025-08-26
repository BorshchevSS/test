"""Задача 2. «Перепутанные слова»
1. 2. 3. 4. Заранее создать список слов, например: ["python", "список", "цикл", "игра", "число"].
Программа выбирает случайное слово и перемешивает буквы.
Пользователь должен угадать исходное слово.
Если угадал – выводим «Верно!», иначе показываем правильный ответ."""
import random                      #random.randint()

#словарь содержит "ключь"(номер слова) и "значение"(само слово)
dict_Num_Word = {
    1: "python",
    2: "список",
    3: "цикл",
    4: "игра",
    5: "число",
}

#Выбираем случайное число из доступного диапазона "ключей" словоря; на основании него подтягиваем "значение" из словоря
numRandomWord = random.randint(min(dict_Num_Word.keys()), max(dict_Num_Word.keys())) #случайное число из перечня ключей
randomWord = dict_Num_Word[numRandomWord] #Значение из словоря
# print(dict_NumDay_AmountHour.keys())
# print(numRandomWord)
#print(f"Из словоря выбрано слово:'{dict_Num_Word[numRandomWord]}'")
# print(len(dict_NumDay_AmountHour))
# print(dict_NumDay_AmountHour.values())

randomLettersInRandomWord = [] #пустой список(list) в которы мы положим символы
listLetters_RandomWord = list(randomWord) #разбираю "randomWord" на список символов

#print(f"Разбираю слово '{randomWord}' на список символов: {listLetters_RandomWord}") #разбираю строку на список символов

while len(randomLettersInRandomWord) < len(randomWord): #пока кол-во символов в создаваемом списке меньше исходного делай
    randomNum = random.randint(0, len(listLetters_RandomWord)-1)
    # print(randomNum)
    randomLettersInRandomWord.append(listLetters_RandomWord[randomNum]) #Наполняю пустой список выбраными символами
    listLetters_RandomWord.pop(randomNum) #Удаляю выбранный символ из начального списка
#print(randomLettersInRandomWord)

#print("___")
print(f"Есть слова: {dict_Num_Word}")

# Запрос у пользователя зашифрованного слова. Проверка введёного значения
while True:
    try:
        selectNum = int(input(f'В наборе символов "{"".join(randomLettersInRandomWord)}" зашифровано одно из них. Какое? Введи его номер: '))
        if selectNum <= 0:
            print("Введи положительное число")
            continue
        break
    except ValueError:
        print("Введи целое число")

#Проверка результата
if selectNum == numRandomWord:
    print(f"Поздравляем, Вы угадали!")
else:
    print(f"Неудачная попытка. В наборе символов '{"".join(randomLettersInRandomWord)}' зашифровано слово под №{numRandomWord} ({randomWord}). Вы ошибочно выбрали слово под №{selectNum} ({dict_Num_Word[selectNum]}).")
