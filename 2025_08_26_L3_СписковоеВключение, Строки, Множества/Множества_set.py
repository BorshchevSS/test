set = {1, 2, 5, 2, 8, 9}
#print(set)

#Объединение/сложение пересечение исключение/вычитание множеств

set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}

print(set3.union(set4)) #Объединение
print(set3.intersection(set4)) #пересечение
print(set3.difference(set4)) #вычитание
print(set4.difference(set3)) #вычитание