#Полиморфизм через наследование (объект ведёт себя по разному в зависимости от какого класса дочернего он вызывается)
class Animal:
    def spek(self):
        pass

class Dog(Animal):
    def spek(self):
        return "гав"

class Cat(Animal):
    def spek(self):
        return "мяу"

#Пример полиморфизма. Метод spek() ведёт себя по разному в зависимости от какого класса вызывается
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.spek())


#Полиморфизм №2. Один и тот же метод у разных классов выдаст разные результаты (главное что бы этот метод в классах был)
class Human:
    def speak(self):
        return "Hello"

class Duck:
    def speak(self):
        return "Krya"

def make_sound(object):
    print(object.speak())

make_sound(Human())
make_sound(Duck())

# Полиморфизм №3.1 через перегрузку операторов

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Поменяли поведение метода "+" для данного класса (метод __add__ отвечает за сложение, см. "некоторые магические методы.pdf")
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x}, {self.y}"


v1 = Vector(2,3)
v2 = Vector(2,7 )

v3 = v1 + v2
print(v3)