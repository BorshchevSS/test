"""
Главный игровой цикл
"""

import asyncio
import multiprocessing
from events import handle_events
from trade import trade
from processes import calculate_profit, find_best_route, market_prediction
from enums import Planet, Resource


async def game_loop():
    """Основной игровой цикл"""
    game = GameState1.instance()

    # Запуск асинхронных задач
    market_task = asyncio.create_task(game.market.update_prices())
    events_task = asyncio.create_task(handle_events())

    while not game.game_over:
        # Проверка условий завершения игры
        if game.check_game_over():
            break

        # Отображение статуса
        game.display_status()

        # Главное меню
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ:")
        print("="*50)
        print("1. Управление шахтами")
        print("2. Рынок и цены")
        print("3. Управление кораблём")
        print("4. Торговать на текущей планете")
        print("5. Запустить анализ прибыльности")
        print("6. Найти лучший маршрут")
        print("7. Предсказание изменения цен")
        print("8. Выйти из игры")

        try:
            choice = int(input("\nВаш выбор (1-8): "))

            if choice == 1:
                await manage_mines()
            elif choice == 2:
                await show_market()
            elif choice == 3:
                await manage_ship()
            elif choice == 4:
                await trade()
            elif choice == 5:
                await analyze_profit()
            elif choice == 6:
                await find_route()
            elif choice == 7:
                await predict_prices()
            elif choice == 8:
                print("\nСохранение игры...")
                game.game_over = True
                break

        except ValueError:
            print("[ОШИБКА] Неверный ввод!")

        # Небольшая пауза для отображения
        await asyncio.sleep(1)

    # Остановка всех задач
    market_task.cancel()
    events_task.cancel()

    # Остановка всех шахт
    game.stop_all_mines()

    # Итоги игры
    print("\n" + "="*60)
    print("ИГРА ЗАВЕРШЕНА")
    print("="*60)
    print(f"Итоговый капитал: {game.money} кредитов")
    print(f"Итоговое здоровье: {game.health} HP")
    print("="*60)


async def manage_mines():
    """Управление шахтами"""
    game = GameState1.instance()

    print("\nУПРАВЛЕНИЕ ШАХТАМИ:")
    for i, mine in enumerate(game.mines, 1):
        print(f"{i}. {mine.get_status()}")

    print("\nДействия:")
    print("1. Улучшить шахту (1000 кредитов)")
    print("2. Починить шахту (10 запчастей)")
    print("3. Вернуться в меню")

    try:
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
                else:
                    print("[ОШИБКА] Недостаточно запчастей или шахта не сломана!")

    except ValueError:
        print("[ОШИБКА] Неверный ввод!")


async def show_market():
    """Показать информацию о рынке"""
    game = GameState1.instance()
    game.market.display_prices()


async def manage_ship():
    """Управление кораблём"""
    game = GameState1.instance()

    print("\nУПРАВЛЕНИЕ КОРАБЛЁМ:")
    print(f"Текущее положение: {game.ship.current_planet.value}")
    game.ship.display_cargo()

    print("\nКуда летим?")
    for i, planet in enumerate(Planet.get_all(), 1):
        print(f"{i}. {planet.value}")
    print(f"{len(Planet.get_all()) + 1}. Вернуться в меню")

    try:
        choice = int(input("Ваш выбор: "))

        if 1 <= choice <= len(Planet.get_all()):
            destination = Planet.get_all()[choice - 1]
            await game.ship.fly_to(destination)

    except ValueError:
        print("[ОШИБКА] Неверный ввод!")


async def analyze_profit():
    """Анализ прибыльности торговли"""
    game = GameState1.instance()

    print("\n[АНАЛИТИК] Запуск анализа прибыльности...")

    # Подготовка данных для процесса
    prices_data = {}
    for planet in Planet.get_all():
        prices_data[planet.value] = {}
        for resource in Resource.get_all():
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

        # Рекомендация
        cargo_space = 100 - sum(game.ship.cargo.values())
        if cargo_space > 0:
            potential_profit = profit * cargo_space
            print(f"  Потенциальная прибыль: {potential_profit} кредитов")
    else:
        print("[АНАЛИЗ] Выгодных сделок не найдено")


async def find_route():
    """Поиск оптимального маршрута"""
    game = GameState1.instance()

    print("\n[НАВИГАТОР] Поиск оптимального маршрута...")

    planets_data = ([p.value for p in Planet.get_all()], game.ship.current_planet.value)

    with multiprocessing.Pool(1) as pool:
        result = pool.apply(find_best_route, [planets_data])

    if result:
        planet, distance = result
        print(f"[МАРШРУТ] Рекомендуется лететь на {planet}")
        print(f"  Примерное время полёта: {distance} секунд")

        # Дополнительная информация
        current_planet = game.ship.current_planet
        if planet == current_planet.value:
            print("  Вы уже на этой планете!")
        else:
            print("  Совет: загрузите товары перед отлётом")
    else:
        print("[МАРШРУТ] Маршруты не найдены")


async def predict_prices():
    """Предсказание изменения цен"""
    game = GameState1.instance()

    print("\n[АНАЛИТИК] Анализ рынка и предсказание цен...")

    # Подготовка данных для процесса
    prices_data = {}
    trends_data = {}

    for planet in Planet.get_all():
        prices_data[planet.value] = {}
        trends_data[planet.value] = {}

        for resource in Resource.get_all():
            prices_data[planet.value][resource.value] = game.market.get_price(planet, resource)
            trends_data[planet.value][resource.value] = game.market.trends[planet][resource]

    # Запуск процесса
    with multiprocessing.Pool(1) as pool:
        predictions = pool.apply(market_prediction, [(prices_data, trends_data)])

    if predictions:
        print("\n[ПРЕДСКАЗАНИЯ]:")
        for i, prediction in enumerate(predictions, 1):
            print(f"  {i}. {prediction}")
    else:
        print("\n[ПРЕДСКАЗАНИЯ] Значительных изменений цен не ожидается")


"""
Состояние игры и управление ресурсами
"""

from enums import Resource, Planet, MineType, GameEvent
from enums import (
    STARTING_MONEY, STARTING_HEALTH, TARGET_MONEY,
    STARTING_RESOURCES, UPGRADE_COST, REPAIR_PARTS_COST, RANSOM_COST
)
from mine import Mine
from market import Market
from ship import Ship


class GameState1:
    """Класс состояния игры (Singleton)"""

    _instance = None

    @classmethod
    def instance(cls):
        """
        Получить экземпляр GameState (Singleton)

        Returns:
            Экземпляр GameState
        """
        if cls._instance is None:
            cls._instance = GameState1()
        return cls._instance

    def __init__(self):
        """Инициализация состояния игры"""
        self.money = STARTING_MONEY
        self.health = STARTING_HEALTH
        self.resources = {resource: STARTING_RESOURCES for resource in Resource.get_all()}
        self.mines = []
        self.market = Market()
        self.ship = Ship()
        self.target_money = TARGET_MONEY
        self.game_over = False

        # Создание шахт
        mine_types = MineType.get_all()
        for i, mine_type in enumerate(mine_types, 1):
            mine = Mine(i, mine_type)
            mine.start()
            self.mines.append(mine)

    def add_resource(self, resource: Resource, amount: int):
        """
        Добавить ресурсы на склад

        Args:
            resource: Тип ресурса
            amount: Количество
        """
        self.resources[resource] += amount

    def use_resource(self, resource: Resource, amount: int) -> bool:
        """
        Использовать ресурсы со склада

        Args:
            resource: Тип ресурса
            amount: Количество

        Returns:
            True если ресурсов достаточно, иначе False
        """
        if self.resources[resource] >= amount:
            self.resources[resource] -= amount
            return True
        return False

    def display_status(self):
        """Отобразить текущий статус игры"""
        print("\n" + "=" * 50)
        print("СТАТУС СТАНЦИИ:")
        print("=" * 50)
        print(f"Деньги: {self.money} кредитов (цель: {self.target_money})")
        print(f"Здоровье: {self.health} HP")
        print(f"Корабль на: {self.ship.current_planet.value}")
        print(f"{self.ship.get_cargo_status()}")

        print("\nРесурсы на складе:")
        for resource, amount in self.resources.items():
            print(f" {resource.value}: {amount}")

        print("\nШахты:")
        for mine in self.mines:
            print(f" {mine.get_status()}")

    def check_game_over(self) -> bool:
        """
        Проверить условия завершения игры

        Returns:
            True если игра завершена, иначе False
        """
        if self.health <= 0:
            print("\n[ПОРАЖЕНИЕ] Станция уничтожена!")
            self.game_over = True
            return True

        if self.money >= self.target_money:
            print(f"\n[ПОБЕДА] Цель достигнута! Капитал: {self.money} кредитов")
            self.game_over = True
            return True

        return False

    def stop_all_mines(self):
        """Остановить все шахты"""
        for mine in self.mines:
            mine.stop()

    def get_available_mines(self):
        """Получить список работающих шахт"""
        return [mine for mine in self.mines if not mine.is_broken and not mine.is_upgrading]