#Целевой интерфейс
from abc import ABC, abstractmethod


class PetInfo(ABC):
    @abstractmethod
    def get_info(self):
        pass

#Адаптируемый объект
class CoolAnimalLibrary:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    #Несовместимный метод который нужно адаптировать
    def get_details(self):
        return f"Animal Detailes: {self.type}, {self.name}"


class AnimalAdapter(PetInfo):
    def __init__(self, animal):
        self.animal = animal

    #Переопределяем
    def get_info(self):
        raw_details = self.animal.get_details()
        return raw_details

#Клиентский код
def show_pet_info(pet):
    print(pet.get_info())

cat = CoolAnimalLibrary("Timoxa", "cat")
adapt_cat = AnimalAdapter(cat)

show_pet_info(adapt_cat)