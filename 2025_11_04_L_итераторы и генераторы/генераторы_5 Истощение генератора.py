gen = (x for x in range(3))
print(list(gen)) # [0, 1, 2]
print(list(gen)) # [] генератор истощен

gen = (x for x in range(3))
print(sum(gen)) # 3 генератор не выводили, подали в него функцию которая иттерирует объект, то иттератор истощается
print(list(gen)) # [] генератор истощен

gen = (x for x in range(3))
res = list(gen)
print(sum(res))
print(list(res))