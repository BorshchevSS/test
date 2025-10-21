from collections import defaultdict

dd = defaultdict(list) # для группировки данных
dd["a"].append(1)
dd["b"].append(2)
dd["c"].append(3)
dd["a"].append(11)
print(dd)


dd1 = defaultdict(int) # для подсчета элементов
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
for fruit in data:
    dd1[fruit] +=1
print(dd1)

def default_value(): # Только функция без аргументов
    return "значение по умолчанию"

dd2 = defaultdict(default_value) # значение по умолчанию (если нет такого элемента в массиве, то должна быть ошибка keyError, он выдает значение по умолчанию
print(dd2["key"])

# группировка данных
data1 = [("a", 1), ("b", 2), ("a", 3), ("b", 2)]
grouped = defaultdict(list)
for key, value in data1:
    grouped[key].append(value)

print(grouped)