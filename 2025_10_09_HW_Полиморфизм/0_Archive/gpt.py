from typing import List, Union


class Dish:
    """Базовый класс для блюд"""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} руб."

    def repr(self):
        return f"Dish('{self.name}', {self.price})"


class MainDish(Dish):
    """Основное блюдо"""

    def init(self, name: str, price: float, is_vegetarian: bool = False):
        super().init(name, price)
        self.is_vegetarian = is_vegetarian

    def str(self):
        veg_status = " (вегетарианское)" if self.is_vegetarian else ""
        return f"{self.name}{veg_status} - {self.price} руб."

    def repr(self):
        return f"MainDish('{self.name}', {self.price}, {self.is_vegetarian})"


class Dessert(Dish):
    """Десерт"""

    def init(self, name: str, price: float, contains_gluten: bool = True):
        super().init(name, price)
        self.contains_gluten = contains_gluten

    def str(self):
        gluten_status = " (без глютена)" if not self.contains_gluten else ""
        return f"{self.name}{gluten_status} - {self.price} руб."

    def repr(self):
        return f"Dessert('{self.name}', {self.price}, {self.contains_gluten})"


class Drink(Dish):
    """Напиток"""

    def init(self, name: str, price: float, is_alcoholic: bool = False):
        super().init(name, price)
        self.is_alcoholic = is_alcoholic

    def str(self):
        alcohol_status = " (алкогольный)" if self.is_alcoholic else ""
        return f"{self.name}{alcohol_status} - {self.price} руб."

    def repr(self):
        return f"Drink('{self.name}', {self.price}, {self.is_alcoholic})"


class Order:
    """Класс для управления заказом"""

    def init(self, order_id: int = None):
        self.order_id = order_id
        self.dishes: List[Dish] = []

    def add_dish(self, dish: Dish) -> None:
        """Добавить блюдо в заказ"""
        self.dishes.append(dish)

    def remove_dish(self, dish_name: str) -> bool:
        """Удалить блюдо из заказа по названию"""
        for i, dish in enumerate(self.dishes):
            if dish.name == dish_name:
                self.dishes.pop(i)
                return True
        return False

    def get_total_price(self) -> float:
        """Получить общую стоимость заказа"""
        return sum(dish.price for dish in self.dishes)

    def add(self, other: 'Order') -> 'Order':
        """Объединение двух заказов"""
        if not isinstance(other, Order):
            raise TypeError("Можно объединять только объекты Order")

        new_order = Order()
        new_order.dishes = self.dishes + other.dishes
        return new_order

    def gt(self, other: 'Order') -> bool:
        """Сравнение заказов по стоимости"""
        if not isinstance(other, Order):
            raise TypeError("Можно сравнивать только объекты Order")

        return self.get_total_price() > other.get_total_price()

    def str(self):
        dishes_str = "\n".join(f"  - {dish}" for dish in self.dishes)
        return f"Заказ #{self.order_id if self.order_id else 'N/A'}:\n{dishes_str}\nИтого: {self.get_total_price()} руб."

    def repr(self):
        return f"Order({self.order_id}, dishes={self.dishes})"


# Демонстрация работы системы
if __name__ == "__main__":
    # Создаем блюда
    steak = MainDish("Стейк Рибай", 1200, is_vegetarian=False)
    salad = MainDish("Греческий салат", 450, is_vegetarian=True)
    cake = Dessert("Чизкейк", 350, contains_gluten=True)
    ice_cream = Dessert("Мороженое", 200, contains_gluten=False)
    cola = Drink("Кола", 150, is_alcoholic=False)
    wine = Drink("Красное вино", 600, is_alcoholic=True)

    # Создаем заказы
    order1 = Order(1)
    order1.add_dish(steak)
    order1.add_dish(salad)
    order1.add_dish(wine)

    order2 = Order(2)
    order2.add_dish(cake)
    order2.add_dish(ice_cream)
    order2.add_dish(cola)

    # Выводим заказы
    print("=== ЗАКАЗ 1 ===")
    print(order1)
    print("\n=== ЗАКАЗ 2 ===")
    print(order2)

    # Объединяем заказы
    combined_order = order1 + order2
    combined_order.order_id = 3
    print("\n=== ОБЪЕДИНЕННЫЙ ЗАКАЗ ===")
    print(combined_order)

    # Сравниваем заказы
    print("\n=== СРАВНЕНИЕ ЗАКАЗОВ ===")
    print(f"Заказ 1 > Заказ 2: {order1 > order2}")
    print(f"Заказ 2 > Заказ 1: {order2 > order1}")
    print(f"Объединенный заказ > Заказ 1: {combined_order > order1}")

    # Удаляем блюдо из заказа
    print("\n=== УДАЛЕНИЕ БЛЮДА ИЗ ЗАКАЗА ===")
    order1.remove_dish("Стейк Рибай")
    print("После удаления стейка:")
    print(order1)

"""
Эта реализация включает:

1. Базовый класс Dish с названием и ценой
2. Классы-наследники:
   - `MainDish` с флагом вегетарианского блюда
   - `Dessert` с флагом содержания глютена
   - `Drink` с флагом алкогольного напитка

3. Класс Order с методами:
   - Добавление/удаление блюд
   - Расчет общей стоимости
   - Перегрузка оператора `+` для объединения заказов
   - Перегрузка оператора `>` для сравнения по стоимости

4. Демонстрация работы с созданием блюд, формированием заказов, их объединением и сравнением.

Система легко расширяема - можно добавлять новые типы блюд, наследуясь от класса Dish, и они автоматически будут работать с классом Order.
"""