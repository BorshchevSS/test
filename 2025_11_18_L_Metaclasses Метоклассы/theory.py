class MyClass:
    def get_info(self):
        return  "Класс обязательного наследования"

class MyClass2(type):
    def __new__(cls, name, bases, attrs):
        if MyClass not in bases:
            new_bases = (MyClass, ) + bases # сложение списков
            print("Добавлен обязательный класс")
        else:
            new_bases = bases

        return super().__new__(cls, name, new_bases, attrs)

class UseClass(metaclass=MyClass2):
    def hi(self):
        return "Hello"

use = UseClass()
print(use.hi())
print(use.get_info()) #Вызываем метод родителя (use унаследовал)