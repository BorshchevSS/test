"""
Модуль торговой системы
"""

from enums import Resource
from game_state import GameState


async def trade():
    """
    Функция торговли на текущей планете
    """
    game = GameState.instance()

    print(f"\nТОРГОВЛЯ на {game.ship.current_planet.value}:")
    print("1. Купить ресурсы")
    print("2. Продать ресурсы")
    print("3. Погрузить ресурсы на корабль")
    print("4. Выгрузить ресурсы с корабля")
    print("5. Вернуться в меню")

    try:
        choice = int(input("Ваш выбор (1-5): "))

        if choice == 1:
            await buy_resources()
        elif choice == 2:
            await sell_resources()
        elif choice == 3:
            await load_cargo()
        elif choice == 4:
            await unload_cargo()
        elif choice == 5:
            return

    except ValueError:
        print("[ОШИБКА] Неверный ввод!")


async def buy_resources():
    """Покупка ресурсов на планете"""
    game = GameState.instance()

    print("\nЧто покупаем?")
    for i, resource in enumerate(Resource.get_all(), 1):
        price = game.market.get_price(game.ship.current_planet, resource)
        print(f"{i}. {resource.value} - {price} кредитов")

    try:
        resource_idx = int(input("Выбор ресурса: ")) - 1
        if resource_idx < 0 or resource_idx >= len(Resource.get_all()):
            print("[ОШИБКА] Неверный выбор ресурса!")
            return

        amount = int(input("Количество: "))
        if amount <= 0:
            print("[ОШИБКА] Количество должно быть положительным!")
            return

        resource = Resource.get_all()[resource_idx]
        cost = amount * game.market.get_price(game.ship.current_planet, resource)

        if game.money >= cost:
            game.money -= cost
            game.resources[resource] += amount
            print(f"[ПОКУПКА] Куплено {amount} {resource.value} за {cost} кредитов")
        else:
            print("[ОШИБКА] Недостаточно денег!")

    except ValueError:
        print("[ОШИБКА] Неверный ввод!")


async def sell_resources():
    """Продажа ресурсов на планете"""
    game = GameState.instance()

    print("\nЧто продаём?")
    for i, resource in enumerate(Resource.get_all(), 1):
        price = game.market.get_price(game.ship.current_planet, resource)
        print(f"{i}. {resource.value} - {price} кредитов (на складе: {game.resources[resource]})")

    try:
        resource_idx = int(input("Выбор ресурса: ")) - 1
        if resource_idx < 0 or resource_idx >= len(Resource.get_all()):
            print("[ОШИБКА] Неверный выбор ресурса!")
            return

        amount = int(input("Количество: "))
        if amount <= 0:
            print("[ОШИБКА] Количество должно быть положительным!")
            return

        resource = Resource.get_all()[resource_idx]

        if game.resources[resource] >= amount:
            price = game.market.get_price(game.ship.current_planet, resource)
            income = amount * price

            game.money += income
            game.resources[resource] -= amount
            print(f"[ПРОДАЖА] Продано {amount} {resource.value} за {income} кредитов")
        else:
            print("[ОШИБКА] Недостаточно ресурсов!")

    except ValueError:
        print("[ОШИБКА] Неверный ввод!")


async def load_cargo():
    """Погрузка ресурсов на корабль"""
    game = GameState.instance()

    print("\nЧто грузим на корабль?")
    for i, resource in enumerate(Resource.get_all(), 1):
        print(f"{i}. {resource.value} (на складе: {game.resources[resource]})")

    try:
        resource_idx = int(input("Выбор ресурса: ")) - 1
        if resource_idx < 0 or resource_idx >= len(Resource.get_all()):
            print("[ОШИБКА] Неверный выбор ресурса!")
            return

        amount = int(input("Количество: "))
        if amount <= 0:
            print("[ОШИБКА] Количество должно быть положительным!")
            return

        resource = Resource.get_all()[resource_idx]

        if game.resources[resource] >= amount:
            if game.ship.load_cargo(resource, amount):
                game.resources[resource] -= amount
                print(f"[ПОГРУЗКА] Загружено {amount} {resource.value}")
            else:
                print("[ОШИБКА] Недостаточно места на корабле!")
        else:
            print("[ОШИБКА] Недостаточно ресурсов!")

    except ValueError:
        print("[ОШИБКА] Неверный ввод!")


async def unload_cargo():
    """Выгрузка ресурсов с корабля"""
    game = GameState.instance()

    print("\nЧто выгружаем с корабля?")
    for i, resource in enumerate(Resource.get_all(), 1):
        print(f"{i}. {resource.value} (на корабле: {game.ship.cargo[resource]})")

    try:
        resource_idx = int(input("Выбор ресурса: ")) - 1
        if resource_idx < 0 or resource_idx >= len(Resource.get_all()):
            print("[ОШИБКА] Неверный выбор ресурса!")
            return

        amount = int(input("Количество: "))
        if amount <= 0:
            print("[ОШИБКА] Количество должно быть положительным!")
            return

        resource = Resource.get_all()[resource_idx]

        if game.ship.unload_cargo(resource, amount):
            game.resources[resource] += amount
            print(f"[ВЫГРУЗКА] Выгружено {amount} {resource.value}")
        else:
            print("[ОШИБКА] Недостаточно ресурсов на корабле!")

    except ValueError:
        print("[ОШИБКА] Неверный ввод!")