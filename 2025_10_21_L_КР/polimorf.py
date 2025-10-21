# полиморфизм через наследование
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return 'гав'

class Cat(Animal):
    def speak(self):
        return 'мяу'

# animals = [Dog(), Cat()]
# for animal in animals:
#     print(animal.speak())


# DuckTyping
class Human:
    def speak(self):
        return 'Hello'

class Duck:
    def speak(self):
        return 'Krya'

def make_sound(object):
    print(object.speak())

# make_sound(Human())
# make_sound(Duck())
#
#через перегрузку операторов
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'{self.x}, {self.y}'

v1 = Vector(2, 3)
v2 = Vector(2, 7)
v3 = v1 + v2
# print(v3)
# print(5 + 2)















