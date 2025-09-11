import json
import datetime
import os

# Перед началом работы кода выполнить проверку, что файла "notes.json" нет. Если он есть, то не пустой и структура массива соответствует местным требованиям.

#Создание заметки
def creationNote():
    dictNose = {
        "currentTime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "title": input("1. Введи заголовок заметки: "),
        "text": input("2. Введи текст заметки: "),
    }
    return dictNose # заметка будут сохранена в виде словоря

# Чтение заметок из JSON
def readNotesInJson():
    try:
        with open('notes.json', 'r', encoding='utf-8') as file:
            notes = json.load(file)
            # print(notes)
            # если ошибка то создай файл
        return notes
    except FileNotFoundError:
        if input("Отсутствуют сохранённые заметки. Если хотите создать заметку, введите '+': ") == "+":
            addNodeInJson()

#Добавление заметки в файл
def addNodeInJson():
    #Если файл с заметками существует
    if os.path.exists('notes.json') == True:
        newNode = {'numNote': (readNotesInJson()[-1]['numNote'] + 1), 'note': creationNote()}  # Формирую новую заметку
        notes = readNotesInJson()  # Выгружаю массив ранее записанных заметок
        notes.append(newNode)  # Добавляю в массив заметок новую заметку
        with open('notes.json', 'w', encoding='utf-8') as file:
            # Конструкция with open(...) гарантирует, что файл будет корректно закрыт после завершения работы, даже в случае ошибок. Если не делать данную конструкцию, то нужно писать отдельную команду на закрытие файла https://otus.ru/nest/post/975/
            #     w - перезаписывает; если файла нет - создает файл
            #     a - дозаписывает; если файла нет   - создает файл
            #         # encoding = 'utf-8' — для корректной записи кириллицы.
            #         # ensure_ascii=False — для сохранения символов в оригинальном виде.
            #         # indent=4 — для улучшения читаемости файла с отступами.
            json.dump(notes, file, ensure_ascii=False, indent=4)
    # Если НЕТ файла с заметками
    else:
        notes = []
        notes.append({'numNote': 1, 'note': creationNote()}) # Формирую новую заметку
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
    return print(f"Заметка №{notes[-1]['numNote']} с заголовком '{notes[-1]['note']['title']}' успешно создана!")

# Список заметок
def readNotesForPrint ():
    notes = readNotesInJson()
    print("Список доступных заметок:")
    for i in range(len(notes)):
        print(f"Заметка №{notes[i]['numNote']}. Заголовок: {notes[i]['note']['title']}")
    return

# Чтение содержимого одной заметки
def readNoteForPrint ():
    note_selection = input("Какую заметку нужно посмотреть? Введите её номер или заголовок: ")
    notes = readNotesInJson()
    marker = False
    for i in range(len(notes)):
        if ((notes[i]['numNote'] == int(note_selection)) or (notes[i]['note']['title'] == note_selection)):
            print(f"Заметка №{notes[i]['numNote']}.\nВремя создания: {notes[i]['note']['currentTime']} \nЗаголовок: {notes[i]['note']['title']}\nСодержание заметки: {notes[i]['note']['text']}")
            marker = True
    if marker == False:
        print(f"Заявка с номером или заголовком '{note_selection}' отсутствует!")
    return

# Удаление заметки
def dellNote():
    note_selection = input("Какую заметку нужно удалить? Введите её номер или заголовок: ")
    notes  = readNotesInJson()
    index_dell = None
    for i in range(len(notes)):
        if ((notes[i]['numNote'] == int(note_selection)) or (notes[i]['note']['title'] == note_selection)):
            index_dell = i
    notes.pop(index_dell) # Удаление заметки
    with open('notes.json', 'w', encoding='utf-8') as file: # Запись очищенного массива в файл
        json.dump(notes, file, ensure_ascii=False, indent=4)
    if index_dell == None:
        print(f"Заявка с номером или заголовком '{note_selection}' отсутствует!")
    return


while True:
    print(f"""\nВыберете действие:
1. Создать заметку;
2. Просмотр списка заметок;
3. Чтение заметки;
4. Удаление заметки;
0. Выход.
    """)
    try:
        uses_selection = int(input("Введите номер действия: "))
        if uses_selection == 0:
            break
        elif uses_selection == 1:
            addNodeInJson()
        elif uses_selection == 2:
            readNotesForPrint()
        elif uses_selection == 3:
            readNoteForPrint()
        elif uses_selection == 4:
            dellNote()
        else:
            print(f"Вы ввели '{uses_selection}'. Нет такого действия!")
    except ValueError:
        print("Введите число!")


