"""Задача 2:
Создайте программу для управления реестром участников мероприятия, используя кортежи, множества и словари.
Пользователь должен иметь возможность регистрировать новых участников, удалять их из реестра и просматривать полный список с деталями.

Указания:
1. Программа должна начинаться с пустого словаря участников.
2. Ключом в словаре должен быть кортеж, состоящий из имени и фамилии участника, а значением — множество с их интересами.
3. Пользователь может добавить нового участника в реестр, используя команду add.
4. Пользователь может удалить участника из реестра, используя команду remove.
5. Пользователь может просмотреть всех участников с их интересами, используя команду list.
6. Пользователь может выйти из программы, используя команду exit.
7. Программа должна обеспечивать обработку ошибок ввода, таких как запрос удаления несуществующего участника.

Ожидаемый результат:
Программа циклически запрашивает у пользователя команду (add, remove, list или exit для выхода),
выполняет ееи затем снова запрашивает команду. Программа должна корректно обрабатывать каждую команду и выдавать
соответствующие сообщения о статусе операции."""

#1. Программа должна начинаться с пустого словаря участников.
#dictUsers = {} #dictUsers = {(nameUser, surnameUser ): mySet}
dictUsers = {('Саша', 'Александров'): {'плаванье'}, ('Дима', 'Типсин'): {'литрабол', 'хоккей', 'мотоспорт'}, ('Виталий', 'Батманов'): {'стрельба', 'автогонки'}} #тесторый словать создан на время тестирования кода

#Функция addUserName () запрашивает и проверяет ФО участника
def addUserName ():

    # Добавляю имя
    while True:
        nameUser = input(f"Введите имя пользователя: ")
        if len(nameUser) < 2:
            print(f"Вы ввели '{nameUser}', необходимо что бы в имени было минимум 2 символа")
            continue
        #tupleNameSurname = nameUser
        break

    # Добавляю фамилию
    while True:
        surnameUser = input(f"Введите фамилию пользователя: ")
        if len(surnameUser) < 2:
            print(f"Вы ввели '{surnameUser}', необходимо что бы в фамилии было минимум 2 символа")
            continue
        #tupleNameSurname = surnameUser
        break
    tupleNameSurname = tuple([nameUser, surnameUser])   # кортеж (nameUser, surnameUser). Делаю список, который скармливаю картежу, иначе ошибка.
    return tupleNameSurname # кортеж (nameUser, surnameUser)

#Функция addInteres () запрашивает и проверяет интересы/скилы участника
def addInteres ():
    setInterests = set() # создаю пустое множество, которое ниже заполню
    while True:
        #Ввод и проверка
        interes = input(f"Введите чем интересуется пользователь, его Soft and Hard skills: ")
        if len(interes) < 3:
            print(f"Вы ввели '{interes}', необходимо что бы в наименовании скила было минимум из 3 символа")
            continue
        setInterests.add(interes)

        # Выход из цикла
        addNewInteres = input("Добавить еще один скил/интерес? Если да, нажмите '+' или '1'. Если нет, введите любой символ: ")
        if addNewInteres == "+" or addNewInteres == "1":
            pass
        else:
            break
    return setInterests # набор в виде множества интересов {интерес№1, интерес№2,...}

#Функция print (numOrAll) принимает ИНДЕКС участника и покажет его свойства; если подать на вход ALL покажет весь список
def printUserAndInteres (numOrAll):
    userAndInteres = ""
    if type(numOrAll) == type(1):
        userName = list(dictUsers.keys())[numOrAll]
        userAndInteres = f"{numOrAll+1}. Имя и Фамилия участника: {userName[0]} {userName[1]}, увлечение(я): {dictUsers[userName]}"
    else:
        # весь список
        for i in range(len(dictUsers)):
            userName = list(dictUsers.keys())[i]
            userAndInteres += f"{i+1}. Имя и Фамилия участника: {userName[0]} {userName[1]}, увлечение(я): {dictUsers[userName]} \n"
    return userAndInteres

# Удаление пользователя
def deleteUser ():
    indexUserForDelete = None # Сюда запишем индекс удаляемого элемента
    while True:
        try:
            numUserForDelete = int(input(f"Список участников: \n{printUserAndInteres("All")}Введите номер участника для удаления: "))
            if numUserForDelete < 1 or numUserForDelete > (len(dictUsers)):
                print(f"Вы ввели '{numUserForDelete}', число вне диапазона [1; {(len(dictUsers))}]. Попробуем еще раз!")
                continue
            indexUserForDelete = numUserForDelete - 1
            break
        except ValueError:
            print(f"Введи целое число")
    dellUserForHistoru = printUserAndInteres (indexUserForDelete)
    dictUsers.pop(list(dictUsers.keys())[indexUserForDelete])
    print(f"Участник: {dellUserForHistoru} успешно удалён!")


def menu ():
    while True:
        print(f"""Внесите информацию в программу для управления реестром участников мероприятия.
    1. Для добавления нового участника в реестр введите 'add' или '1';
        2. Для удаления участника из реестра, используя команду 'remove' или '2';
            3. Для просмотра всех участников с их интересами используйте команду 'list' или '3'
                4. Для выхода из программы, используя команду 'exit' или '0'.
""")
        actionMenu = input("Введите код или номер команды: ")

        if actionMenu == 'add' or  actionMenu == '1':
            key = addUserName ()
            dictUsers[key] = addInteres ()
            print(f"Участник №{printUserAndInteres(len(dictUsers)-1)} успешно добавлен!")
        elif actionMenu == 'remove' or  actionMenu == '2':
            deleteUser ()
        elif actionMenu == 'list' or  actionMenu == '3':
            print(printUserAndInteres("All"))
        elif actionMenu == 'exit' or  actionMenu == '0':
            break
        else:
            print(f"Команда '{actionMenu}' отсутствует в предложенном меню. Попробуйте еще раз.")
    return

print(menu())