from abc import ABC, abstractmethod


# ===== Часть 1: Абстракция и наследование =====

class Resource(ABC):
    def __init__(self, name, amount=0):
        self._name = name
        self._amount = amount

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, int):
            value = int(value)
        if value < 0:
            raise ValueError("Количество ресурса не может быть отрицательным")
        self._amount = value

    def __str__(self):
        return f"Resource: {self.name}, amount: {self.amount}"

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать ресурсы разных типов")
        return type(self)(self.name, self.amount + other.amount)


class Wood(Resource):
    def __init__(self, amount=0):
        super().__init__("Wood", amount)


class Food(Resource):
    def __init__(self, amount=0):
        super().__init__("Food", amount)


class Building(ABC):
    def __init__(self, name):
        self.name = name
        self.storage = {}

    @abstractmethod
    def produce(self):
        pass

    @staticmethod
    def calculate_production_cost(resource_type):
        costs = {Wood: 5, Food: 10}
        return costs.get(resource_type, 0)

    @classmethod
    def create_initial_setup(cls, name):
        instance = cls(name)
        # Начальные ресурсы для всех зданий
        instance.storage = {Wood: Wood(10), Food: Food(5)}
        return instance


# ===== Часть 4: Дескрипторы =====

class ResourceLimiter:
    def __init__(self, max_value):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return self.max_value

    def __set__(self, instance, value):
        raise AttributeError("Лимит нельзя изменить после создания")


# ===== Часть 6: Декораторы =====

def log_production(method):
    def wrapper(self, *args, **kwargs):
        print(f"--- НАЧАЛО ПРОИЗВОДСТВА: {self.__class__.__name__} [{self.name}] ---")
        result = method(self, *args, **kwargs)
        print(f"--- ПРОИЗВОДСТВО ЗАВЕРШЕНО: {self.__class__.__name__} ---")
        return result

    return wrapper


# ===== Конкретные классы зданий =====

class Farm(Building):
    max_food = ResourceLimiter(200)

    @log_production
    def produce(self):
        food_production = 20
        current_food = self.storage.get(Food, Food(0)).amount

        if current_food + food_production > self.max_food:
            print(f"Достигнут лимит хранения еды: {self.max_food}")
            food_production = self.max_food - current_food

        if food_production > 0:
            if Food in self.storage:
                self.storage[Food].amount += food_production
            else:
                self.storage[Food] = Food(food_production)
            print(f"Произведено еды: {food_production}")
        else:
            print("Нельзя произвести еду - склад полон")


class LumberMill(Building):
    max_wood = ResourceLimiter(150)

    @log_production
    def produce(self):
        wood_production = 15
        current_wood = self.storage.get(Wood, Wood(0)).amount

        if current_wood + wood_production > self.max_wood:
            print(f"Достигнут лимит хранения древесины: {self.max_wood}")
            wood_production = self.max_wood - current_wood

        if wood_production > 0:
            if Wood in self.storage:
                self.storage[Wood].amount += wood_production
            else:
                self.storage[Wood] = Wood(wood_production)
            print(f"Произведено древесины: {wood_production}")
        else:
            print("Нельзя произвести древесину - склад полон")


# ===== Тестирование =====

if __name__ == "__main__":
    print("=== ТЕСТИРОВАНИЕ СИСТЕМЫ ===\n")

    # Создание экземпляров с помощью метода класса
    print("1. Создание зданий:")
    farm = Farm.create_initial_setup("Green Acres")
    lumber_mill = LumberMill.create_initial_setup("Forest Saw")

    print(f"Ферма создана: {farm.name}")
    print(f"Лесопилка создана: {lumber_mill.name}")
    print(f"Начальные ресурсы фермы: {[f'{k.__name__}: {v.amount}' for k, v in farm.storage.items()]}")
    print(f"Начальные ресурсы лесопилки: {[f'{k.__name__}: {v.amount}' for k, v in lumber_mill.storage.items()]}\n")

    # Сложение ресурсов
    print("2. Сложение ресурсов:")
    wood1 = Wood(50)
    wood2 = Wood(75)
    food1 = Food(30)

    try:
        total_wood = wood1 + wood2
        print(f"Сложение древесины: {wood1.amount} + {wood2.amount} = {total_wood.amount}")

        # Попытка сложить разные типы ресурсов
        invalid_sum = wood1 + food1
    except TypeError as e:
        print(f"Ошибка при сложении разных типов: {e}\n")

    # Проверка сеттера с отрицательным значением
    print("3. Проверка валидации количества ресурса:")
    try:
        wood1.amount = -10
    except ValueError as e:
        print(f"Ошибка при установке отрицательного значения: {e}")

    # Проверка преобразования нецелого числа
    wood1.amount = 25.7
    print(f"Преобразование нецелого числа: 25.7 -> {wood1.amount}\n")

    # Производство ресурсов
    print("4. Производство ресурсов:")
    farm.produce()
    print()
    lumber_mill.produce()
    print()

    # Проверка лимитов
    print("5. Проверка лимитов хранения:")
    # Заполним склады почти до предела
    farm.storage[Food].amount = farm.max_food - 5
    lumber_mill.storage[Wood].amount = lumber_mill.max_wood - 3

    print(f"Еды на ферме перед производством: {farm.storage[Food].amount}/{farm.max_food}")
    print(f"Древесины на лесопилке перед производством: {lumber_mill.storage[Wood].amount}/{lumber_mill.max_wood}\n")

    farm.produce()
    print()
    lumber_mill.produce()
    print()

    # Статический метод
    print("6. Расчет стоимости производства:")
    wood_cost = Building.calculate_production_cost(Wood)
    food_cost = Building.calculate_production_cost(Food)

    print(f"Стоимость производства древесины: {wood_cost}")
    print(f"Стоимость производства еды: {food_cost}")

    print("\n=== ТЕСТИРОВАНИЕ ЗАВЕРШЕНО ===")