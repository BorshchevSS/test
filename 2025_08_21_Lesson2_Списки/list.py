list1 = [] #Список, изменяемый тип данных
list2 = list() #Преобразование переменной в список
print(list1)
list1.append(5)
list1.append(3)
list1.append(1)
list1.append(0)
list1.append(-2)
list1.append(-4)
print(list1)
print(list1[0])

list1[0] = 55
print(list1[0])

#Срезы
# range(n, k, step)
# n - начало диапазона(по умолчанию = 0);
# k - конец диапазона не включая значение
# step - шаг (по умолчанию = 1)

print(list1[1:6:2])
print(list1[-1])
print(list1[-1:-6:-2])
print(list1[:6])
print(list1[3::])# с третьего и далее
print(list1[::-1])#в обратном порядке

list3 = [1, 11, 1, 11, 10]
print(list3.remove(1)) #удаление первого элемента
#pop() удаление с конца (по индексу) с возвращфемым значением

print(list1.extend(list2))  #Объединение списков

# sort - сортировка однородного списка
print(list1.sort())

list1.reverse() #Перевернуть