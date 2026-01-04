from abc import ABC, abstractmethod

#Product
class Car:
    def __init__(self):
        self.parts = {}

    def add_part(self, name, value):
        self.parts[name] = value

    def __str__(self):
        parts_list = "\n".join(f"{name}: {value}" for name, value in self.parts.items())
        return f"Готовый автомобиль: {parts_list}"

# Builder
class CarBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_engine(self, type_engine):
        pass

    @abstractmethod
    def set_wheel(self, number):
        pass

    @abstractmethod
    def get_result(self):
        pass

# Concrete Builder
class SportCarBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._car = Car()

    def set_engine(self, type_engine="diesel"):
        self._car.add_part("engine", type_engine)
        return self

    def set_wheel(self, number=4):
        self._car.add_part("whell", number)
        return self

    def get_result(self):
        car = self._car
        self.reset() #Очищаем для следующей сборки
        return car

class Director:
    def __init__(self, builder: CarBuilder):
        self._builder = builder

    def builder_full_featured(self):
        return self._builder.set_engine("diesel Turbo").set_wheel().get_result() #Цепочка вызовов, работает если в return self

builder = SportCarBuilder()
director = Director(builder)
sport_cat = director.builder_full_featured()
print(sport_cat)