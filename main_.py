# Ctrl + /        Однострочный комментарий
""" Многострочный коментарий """

#Целое число
x = 10       #int
y = 3.5      #float
t = True     #bool
f = False    #bool
s = "stroka" #str

#Массивы бывают
l = []             #list (список, по сути классический массив)
t = (4, 2, 6 )     #tuple Кортеж (неизменяемый список)
se = {4, 6}        #set Множества - неупорядоченный массив
d = {"a":5, "b":6} #dict Словарь это массив состоящий из   "ключь":значение

# Ввод и вывод переменных
name = input("Enter yoy name: ")
age = int(input("Enter you age: "))
age2 = float(input("Enter you age2: "))
print(name)
print(type(name))
print(age)
print(age2)

# Логические операторы и проверка условия
if age > 18:
    print("Совершеннолетний")
elif age >= 18 and age <= 18:
    print("НеСовершеннолетний")
#     and, or, not
else:
    print("Неверный формат данных")

print("Name: ", name, "age: ", age)
print(f"Name: {name}, age: {age}") #

# Математические действия
# + - / * **
# // - целую часть от деления
# % - остаток от деления (ВНИМАНИЕ! если делимое меньше делителя 6 % 9 в ответ будет делитель 6 отображаться)


# Циклы (for...; while...)
for i in range(10): #(let i=0; i<10; i++) -
    print(i)
        #range(n, k, step)
        # n - начало диапазона(по умолчанию = 0);
        # k - конец диапазона не включая значение
        # step - шаг (по умолчанию = 1)


    #Строка это изменяемый тип данных (если меняешь значение переменной то меняется её ID)
a = "hello"
print(id(a))
b = "hello"
print(id(b))
a = "hello!"
print(id(a))

str1 = "abcdefg"
print(str1)
print(str1[0]) #первый символ

for char in str1:
    print(char) #перебор значений в строке

for ch in range(len(str1)):
    print(f"{ch}_{str1[ch]}")

count = 1
while count < 10:
    print(count)
    count += 1

while count < 20:
    print(count)
    count += 1
    if count == 5:
        break #остановка цикла

while count < 20:
    if count == 2 or count == 10 or count == 2:
        count += 1
        continue #прерывается операция и все что ниже нее было (все что ниже работать не будет) но цикл не останавливается
    print(count)
    count += 1

#Обработка исключений(ошибок)
    # ValueError, FileNotFoundError, TypeError, ZeroDivisionError

try: #код, который попытается выполниться
    print(10/age)
except ZeroDivisionError: #код, который будет выполняться если есть ошибка
    print("Делить на ноль нельзя")
except KeyboardInterrupt: #код, который будет выполняться если есть ошибка
   print("Введи значение")
except ValueError:
    print("Введи значение")