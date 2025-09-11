# lambda параметр: выражение
l_fun = lambda  x: x**2
print(l_fun(9))

wrds = ["banana", "apple", "cherry", "kiwi"]
sorted_wrds = sorted(wrds, key=lambda word: len(word))
print(sorted_wrds)

sort_wrds = sorted(wrds, key=lambda word: word[-1]) #Сортировка по последней букве
print(sort_wrds)

touple1 = [(1,5), (2,3), (4,1)]
sort_touple1 = sorted (touple1, key=lambda tup: tup[1]) #Сортирует в порядке возрастания по tup[1]
print(sort_touple1)

mul = lambda x,y: x*y
print(mul(2, 4))
