#seed.py - наполнение базы данных тестовыми данными

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Product, Order, OrderItem
import random

# Создаем движок и сессию
engine = create_engine('sqlite:///electronics_store.db')
Base.metadata.drop_all(engine)  # Очищаем существующие таблицы
Base.metadata.create_all(engine)  # Создаем таблицы заново

Session = sessionmaker(bind=engine)
session = Session()

# Создаем тестовых пользователей
users_data = [
    {"username": "ivan_tech", "email": "customer@example.com"},
    {"username": "anna_shopper", "email": "anna@example.com"},
    {"username": "petr_gadget", "email": "petr@example.com"},
    {"username": "olga_buyer", "email": "olga@example.com"},
    {"username": "serg_shop", "email": "serg@example.com"},
    {"username": "test_user", "email": "test@example.com"}
]

users = []
for user_data in users_data:
    user = User(**user_data)
    session.add(user)
    users.append(user)

session.commit()

# Создаем тестовые товары
products_data = [
    # Смартфоны
    {"name": "iPhone 15 Pro", "category": "Смартфон", "price": 99999.99, "quantity_in_stock": 50},
    {"name": "Samsung Galaxy S24", "category": "Смартфон", "price": 89999.99, "quantity_in_stock": 40},
    {"name": "Xiaomi 14", "category": "Смартфон", "price": 49999.99, "quantity_in_stock": 60},
    {"name": "OnePlus 12", "category": "Смартфон", "price": 59999.99, "quantity_in_stock": 30},
    {"name": "Google Pixel 8", "category": "Смартфон", "price": 69999.99, "quantity_in_stock": 25},
    {"name": "Realme GT5", "category": "Смартфон", "price": 39999.99, "quantity_in_stock": 45},

    # Ноутбуки
    {"name": "MacBook Pro 16", "category": "Ноутбук", "price": 249999.99, "quantity_in_stock": 20},
    {"name": "Dell XPS 15", "category": "Ноутбук", "price": 159999.99, "quantity_in_stock": 25},
    {"name": "Lenovo ThinkPad X1", "category": "Ноутбук", "price": 129999.99, "quantity_in_stock": 30},

    # Наушники
    {"name": "Sony WH-1000XM5", "category": "Наушники", "price": 29999.99, "quantity_in_stock": 100},
    {"name": "Apple AirPods Pro 2", "category": "Наушники", "price": 24999.99, "quantity_in_stock": 150},
    {"name": "Samsung Galaxy Buds2 Pro", "category": "Наушники", "price": 17999.99, "quantity_in_stock": 120}
]

products = []
for product_data in products_data:
    product = Product(**product_data)
    session.add(product)
    products.append(product)

session.commit()

# Создаем тестовые заказы
statuses = ["в обработке", "оплачен", "отправлен", "доставлен"]

# Заказы для разных пользователей
for i in range(8):  # 8 заказов вместо 5 для разнообразия
    user = random.choice(users)
    order = Order(
        user_id=user.id,
        status=random.choice(statuses)
    )
    session.add(order)
    session.flush()  # Получаем ID заказа

    # Создаем позиции для заказа (от 1 до 4 товаров)
    num_items = random.randint(1, 4)
    selected_products = random.sample(products, num_items)

    for product in selected_products:
        quantity = random.randint(1, 3)
        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=quantity,
            price_at_order=product.price  # Копируем текущую цену
        )
        session.add(order_item)

    session.commit()

print("База данных успешно создана и заполнена тестовыми данными!")
print(f"Создано: {len(users)} пользователей")
print(f"Создано: {len(products)} товаров")

# Проверяем количество заказов
orders_count = session.query(Order).count()
order_items_count = session.query(OrderItem).count()
print(f"Создано: {orders_count} заказов")
print(f"Создано: {order_items_count} позиций в заказах")

session.close()