'''Поиск слов в тексте
Задание:
• Дана книга в файле book.txt.
• Напиши функцию word_count(filename), которая возвращает количество всех слов в книге.
• Напиши функцию find_word(filename, word), которая возвращает, сколько раз встречается указанное слово (без учёта регистра).
• Напиши функцию save_statistics(filename), которая создаёт файл stats.txt с результатами анализа (общее количество слов, топ-5 самых частых слов).

Дополнительно: исключить стоп-слова (например: "и", "в", "на", "с").'''
import os
import glob
from collections import Counter

#Поиск и выбор нужного файла, функция выгружает его содержимое
def searchFile(fileName):
    # Рекурсивный поиск в подпапках
    files_recursive = glob.glob(f"**/{fileName}*", recursive=True)  # ** ищет во всех подкаталогах
    #files_current = glob.glob("book*")  # Ищем все файлы в текущем каталоге, начинающиеся на "book..."
    text = ""
    print(f"Файлы '{fileName}' в подпапках:", files_recursive)
    id_file = None
    if len(files_recursive) > 0:
        print("Список доступных файлов:")
        for i in range(len(files_recursive)):
            print(f"{i+1}. {files_recursive[i]}")

        #Обработка ошибки ввода (число вне диапазона и текст)
        while True:
            nomer_file = input(f"Выберете номер файла для просмотра: ")
            try:
                id_file = int(nomer_file) - 1
                if id_file >= 0 and id_file <= (len(files_recursive)-1):
                    break
                else:
                    print(f"Введите число от 1 до {len(files_recursive)}")
            except:
                print("Введите число!")
    else:
        print(f"Файла с названием '{fileName}' в текущем каталоге и подкаталогах нет!")
    fileName = files_recursive[id_file]

    with open(fileName, 'r', encoding='utf-8') as file:
        textInFile = file.read()
    return textInFile

#Подсчитывает количество слов в предложении
def word_count(fileName):
    text = searchFile(fileName)
    return len(text.split())

#Возвращает, сколько раз встречается указанное слово (без учёта регистра)
def find_word(fileName, word):
    word_lower = word.lower() #Перевод ключевого слова в нижний регистр
    text = searchFile(fileName) #Подгружаю текст из файла
    text_lower = text.lower()
    # Считаем количество вхождений слова
    count = text_lower.count(word_lower)
    print(f"Слово '{word}' встречается {count} раз (без учета регистра).")
    return count
#find_word("book", "Я")


#Напиши функцию save_statistics(filename), которая создаёт файл stats.txt с результатами анализа (общее количество слов, топ-5 самых частых слов)
def save_statistics(fileName):
    text = searchFile(fileName)
    textList = text.split() #Разделяю строку на слова по разделителю ПРОБЕЛ
    #print(textList)
    textListClean = list() # Пустой массив, в цикле ниже наполню его строками без лишних символов
    for word in textList:
        if len(word.strip(",.!?:;—()")) > 0: # Избавляюсь от пустых строк в массиве
            textListClean.append(word.strip(",.!?:;—()").lower()) # Убираю лишние символы, меняю геристр на нижний
    list_wordAndQuantity = Counter(textListClean) # получения словаря частот всех элементов {слово; частота появления}
    print(list_wordAndQuantity)
    textStat = f"В файле {fileName}:\nВсего слов: {len(textList)};\n{list_wordAndQuantity}"

    #Сохранение файла со статистикой
    with open("stats.txt", 'w', encoding='utf-8') as file:
        file.write(textStat)

save_statistics("book.txt")

