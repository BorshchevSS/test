"""
Модуль рынка - асинхронные операции
"""

import asyncio
import random
from enums import Planet, Resource


class Market:
    """Класс рынка для управления ценами"""

    def __init__(self):
        """Инициализация рынка со случайными ценами"""
        self.prices = {
            planet: {
                resource: random.randint(10, 100)
                for resource in Resource.get_all()
            }
            for planet in Planet.get_all()
        }
        self.trends = {
            planet: {resource: 0 for resource in Resource.get_all()}
            for planet in Planet.get_all()
        }

    async def update_prices(self):
        """Асинхронное обновление цен каждые 3 секунды"""
        while True:
            await asyncio.sleep(3)
            for planet in Planet.get_all():
                for resource in Resource.get_all():
                    # Изменение цены с трендом
                    change = random.uniform(-0.1, 0.1) + self.trends[planet][resource]
                    self.prices[planet][resource] = max(5, int(self.prices[planet][resource] * (1 + change)))

                    # Обновление тренда
                    self.trends[planet][resource] = random.uniform(-0.05, 0.05)

    def get_price(self, planet: Planet, resource: Resource) -> int:
        """
        Получить текущую цену ресурса на планете

        Args:
            planet: Планета
            resource: Ресурс

        Returns:
            Цена ресурса
        """
        return self.prices[planet][resource]

    def display_prices(self):
        """Отобразить текущие цены на всех планетах"""
        print("\n" + "=" * 50)
        print("ТЕКУЩИЕ ЦЕНЫ НА РЫНКЕ:")
        print("=" * 50)

        for planet in Planet.get_all():
            print(f"\n{planet.value}:")
            for resource in Resource.get_all():
                trend = self.trends[planet][resource]
                if trend > 0.01:
                    trend_symbol = "▲"
                elif trend < -0.01:
                    trend_symbol = "▼"
                else:
                    trend_symbol = "●"

                price = self.prices[planet][resource]
                print(f" {resource.value}: {price:3d} кредитов {trend_symbol}")

    def apply_solar_flare(self):
        """Применить эффект солнечной вспышки (цены на энергию +20%)"""
        for planet in Planet.get_all():
            self.trends[planet][Resource.ENERGY] += 0.2

    def apply_meteor_shower(self):
        """Применить эффект метеоритного дождя (все цены -10%)"""
        for planet in Planet.get_all():
            for resource in Resource.get_all():
                self.trends[planet][resource] -= 0.1