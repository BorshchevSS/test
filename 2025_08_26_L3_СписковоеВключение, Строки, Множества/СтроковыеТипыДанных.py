str1 = "превысокомногорассмотрительствующий123467890"
# str1[0] = "x" #ERROR будет; строки менять НЕЛЬЗЯ, можно создать новый
# print(str1[0])
# print(str1[3:10:2])
# print(str1[-1])
# print(str1[::-1]) #развернул строку
# print(len(str1))

str2 = "Hello? World! "
# Удаляем пробелы в начале и конце строки (ошибочный ввод пользователя)
print(str2.strip())

#Поиск строки. Результат: "-1" если не найдено, либо индекс вхождения
pos = str2.find("World") #Ошибки не будет если значение не найдено (значение будет "-1") Если значение найдено, то возвращает его позиция
print(pos)

#Изменение регистра
print(str2.upper()) #все верхний регистр
print(str2.lower()) #все в низкий регистр
print(str2.title())  #Первая буква слова заглавная
print(str2.capitalize()) #Первый символ в строке переводит в верхний регистр

#Разделение строки
#
print(str2.split())
print(str2.strip().split(", "))
print(", ".join(str2))

#Конкотенация, умножение строк
print("q" + "w" + "e")
print("q"*4)

num = 25
print("q" + str(num) + "e")

#f"строки" или интерполяция(внедрение)
print(f"List: {str1.upper()}")

#Проверка регистра
print("HHHhhh".isupper()) #Является ли строка вся в верхнем регистре
print("Hhhh".isupper()) #Является ли строка вся в верхнем регистре
print("HHH".isupper()) #Является ли строка вся в верхнем регистре
# isupper(), islower(), istitle(), iscapitalize()

#Проверка все буквы
print("Hello".isalpha())
print("Hello123".isalpha())
print("Привет".isalpha())
print("".isalpha())

#Или цифры или буквы
print("666".isalnum())
print("666aaa".isalnum())
print("666!".isalnum())

print("123".isdecimal()) #Десятичные цифра
print("1.3".isdecimal()) #Десятичная цифра
print("1,3".isdecimal()) #Десятичная цифра
print("IV".isdecimal()) #Десятичная цифра