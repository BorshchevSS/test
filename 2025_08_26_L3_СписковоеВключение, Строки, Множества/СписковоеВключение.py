# Списковое включение
list1 = [2, 4, 5, 6]
list1_1 = [x**2 for x in list1]
list2 = [x**3 for x in range(10)]
list3 = ["2", "4", "5", "6"]
list3_1 = [int(x) for x in list3]
list4 = [x**2 for x in range(10) if x % 2 == 0]
pairs = [(x, y) for x in range(3) for y in range(3)]
print(list1_1)
print(list2)
print(list3_1)
print(list4)
print(pairs)

# [выражение for элемент in иттерируемыОбъект if условие]
# for num in n:
#     list1.append(num**2)
#     print(list1)

list1 = [2, 4, 5, 6]