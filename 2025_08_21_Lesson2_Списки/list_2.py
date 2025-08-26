nums = ["10",  "20", "55", "32", "88"]
#Объединение. Из списка сделать ОДНУ строку (если там только строковые значения, на числах ошибка)
print("".join(nums))
print(", ".join(nums))

#len() длина
print(len(nums))

#Массивы
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[2][1])

#Перебор без индексации
for n in matrix:
    print(n)

for n in matrix:
    for m in n:
        print(m)

#С индексацией
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])

# MemoryError - пытается добавлять значения в список бесконечно
# RuntimeError - Удаление элемента из списка
# IndexError - обращаемся к элементу, которого нет в списке


