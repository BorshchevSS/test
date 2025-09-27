"""Умный словарь с историей изменений
Давайте создадим словарь, который:
Запоминает историю всех изменений
Может откатываться к предыдущим состояниям
Поддерживает все стандартные операции словаря"""

class TestClass:
    def __getitem__(self, key):
        pass


class SimpList:
    def __init__(self, items):
        self.items = list(items)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.items[index]

lst = SimpList([1, 2, 3, 4, 5])
print(lst[1])
print(lst[1:4])


class SimpleDict:
    def __init__(self, items):
        self.items = dict(items)

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.items[key]

dct = SimpleDict([("a", "b"), ("c", "d"), ("e", "f")])
print(dct["a"])