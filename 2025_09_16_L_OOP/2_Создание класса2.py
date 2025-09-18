class Dog:
    #Свойства класса
    def __init__(self, name_arg, age_arg, breed_arg = "taksa"):
        self.name = name_arg
        self.age = age_arg
        self.breed = breed_arg

    #self это указатель на объект
    def wooff(self, owner):
        print(f"Woof woof say {self.name} ({owner})")

    def __str__(self): #Строковое представление обекта (То, что будет печататься при вызове экземпляра класса)
        return f"{self.name} {self.age} {self.breed}"

dog3 = Dog("Rex", 7)
dog4 = Dog("Bobic", 2, "ovcharca")
dog5 = Dog("Bacs", 4)

print(dog3.name, dog3.age)
#dog4.wooff()
print(dog5) #Что выводится написано в def __str__(self)

owner = "Text"
dog3.wooff(owner)

# dog1 = Dog()
# dog1.name = "Rex"
# print(dog1.name, dog1.age)
# dog1.wooff()