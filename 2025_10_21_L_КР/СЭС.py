from abc import ABC, abstractmethod # Импорт необходимых компонентов

class Resource(ABC):
    """Базовый класс для всех ресурсов."""
    def __init__(self, name: str, amount):
        self.name = name #название ресурса
        self.amount #количество

    @property #Позволяет обращаться к методу как к обычному атрибуту, например obj.attribute, вместо obj.get_attribute()
    def amount(self):
        """Геттер для атрибута amount"""
        return self.amount

    @amount.setter # Метод, который используется для установки или изменения значения атрибута.
    #Внутри сеттер может выполнять дополнительную логику, такую как валидация данных, перед сохранением в приватный атрибут
    def amount(self, value):
        """Сеттер для атрибута amount"""
        if value < 0:
            raise ValueError("Количество не может быть отрицательным")
        if not isinstance(value, int):
            raise ValueError("Значение не является целым числом")
        self.amount = value

    def __str__(self):
        """В классе Resource реализуйте этот метод для удобного строкового представления в формате, например: Resource: Wood, amount: 150"""
        return f"Название: {self.name}, количество: {self.amount} шт."

    def __add__(self, other: 'Resource') -> 'Resource':
        """Объединение двух объектов"""
        """В классе Resource реализуйте перегрузку оператора сложения (+). Сложение двух экземпляров ресурса должно
        создавать новый экземпляр того же типа с суммарным количеством. Если типы ресурсов разные (например, Wood +
        Food), должно быть сгенерировано исключение (TypeError)."""

        if not isinstance(other, Resource):
            raise TypeError("Можно объединять только объекты Resource")

        if self.name != other.name:
            raise ValueError('Разные классы, можно объединять только одинаковые классы')

        new_name = f"Комбо [{self.name} + {other.name}]"
        new_amount = self.amount + other.amount
        new_resource = Resource(new_name, new_amount)
        return new_resource




class Building(ABC):
    """Базовый класс для всех производственных зданий."""
    def __init__(self, name: str, storage: dict):
        self.name = name #название ресурса
        self.storage = storage #хранилище

    @abstractmethod
    def produce(self):
        """абстрактный метод produce(self), который будет реализован в подклассах"""
        pass



class Wood(Resource):
    """Древесина, наследник абстрактного класса Resource"""
    def __init__(self, name: str, amount: int):
        super().__init__(name, amount)

    def __str__(self):
        return f"Название: {self.name}, количество: {self.amount} шт."

    def __repr__(self):
        return f"Wood('{self.name}', '{self.amount}')"


class Food(Resource):
    """Еда, наследник абстрактного класса Resource"""
    def __init__(self, name: str, amount: int):
        super().__init__(name, amount)


    def __str__(self):
        return f"Название: {self.name}, количество: {self.amount} шт."

    def __repr__(self):
        return f"Food('{self.name}', '{self.amount}')"

class Farm(Building):
    """Ферма Farm производит Food, наследуется от здания"""
    def __init__(self, name: str, storage: dict):
        super().__init__(name, storage)

    def produce(self) -> 'Food':
        """Переопределяем метод produce родительского класса"""
        return Food(self.name, self.storage[self.name])

class LumberMill(Building):
    """Лесопильный завод, производит Wood(Древесина), наследуется от здания"""
    def __init__(self, name: str, storage: dict):
        super().__init__(name, storage)

    def produce(self) -> 'Wood':
        return Wood(self.name, self.storage[self.name])

# {'': 10,
#  'Food': 10}
test_1 = Farm('Wood', {"Wood": 10, "Food": 7})
f = test_1.produce()
print(f)

test_2 = Farm("Wood", {"Food": 20, "Wood": 77})
f2 = test_2.produce()
print(f2)

#
# test_3 = LumberMill("Доски", 100)
# f3 = test_3.produce()
# print(f3)

test_4 = f + f2
print(test_4)
# print(test_4)