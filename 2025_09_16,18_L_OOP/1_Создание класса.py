class Dog:
    #Свойства класса с заданными значениями
    name = "Luna"
    age = 5

    #self это указатель на объект
    def wooff(self):
        print("Woof woof")

dog = Dog()
print(dog.name, dog.age)
dog.wooff()

dog1 = Dog()
dog1.name = "Rex"
print(dog1.name, dog1.age)
dog1.wooff()