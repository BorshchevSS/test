print(f"""1. Пользователь вводит с клавиатуры некоторый текст, после чего пользователь вводит список
зарезервированных слов. Необходимо найти в тексте все зарезервированные слова и изменить их регистр на
верхний. Вывести на экран измененный текст.\n""")

#inputText = input("Введите с клавиатуры некоторый текст: ")
#inputKeyWord = input("Введите через запятую список зарезервированных слов (они будут заменены на верхний регистр): ")

inputText = "Вот дом, который построил Джек. А это пшеница, которая в темном чулане хранится в доме, который построил Джек. А это веселая птица-синица, которая часто ворует пшеницу, которая в темном чулане хранится в доме, который построил Джек!"
inputKeyWord = "Джек, Дом, доме, пшеница; пшеницу; который, которая"



listInputText = inputText.split() # разбивает строку на СПИСОК подстрок по заданному разделителю (в нашем случае, пробелу)


# Строку с "зарезервированные слова" превращаю в строку и убираю запятые
listInputKeyWord = inputKeyWord.split() # строку в список
listInputKeyWord = [listInputKeyWord[x].strip(",;") for x in range(len(listInputKeyWord))] # убираю лишние символы (запятые)

listInputText_AccentuatedKeyWord = [] # список с измененными строками
for i in range(len(listInputText)):
    markerCaseChange = False
    for j in range(len(listInputKeyWord)): # внутренний цикл для сравнения слова в исходном тексте со списком заданныхСлов
        if listInputText[i].strip('.,!&?^-').lower() == listInputKeyWord[j].lower():
            markerCaseChange = True
    if markerCaseChange:
        listInputText_AccentuatedKeyWord.append(listInputText[i].upper())
    else:
        listInputText_AccentuatedKeyWord.append(listInputText[i])

listInputText_AccentuatedKeyWord = " ".join(listInputText_AccentuatedKeyWord)

print(f"Исходны текст: {inputText}\n")
print(f"Cписок зарезервированных слов: {inputKeyWord}\n")
print(f"Отредактированный текст: {listInputText_AccentuatedKeyWord}")