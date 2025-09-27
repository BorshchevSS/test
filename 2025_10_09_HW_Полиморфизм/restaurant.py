"""Создайте систему для управления заказами в ресторане, используя классы для моделирования блюд и заказов.
1. Реализуйте классы Dish (блюдо) и Order (заказ).
Класс Dish должен содержать информацию о названии и цене блюда.
2. Класс Order должен хранить информацию о нескольких блюдах, которые входят в заказ.
3. Создайте несколько классов-наследников от Dish:
MainDish (основное блюдо), Dessert (десерт) и Drink (напиток).
Пусть у каждого класса будут специфические свойства (например, наличие алкоголя у напитков или вегетарианские блюда).
4. Класс Order должен уметь работать с любыми типами блюд, поддерживая добавление и удаление блюд различных типов в заказ.
5. Перегрузите оператор +, чтобы можно было объединять два объекта Order (суммировать заказы).
6. Перегрузите оператор >, чтобы сравнивать заказы по общей стоимости."""

from typing import List

class Dish:
    """Базовый класс для блюд"""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    """str__ предназначен для создания «приятного» для чтения представления объекта"""
    def __str__(self):
        return f"Название: {self.name} ({self.price})"


    """встроенная функция, которая возвращает строковое представление объекта. 
    Эта строка показывает, как объект выглядит «внутри» — с технической точки зрения. 
    Она создаётся так, чтобы по ней можно было понять, из чего состоит объект, 
    а иногда — использовать её для точного воссоздания объекта в коде."""
    def __repr__(self):
        return f"Dish('{self.name}', {self.price})"


class MainDish(Dish):
    # основное блюдо
    def __init__(self, name: str, price: float, is_vegetarian: bool = False):
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian

    def __str__(self):
        veg_status = " (вегетарианское)" if self.is_vegetarian else ""
        return f"{self.name}{veg_status} - {self.price} руб."

    def __repr__(self):
        return f"MainDish('{self.name}', {self.price}, {self.is_vegetarian})"

# md = MainDish("Оливье", 400, True)
# print(md)
# print(md.__repr__())

class Dessert(Dish):
    """Десерт"""
    def __init__(self, name: str, price: float, contains_gluten: bool = True):
        super().__init__(name, price)
        self.contains_gluten = contains_gluten

    def __str__(self):
        gluten_status = " (без глютена)" if not self.contains_gluten else ""
        return f"{self.name}{gluten_status} - {self.price} руб."

    def __repr__(self):
        return f"Dessert('{self.name}', {self.price}, {self.contains_gluten})"

# des = Dessert("Пирог", 100, False)
# print(des)


class Drink(Dish):
    """Напиток"""
    def __init__(self, name: str, price: float, is_alcoholic: bool = False):
        super().__init__(name, price)
        self.is_alcoholic = is_alcoholic

    def __str__(self):
        alcohol_status = " (алкогольный)" if self.is_alcoholic else ""
        return f"{self.name}{alcohol_status} - {self.price} руб."

    def __repr__(self):
        return f"Drink('{self.name}', {self.price}, {self.is_alcoholic})"



class Order:
    """Класс для управления заказом"""
    """#Класс Order должен хранить информацию о нескольких блюдах, которые входят в заказ."""
    def __init__(self, order_id: int = None):
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

    def __add__(self, other: 'Order') -> 'Order':
        """Объединение двух заказов"""
        if not isinstance(other, Order):
            raise TypeError("Можно объединять только объекты Order")
        new_order = Order()
        new_order.dishes = self.dishes + other.dishes
        return new_order

    def __gt__(self, other: 'Order') -> bool:
        """Сравнение заказов по стоимости"""
        if not isinstance(other, Order):
            raise TypeError("Можно сравнивать только объекты Order")
        return self.get_total_price() > other.get_total_price()

    def __str__(self):
        dishes_str = "\n".join(f"  - {dish}" for dish in self.dishes)
        return f"Заказ #{self.order_id if self.order_id else 'N/A'}:\n{dishes_str}\nИтого: {self.get_total_price()} руб."

    def __repr__(self):
        return f"Order({self.order_id}, dishes={self.dishes})"

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