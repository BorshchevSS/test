# public - доступны извне и внутри
# protected - защищённые/внутренние - условно скрыты для внешнего использования (у наследников доступны)
# private - закрытые свойства (не доступны вне класса даже в наследниках)

class Car:
    def __init__(self, model, year, num="12345"):
        self.model = model
        self.year = year
        self._serial_number = num # Защищенное свойство
        self.__vin_number = None # Приватный метод

    def drive(self):
        print(f"{self.model} is driving")

    def _info_serial_numder(self):
        print(self._serial_number)

car = Car("Toyota", 2019)
print(car.model)
car.drive()

print(car._serial_number)
car._info_serial_numder()
print(car._Car__vin_number)