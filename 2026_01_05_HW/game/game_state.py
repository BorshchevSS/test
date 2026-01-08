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