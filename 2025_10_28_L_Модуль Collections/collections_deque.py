#import collections
from collections import deque


# Упрощает работу с данными

# Способы организации данных:
#   LIFO - последний пришел, первый ушел
#   FIFO - первый вошел, первый вышел

d = deque([1, 2, 3]) # Очередь односторонняя/двухсторонная (можно удалять значения с двух сторон)
# append(value) добавление в конец коллекции
# appendleft(value) добавление в начало коллекции

d.append(4)
d.appendleft(0)
print(d)

# pop удаление с конца
# popleft удаление с начала

d.pop()
d.popleft()
print(d)

print(d[0]) # Обращение по индексу

# Ограничение по длине
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
print(d)
print(d[0])
d.append(4)

print(d)
print(d[0])

# Циклический сдвиг/вращение
d.rotate(-1)
print(d)

O(1)
o(n)
O(v^2)
