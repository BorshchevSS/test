import threading
import asyncio
import multiprocessing
import time
import random
from enum import Enum
from typing import Dict, List, Tuple
import sys


# ==================== ENUMS AND CONSTANTS ====================
class Resource(Enum):
    ENERGY = "Энергия"
    METAL = "Металл"
    CRYSTALS = "Кристаллы"
    PARTS = "Запчасти"


class Planet(Enum):
    ICE_9 = "Лёд-9"
    FIREWORLD = "Огневик"
    MECHANICUS = "Механикус"
    NEUTRAL = "Нейтральная"


class MineType(Enum):
    ENERGY = "Энерго-шахта"
    DEEP = "Глубинная"
    EXPERIMENTAL = "Экспериментальная"


# ==================== THREADING: MINES ====================
class Mine(threading.Thread):
    def __init__(self, mine_id: int, mine_type: MineType):
        super().__init__(daemon=True)
        self.mine_id = mine_id
        self.mine_type = mine_type
        self.level = 1
        self.is_running = True
        self.is_broken = False
        self.is_upgrading = False
        self.resource_type = self._get_resource_type()
        self.production_rate = self._get_base_rate()
        self.last_breakdown = time.time()
        self.breakdown_interval = random.randint(30, 90)

    def _get_resource_type(self) -> Resource:
        if self.mine_type == MineType.ENERGY:
            return Resource.ENERGY
        elif self.mine_type == MineType.DEEP:
            return Resource.METAL
        else:  # EXPERIMENTAL
            return random.choice([Resource.CRYSTALS, Resource.PARTS])

    def _get_base_rate(self) -> int:
        if self.mine_type == MineType.ENERGY:
            return 5
        elif self.mine_type == MineType.DEEP:
            return 2
        else:  # EXPERIMENTAL
            return 1

    def run(self):
        while self.is_running:
            if not self.is_broken and not self.is_upgrading:
                # Производство ресурсов
                GameState.instance().add_resource(self.resource_type, self.production_rate)
                time.sleep(1)

                # Проверка на поломку
                if time.time() - self.last_breakdown > self.breakdown_interval:
                    if random.random() < 0.3:  # 30% шанс поломки
                        self.is_broken = True
                        print(f"[АВАРИЯ] Шахта #{self.mine_id} ({self.mine_type.value}) сломалась!")
            else:
                time.sleep(0.5)

    def repair(self, parts_available: int) -> bool:
        if self.is_broken and parts_available >= 10:
            self.is_broken = False
            self.last_breakdown = time.time()
            self.breakdown_interval = random.randint(30, 90)
            print(f"[РЕМОНТ] Шахта #{self.mine_id} отремонтирована!")
            return True
        return False

    def upgrade(self):
        if not self.is_broken and not self.is_upgrading:
            self.is_upgrading = True
            print(f"[УЛУЧШЕНИЕ] Шахта #{self.mine_id} улучшается...")
            time.sleep(5)
            self.level += 1
            self.production_rate = int(self.production_rate * 1.5)
            self.is_upgrading = False
            print(f"[ГОТОВО] Шахта #{self.mine_id} теперь уровень {self.level} (+{self.production_rate}/сек)")

    def get_status(self) -> str:
        status = "работает"
        if self.is_broken:
            status = "требует ремонта!"
        elif self.is_upgrading:
            status = "улучшается"

        return f"[Шахта {self.mine_id}] {self.resource_type.value}: +{self.production_rate}/сек ({status})"


# ==================== ASYNCIO: SHIP AND MARKET ====================
class Market:
    def __init__(self):
        self.prices = {
            planet: {
                resource: random.randint(10, 100)
                for resource in Resource
            }
            for planet in Planet
        }
        self.trends = {planet: {resource: 0 for resource in Resource} for planet in Planet}

    async def update_prices(self):
        while True:
            await asyncio.sleep(3)
            for planet in Planet:
                for resource in Resource:
                    # Изменение цены с трендом
                    change = random.uniform(-0.1, 0.1) + self.trends[planet][resource]
                    self.prices[planet][resource] = max(5, int(self.prices[planet][resource] * (1 + change)))

                    # Обновление тренда
                    self.trends[planet][resource] = random.uniform(-0.05, 0.05)

            # print("[РЫНОК] Цены обновлены")

    def get_price(self, planet: Planet, resource: Resource) -> int:
        return self.prices[planet][resource]

    def display_prices(self):
        print("\n" + "=" * 50)
        print("ТЕКУЩИЕ ЦЕНЫ НА РЫНКЕ:")
        print("=" * 50)
        for planet in Planet:
            print(f"\n{planet.value}:")
            for resource in Resource:
                trend = self.trends[planet][resource]
                trend_symbol = "▲" if trend > 0.01 else "▼" if trend < -0.01 else "●"
                print(f"  {resource.value}: {self.prices[planet][resource]} кредитов {trend_symbol}")


class Ship:
    def __init__(self):
        self.current_planet = Planet.NEUTRAL
        self.is_flying = False
        self.cargo = {resource: 0 for resource in Resource}
        self.cargo_capacity = 100

    async def fly_to(self, destination: Planet):
        if self.is_flying:
            print("[ОШИБКА] Корабль уже в полёте!")
            return False

        self.is_flying = True
        flight_time = random.randint(3, 7)

        print(f"\n[ПОЛЁТ] Летим на {destination.value}...")
        for i in range(flight_time, 0, -1):
            print(f"  Прибытие через {i} сек...")
            await asyncio.sleep(1)

        self.current_planet = destination
        self.is_flying = False
        print(f"[ПРИЛЕТЕЛИ] На планете {destination.value}")
        return True

    def load_cargo(self, resource: Resource, amount: int) -> bool:
        total_cargo = sum(self.cargo.values())
        if total_cargo + amount <= self.cargo_capacity:
            self.cargo[resource] += amount
            return True
        return False

    def unload_cargo(self, resource: Resource, amount: int) -> bool:
        if self.cargo[resource] >= amount:
            self.cargo[resource] -= amount
            return True
        return False

    def get_cargo_status(self) -> str:
        used = sum(self.cargo.values())
        return f"Груз: {used}/{self.cargo_capacity} единиц"


# ==================== MULTIPROCESSING: HEAVY TASKS ====================
def calculate_profit(prices_data):
    """Расчёт наиболее выгодной сделки"""
    prices, current_cargo = prices_data
    best_profit = 0
    best_trade = None

    for buy_planet in Planet:
        for sell_planet in Planet:
            if buy_planet == sell_planet:
                continue

            for resource in Resource:
                buy_price = prices[buy_planet.value][resource.value]
                sell_price = prices[sell_planet.value][resource.value]

                if sell_price > buy_price:
                    profit = sell_price - buy_price
                    if profit > best_profit:
                        best_profit = profit
                        best_trade = (buy_planet.value, sell_planet.value, resource.value, profit)

    return best_trade


def battle_simulation(strength_data):
    """Симуляция боя с пиратами"""
    player_strength, pirate_strength = strength_data

    # Простая симуляция
    player_roll = random.randint(1, player_strength)
    pirate_roll = random.randint(1, pirate_strength)

    if player_roll > pirate_roll:
        return ("ПОБЕДА", player_roll - pirate_roll)
    elif player_roll < pirate_roll:
        return ("ПОРАЖЕНИЕ", pirate_roll - player_roll)
    else:
        return ("НИЧЬЯ", 0)


def find_best_route(planets_data):
    """Поиск оптимального маршрута"""
    planets, current_planet = planets_data

    # Простой алгоритм поиска маршрута
    distances = {
        planet: random.randint(1, 10)
        for planet in planets
        if planet != current_planet
    }

    if distances:
        best_planet = min(distances, key=distances.get)
        return (best_planet, distances[best_planet])
    return None


# ==================== GAME STATE AND EVENTS ====================
class GameState:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = GameState()
        return cls._instance

    def __init__(self):
        self.money = 5000
        self.health = 100
        self.resources = {resource: 1000 for resource in Resource}
        self.mines = []
        self.market = Market()
        self.ship = Ship()
        self.target_money = 10000
        self.game_over = False

        # Создание шахт
        mine_types = [MineType.ENERGY, MineType.DEEP, MineType.EXPERIMENTAL]
        for i, mine_type in enumerate(mine_types, 1):
            mine = Mine(i, mine_type)
            mine.start()
            self.mines.append(mine)

    def add_resource(self, resource: Resource, amount: int):
        self.resources[resource] += amount

    def use_resource(self, resource: Resource, amount: int) -> bool:
        if self.resources[resource] >= amount:
            self.resources[resource] -= amount
            return True
        return False

    def display_status(self):
        print("\n" + "=" * 50)
        print("СТАТУС СТАНЦИИ:")
        print("=" * 50)
        print(f"Деньги: {self.money} кредитов (цель: {self.target_money})")
        print(f"Здоровье: {self.health} HP")
        print(f"Корабль на: {self.ship.current_planet.value}")
        print(f"{self.ship.get_cargo_status()}")

        print("\nРесурсы на складе:")
        for resource, amount in self.resources.items():
            print(f"  {resource.value}: {amount}")

        print("\nШахты:")
        for mine in self.mines:
            print(f"  {mine.get_status()}")

    async def handle_events(self):
        event_types = [
            ("ПИРАТСКАЯ АТАКА", 30, 60),
            ("СОЛНЕЧНАЯ ВСПЫШКА", 20, 40),
            ("МЕТЕОРИТНЫЙ ДОЖДЬ", 15, 30)
        ]

        while not self.game_over:
            await asyncio.sleep(random.randint(10, 20))

            if self.game_over:
                break

            event_type, min_time, max_time = random.choice(event_types)

            if event_type == "ПИРАТСКАЯ АТАКА":
                print(f"\n[ТРЕВОГА!] Пираты атакуют станцию!")

                # Выбор действия
                print("Выберите действие:")
                print("1. Сражаться (симуляция боя)")
                print("2. Заплатить выкуп (500 кредитов)")
                print("3. Спрятаться (станция не работает 10 сек)")

                try:
                    choice = int(input("Ваш выбор (1-3): "))

                    if choice == 1:
                        # Запуск процесса симуляции боя
                        with multiprocessing.Pool(1) as pool:
                            strength = self.health // 10 + len([m for m in self.mines if not m.is_broken])
                            result = pool.apply(battle_simulation, [(strength, random.randint(5, 20))])

                        outcome, damage = result

                        if outcome == "ПОБЕДА":
                            print(f"[БОЙ] {outcome}! Потеряно {damage} HP")
                            self.health -= damage
                            loot = random.randint(100, 500)
                            self.money += loot
                            print(f"[ДОБЫЧА] Получено {loot} кредитов!")
                        else:
                            print(f"[БОЙ] {outcome}! Потеряно {damage * 10} HP и 20% ресурсов")
                            self.health -= damage * 10
                            for resource in self.resources:
                                self.resources[resource] = int(self.resources[resource] * 0.8)

                    elif choice == 2:
                        if self.money >= 500:
                            self.money -= 500
                            print("[ВЫКУП] Пираты довольны и улетают")
                        else:
                            print("[ОШИБКА] Недостаточно денег для выкупа!")

                    elif choice == 3:
                        print("[СКРЫТИЕ] Станция затихает на 10 секунд...")
                        await asyncio.sleep(10)

                except ValueError:
                    print("[ОШИБКА] Неверный выбор!")

            elif event_type == "СОЛНЕЧНАЯ ВСПЫШКА":
                print(f"\n[СОБЫТИЕ] Солнечная вспышка!")
                print("- Шахты работают на 50% скорости 15 сек")
                print("- Цены на Энергию +20%")

                # Влияние на цены
                for planet in Planet:
                    GameState.instance().market.trends[planet][Resource.ENERGY] += 0.2

            elif event_type == "МЕТЕОРИТНЫЙ ДОЖДЬ":
                print(f"\n[СОБЫТИЕ] Метеоритный дождь!")
                print("- Все цены -10%")

                # Влияние на цены
                for planet in Planet:
                    for resource in Resource:
                        GameState.instance().market.trends[planet][resource] -= 0.1

    async def trade(self):
        print(f"\nТОРГОВЛЯ на {self.ship.current_planet.value}:")
        print("1. Купить ресурсы")
        print("2. Продать ресурсы")
        print("3. Погрузить ресурсы на корабль")
        print("4. Выгрузить ресурсы со корабля")

        try:
            choice = int(input("Ваш выбор (1-4): "))

            if choice == 1:
                print("\nЧто покупаем?")
                for i, resource in enumerate(Resource, 1):
                    price = self.market.get_price(self.ship.current_planet, resource)
                    print(f"{i}. {resource.value} - {price} кредитов")

                resource_idx = int(input("Выбор ресурса: ")) - 1
                amount = int(input("Количество: "))

                resource = list(Resource)[resource_idx]
                cost = amount * self.market.get_price(self.ship.current_planet, resource)

                if self.money >= cost:
                    self.money -= cost
                    self.resources[resource] += amount
                    print(f"[ПОКУПКА] Куплено {amount} {resource.value} за {cost} кредитов")
                else:
                    print("[ОШИБКА] Недостаточно денег!")

            elif choice == 2:
                print("\nЧто продаём?")
                for i, resource in enumerate(Resource, 1):
                    price = self.market.get_price(self.ship.current_planet, resource)
                    print(f"{i}. {resource.value} - {price} кредитов (на складе: {self.resources[resource]})")

                resource_idx = int(input("Выбор ресурса: ")) - 1
                amount = int(input("Количество: "))

                resource = list(Resource)[resource_idx]

                if self.resources[resource] >= amount:
                    price = self.market.get_price(self.ship.current_planet, resource)
                    income = amount * price

                    self.money += income
                    self.resources[resource] -= amount
                    print(f"[ПРОДАЖА] Продано {amount} {resource.value} за {income} кредитов")
                else:
                    print("[ОШИБКА] Недостаточно ресурсов!")

            elif choice == 3:
                print("\nЧто грузим на корабль?")
                for i, resource in enumerate(Resource, 1):
                    print(f"{i}. {resource.value} (на складе: {self.resources[resource]})")

                resource_idx = int(input("Выбор ресурса: ")) - 1
                amount = int(input("Количество: "))

                resource = list(Resource)[resource_idx]

                if self.resources[resource] >= amount:
                    if self.ship.load_cargo(resource, amount):
                        self.resources[resource] -= amount
                        print(f"[ПОГРУЗКА] Загружено {amount} {resource.value}")
                    else:
                        print("[ОШИБКА] Недостаточно места на корабле!")
                else:
                    print("[ОШИБКА] Недостаточно ресурсов!")

            elif choice == 4:
                print("\nЧто выгружаем с корабля?")
                for i, resource in enumerate(Resource, 1):
                    print(f"{i}. {resource.value} (на корабле: {self.ship.cargo[resource]})")

                resource_idx = int(input("Выбор ресурса: ")) - 1
                amount = int(input("Количество: "))

                resource = list(Resource)[resource_idx]

                if self.ship.unload_cargo(resource, amount):
                    self.resources[resource] += amount
                    print(f"[ВЫГРУЗКА] Выгружено {amount} {resource.value}")
                else:
                    print("[ОШИБКА] Недостаточно ресурсов на корабле!")

        except (ValueError, IndexError):
            print("[ОШИБКА] Неверный ввод!")


# ==================== MAIN GAME LOOP ====================
async def game_loop():
    game = GameState.instance()

    # Запуск обновления цен
    market_task = asyncio.create_task(game.market.update_prices())

    # Запуск обработки событий
    events_task = asyncio.create_task(game.handle_events())

    print("\n" + "=" * 50)
    print("КОСМИЧЕСКИЙ ШАХТЁР: ГОНКА ЗА РЕСУРСАМИ")
    print("=" * 50)
    print("Цель: заработать 10,000 кредитов")
    print("=" * 50)

    while game.money < game.target_money and game.health > 0 and not game.game_over:
        game.display_status()

        print("\n" + "=" * 50)
        print("ГЛАВНОЕ МЕНЮ:")
        print("=" * 50)
        print("1. Управление шахтами")
        print("2. Рынок и цены")
        print("3. Управление кораблём")
        print("4. Торговать на текущей планете")
        print("5. Запустить анализ прибыльности")
        print("6. Найти лучший маршрут")
        print("7. Выйти из игры")

        try:
            choice = int(input("\nВаш выбор (1-7): "))

            if choice == 1:
                # Управление шахтами
                print("\nУПРАВЛЕНИЕ ШАХТАМИ:")
                for i, mine in enumerate(game.mines, 1):
                    print(f"{i}. {mine.get_status()}")

                print("\nДействия:")
                print("1. Улучшить шахту (1000 кредитов)")
                print("2. Починить шахту (10 запчастей)")

                action = int(input("Выбор действия: "))

                if action == 1:
                    mine_idx = int(input("Номер шахты (1-3): ")) - 1
                    if 0 <= mine_idx < len(game.mines):
                        if game.money >= 1000:
                            game.money -= 1000
                            game.mines[mine_idx].upgrade()
                        else:
                            print("[ОШИБКА] Недостаточно денег!")

                elif action == 2:
                    mine_idx = int(input("Номер шахты (1-3): ")) - 1
                    if 0 <= mine_idx < len(game.mines):
                        if game.mines[mine_idx].repair(game.resources[Resource.PARTS]):
                            game.resources[Resource.PARTS] -= 10

            elif choice == 2:
                # Рынок и цены
                game.market.display_prices()

            elif choice == 3:
                # Управление кораблём
                print("\nУПРАВЛЕНИЕ КОРАБЛЁМ:")
                print(f"Текущее положение: {game.ship.current_planet.value}")
                print(game.ship.get_cargo_status())
                print("\nГруз на корабле:")
                for resource, amount in game.ship.cargo.items():
                    if amount > 0:
                        print(f"  {resource.value}: {amount}")

                print("\nКуда летим?")
                for i, planet in enumerate(Planet, 1):
                    print(f"{i}. {planet.value}")

                planet_idx = int(input("Выбор планеты: ")) - 1

                if 0 <= planet_idx < len(Planet):
                    destination = list(Planet)[planet_idx]
                    if destination != game.ship.current_planet:
                        await game.ship.fly_to(destination)
                    else:
                        print("[ОШИБКА] Корабль уже на этой планете!")

            elif choice == 4:
                # Торговля
                await game.trade()

            elif choice == 5:
                # Анализ прибыльности
                print("\n[АНАЛИТИК] Запуск анализа прибыльности...")

                # Подготовка данных для процесса
                prices_data = {}
                for planet in Planet:
                    prices_data[planet.value] = {}
                    for resource in Resource:
                        prices_data[planet.value][resource.value] = game.market.get_price(planet, resource)

                current_cargo = {k.value: v for k, v in game.ship.cargo.items()}

                # Запуск процесса
                with multiprocessing.Pool(1) as pool:
                    result = pool.apply(calculate_profit, [(prices_data, current_cargo)])

                if result:
                    buy_planet, sell_planet, resource, profit = result
                    print(f"[АНАЛИЗ] Самый выгодный торговый путь:")
                    print(f"  Купить {resource} на {buy_planet}")
                    print(f"  Продать на {sell_planet}")
                    print(f"  Прибыль: {profit} кредитов за единицу")
                else:
                    print("[АНАЛИЗ] Выгодных сделок не найдено")

            elif choice == 6:
                # Поиск маршрута
                print("\n[НАВИГАТОР] Поиск оптимального маршрута...")

                planets_data = ([p.value for p in Planet], game.ship.current_planet.value)

                with multiprocessing.Pool(1) as pool:
                    result = pool.apply(find_best_route, [planets_data])

                if result:
                    planet, distance = result
                    print(f"[МАРШРУТ] Рекомендуется лететь на {planet}")
                    print(f"  Примерное время полёта: {distance} секунд")

            elif choice == 7:
                # Выход
                print("\nСохранение игры...")
                game.game_over = True
                break

        except ValueError:
            print("[ОШИБКА] Неверный ввод!")

        # Небольшая пауза для отображения
        await asyncio.sleep(1)

    # Отмена задач
    market_task.cancel()
    events_task.cancel()

    # Итоги игры
    if game.money >= game.target_money:
        print("\n" + "=" * 50)
        print("ПОБЕДА! Вы достигли цели!")
        print(f"Итоговый капитал: {game.money} кредитов")
        print("=" * 50)
    elif game.health <= 0:
        print("\n" + "=" * 50)
        print("ПОРАЖЕНИЕ! Станция уничтожена!")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("ИГРА ЗАВЕРШЕНА")
        print("=" * 50)


# ==================== MAIN ====================
if __name__ == "__main__":
    # Для корректной работы multiprocessing в Windows
    multiprocessing.freeze_support()

    print("Запуск игры 'Космический шахтёр'...")
    print("Используются три технологии параллелизма:")
    print("1. Threading - для работы шахт")
    print("2. Asyncio - для рынка и полётов корабля")
    print("3. Multiprocessing - для тяжёлых вычислений")
    print("\nЗагрузка...")

    try:
        asyncio.run(game_loop())
    except KeyboardInterrupt:
        print("\n\nИгра прервана пользователем")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")

    print("\nСпасибо за игру!")