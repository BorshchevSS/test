"""Задание 2. Подсчёт продуктов, группировка по категориям
Ситуация: мы работаем над приложением для продуктового магазина.
У нас есть список покупок, где каждый элемент представляет собой кортеж (категория, продукт). Нам нужно сгруппировать продукты по
категориям, чтобы упростить подсчёт.
Задача — реализовать функцию group_products_by_category(items), которая принимает список кортежей (категория, продукт) и
возвращает словарь, где ключи — категории, а значения — списки продуктов. Использовать defaultdict для упрощения группировки."""

from collections import defaultdict

def group_products_by_category(items): #items - список картежей
    grouped_products = defaultdict(list)
    for category, products in items:
        grouped_products[category].append(products)
    return grouped_products

shopping_list = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("fruit", "apple"),
    ("овощи", "помидор"),
    ("овощи", "помидор"),
    ("овощи", "огурец"),
]

for item in shopping_list:
    print(item)
result = group_products_by_category(shopping_list)
print(result)

for category, products in result.items():
    print(f"Категория: {category}")
    print(f"    Продукты: {", ".join(products)}")