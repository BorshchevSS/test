#queries.py - выполнение запросов

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from models import User, Product, Order, OrderItem

# Создаем движок и сессию
engine = create_engine('sqlite:///electronics_store.db')
Session = sessionmaker(bind=engine)
session = Session()

print("=" * 60)
print("ЗАПРОС 1: Товары в категории 'Смартфон' с ценой < 50000 рублей")
print("=" * 60)

# Запрос 1: Товары в категории 'Смартфон' с ценой < 50000
smartphones_under_50000 = session.query(Product).filter(
    and_(
        Product.category == "Смартфон",
        Product.price < 50000
    )
).all()

if smartphones_under_50000:
    for product in smartphones_under_50000:
        print(f"ID: {product.id:3} | Название: {product.name:20} | "
              f"Цена: {product.price:10.2f} руб. | "
              f"В наличии: {product.quantity_in_stock} шт.")
else:
    print("Товары не найдены")

print("\n" + "=" * 60)
print("ЗАПРОС 2: Все заказы пользователя с email 'customer@example.com'")
print("=" * 60)

# Запрос 2: Заказы пользователя с определенным email
user_orders = session.query(Order).join(User).filter(
    User.email == "customer@example.com"
).all()

if user_orders:
    for order in user_orders:
        print(f"ID заказа: {order.id}")
        print(f" Дата заказа: {order.order_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" Статус: {order.status}")

        # Дополнительно: выводим товары в заказе
        order_items = session.query(OrderItem).join(Product).filter(
            OrderItem.order_id == order.id
        ).all()

        if order_items:
            print(" Товары в заказе:")
            for item in order_items:
                product = session.query(Product).get(item.product_id)
                print(f" - {product.name}: {item.quantity} шт. x {item.price_at_order:.2f} руб.")
        print("-" * 40)
else:
    print("Заказы не найдены")

# Дополнительные аналитические запросы
print("\n" + "=" * 60)
print("ДОПОЛНИТЕЛЬНЫЕ АНАЛИТИЧЕСКИЕ ЗАПРОСЫ")
print("=" * 60)

# 3. Общая стоимость каждого заказа
print("\n3. Общая стоимость заказов пользователя 'customer@example.com':")
user = session.query(User).filter(User.email == "customer@example.com").first()
if user:
    for order in user.orders:
        total = sum(item.quantity * item.price_at_order for item in order.items)
        print(f"Заказ #{order.id}: {total:.2f} руб. (статус: {order.status})")

# 4. Самый популярный товар
print("\n4. Статистика по товарам:")
from sqlalchemy import func

product_stats = session.query(
    Product.name,
    func.sum(OrderItem.quantity).label('total_sold'),
    func.count(OrderItem.id).label('order_count')
).join(OrderItem).group_by(Product.id).order_by(func.sum(OrderItem.quantity).desc()).all()

print("Товар | Продано шт. | Количество заказов")
print("-" * 50)
for name, total_sold, order_count in product_stats[:5]:  # Топ-5
    if total_sold:
        print(f"{name:30} | {total_sold:10} | {order_count:15}")

session.close()