"""
Модуль корабля - асинхронные полёты и груз
"""

import asyncio
import random
from enums import Planet, Resource


class Ship:
    """Класс космического корабля"""

    def __init__(self, cargo_capacity: int = 100):
        """
        Инициализация корабля

        Args:
            cargo_capacity: Вместимость грузового отсека
        """
        self.current_planet = Planet.NEUTRAL
        self.is_flying = False
        self.cargo = {resource: 0 for resource in Resource.get_all()}
        self.cargo_capacity = cargo_capacity

    async def fly_to(self, destination: Planet):
        """
        Асинхронный полёт на другую планету

        Args:
            destination: Целевая планета

        Returns:
            True если полёт успешен, иначе False
        """
        if self.is_flying:
            print("[ОШИБКА] Корабль уже в полёте!")
            return False

        if destination == self.current_planet:
            print("[ОШИБКА] Корабль уже на этой планете!")
            return False

        self.is_flying = True
        flight_time = random.randint(3, 7)

        print(f"\n[ПОЛЁТ] Летим на {destination.value}...")
        for i in range(flight_time, 0, -1):
            print(f" Прибытие через {i} сек...", end="\r")
            await asyncio.sleep(1)

        self.current_planet = destination
        self.is_flying = False
        print(f"\n[ПРИЛЕТЕЛИ] На планете {destination.value}")
        return True

    def load_cargo(self, resource: Resource, amount: int) -> bool:
        """
        Погрузить ресурсы на корабль

        Args:
            resource: Тип ресурса
            amount: Количество

        Returns:
            True если погрузка успешна, иначе False
        """
        total_cargo = sum(self.cargo.values())
        if total_cargo + amount <= self.cargo_capacity:
            self.cargo[resource] += amount
            return True
        return False

    def unload_cargo(self, resource: Resource, amount: int) -> bool:
        """
        Выгрузить ресурсы с корабля

        Args:
            resource: Тип ресурса
            amount: Количество

        Returns:
            True если выгрузка успешна, иначе False
        """
        if self.cargo[resource] >= amount:
            self.cargo[resource] -= amount
            return True
        return False

    def get_cargo_status(self) -> str:
        """
        Получить статус груза

        Returns:
            Строка со статусом груза
        """
        used = sum(self.cargo.values())
        return f"Груз: {used}/{self.cargo_capacity} единиц"

    def display_cargo(self):
        """Отобразить текущий груз на корабле"""
        print("\nТекущий груз на корабле:")
        has_cargo = False
        for resource, amount in self.cargo.items():
            if amount > 0:
                print(f" {resource.value}: {amount}")
                has_cargo = True

        if not has_cargo:
            print(" Корабль пуст")

        print(f" {self.get_cargo_status()}")

    def clear_cargo(self):
        """Очистить весь груз на корабле"""
        self.cargo = {resource: 0 for resource in Resource.get_all()}