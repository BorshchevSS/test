
from collections import Counter
# Подсчитывает автоматически сколько раз встречается выбранный элемент

с = Counter([1, 2, 2, 3, 3, 3, "aa", "aa", "ad"])
s = Counter("abracadabra")
d = Counter({'a': 5, 'b': 2})
print(с)
print(s)
print(d)

data = ["a", "b", "a", "a", "c", "b"]
cc = Counter(data)
print(cc)
print(cc.most_common(1))
print(cc.most_common(2))

cc.update(["c", "we"])
print(cc)