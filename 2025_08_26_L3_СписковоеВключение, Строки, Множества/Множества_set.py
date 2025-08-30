set1 = {1, 2, 5, 2, 8, 9}
#print(set)

#Объединение/сложение пересечение исключение/вычитание множеств

set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}

print(set3.union(set4)) #Объединение
print(set3 | set4) #объединение

print(set3.intersection(set4)) #пересечение
print(set3 & set4) #пересечение

print(set3.difference(set4)) #вычитание
print(set4.difference(set3)) #вычитание
print(set4 - set3) #вычитание

print(set3.symmetric_difference(set4)) #симметричная разность
print(set4.symmetric_difference(set3)) #симметричная разность
print(set4 ^ set3) #симметричная разность

a = {1, 2, 3, 4}
b = a
a.add(5) #добавление элемента
print(a)

a.remove(2)
print(a)

#a.remove(8) #будет ошибка так как элемента нет

a.discard(8) #Если элемента нет, то ошибки не будет
print(a)

a.clear() #очистка множества
print(a)

a_copy = a.copy()
print(id(a))
print(id(a_copy))

#ошибки не будет (если бы редактировали а, была бы)
for i in a_copy:
    a.add(9)

b = {1, 2}
c = {1, 2, 3, 4, 5}
print(b.issubset(c)) #проверка на подмножества
print(c.issubset(b))
print(c <= b)

print(c.issuperset(b)) #проверка на НАДМНОЖЕСТВО
print(c >= b)

d = {2, 1}
print(b == d)

#Элементами множества может быть ТОЛЬКО неизменяемые типы данных (числа, строки, картежи):
