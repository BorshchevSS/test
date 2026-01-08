"""
Перечисления и константы игры
"""

from enum import Enum


class Resource(Enum):
    """Типы ресурсов в игре"""
    ENERGY = "Энергия"
    METAL = "Металл"
    CRYSTALS = "Кристаллы"
    PARTS = "Запчасти"

    @classmethod
    def get_all(cls):
        """Получить все ресурсы"""
        return list(cls)


class Planet(Enum):
    """Планеты в игре"""
    ICE_9 = "Лёд-9"
    FIREWORLD = "Огневик"
    MECHANICUS = "Механикус"
    NEUTRAL = "Нейтральная"

    @classmethod
    def get_all(cls):
        """Получить все планеты"""
        return list(cls)


class MineType(Enum):
    """Типы шахт"""
    ENERGY = "Энерго-шахта"
    DEEP = "Глубинная"
    EXPERIMENTAL = "Экспериментальная"

    @classmethod
    def get_all(cls):
        """Получить все типы шахт"""
        return list(cls)


class GameEvent(Enum):
    """Типы игровых событий"""
    PIRATE_ATTACK = "ПИРАТСКАЯ АТАКА"
    SOLAR_FLARE = "СОЛНЕЧНАЯ ВСПЫШКА"
    METEOR_SHOWER = "МЕТЕОРИТНЫЙ ДОЖДЬ"
    EQUIPMENT_BREAKDOWN = "ПОЛОМКА ОБОРУДОВАНИЯ"


# Константы игры
STARTING_MONEY = 5000
STARTING_HEALTH = 100
TARGET_MONEY = 10000
STARTING_RESOURCES = 1000
CARGO_CAPACITY = 100
UPGRADE_COST = 1000
REPAIR_PARTS_COST = 10
RANSOM_COST = 500