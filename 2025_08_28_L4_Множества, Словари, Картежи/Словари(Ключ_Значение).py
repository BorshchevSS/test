#создание пустого словоря
dict1 =  {}
dict2 =  dict()

# добавление элемента
dict1["apple"] = "red"
dict1["orange"] = "orange"
print(dict1)

#
print(dict1.keys()) #список ключей словоря
print(dict1.values()) #список значений словоря
print(dict1.items()) #список элементов словоря (элементы словоря картежами представлены)

for k, v in dict1.items():
    print(k)
    print(v)

t = (6, 8)
k, v = t
print(k, v)

#get - получать
a1 = dict1.get("apple", "НетТакогоЗначения") #Возвращает значение (если оно есть), иначе второй аргумент метода
a2 = dict1.get("apple!", "НетТакогоЗначения")

print(a1)
print(a2)
print(len(dict1))

# добавление
dict1.update({"age": 55, "city": "nsk"})
print(dict1)

#Удаление и возвращение удалённого элемента
age = dict1.pop("age") #Удаляет по ключу и возвращает значение; KeyError если элемент не найден
print(age)

#Удаление элемента/объекта
del dict1 ["city"]
print(dict1)