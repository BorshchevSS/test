"""
Модуль шахт - работа с потоками (Threading)
"""

import threading
import time
import random
from enums import MineType, Resource


class Mine(threading.Thread):
    """Класс шахты, работающей в отдельном потоке"""

    def __init__(self, mine_id: int, mine_type: MineType):
        """
        Инициализация шахты

        Args:
            mine_id: Уникальный идентификатор шахты
            mine_type: Тип шахты
        """
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
        """Определить тип ресурса в зависимости от типа шахты"""
        if self.mine_type == MineType.ENERGY:
            return Resource.ENERGY
        elif self.mine_type == MineType.DEEP:
            return Resource.METAL
        else:  # EXPERIMENTAL
            return random.choice([Resource.CRYSTALS, Resource.PARTS])

    def _get_base_rate(self) -> int:
        """Получить базовую скорость производства"""
        if self.mine_type == MineType.ENERGY:
            return 5
        elif self.mine_type == MineType.DEEP:
            return 2
        else:  # EXPERIMENTAL
            return 1

    def run(self):
        """Основной метод потока - производство ресурсов"""
        while self.is_running:
            if not self.is_broken and not self.is_upgrading:
                # Производство ресурсов
                from game.game_state import GameState
                GameState.instance().add_resource(self.resource_type, self.production_rate)
                time.sleep(1)

                # Проверка на поломку
                if time.time() - self.last_breakdown > self.breakdown_interval:
                    if random.random() < 0.3:  # 30% шанс поломки
                        self.is_broken = True
                        print(f"\n[АВАРИЯ] Шахта #{self.mine_id} ({self.mine_type.value}) сломалась!")
            else:
                time.sleep(0.5)

    def repair(self, parts_available: int) -> bool:
        """
        Починить шахту

        Args:
            parts_available: Количество доступных запчастей

        Returns:
            True если ремонт успешен, иначе False
        """
        if self.is_broken and parts_available >= 10:
            self.is_broken = False
            self.last_breakdown = time.time()
            self.breakdown_interval = random.randint(30, 90)
            print(f"[РЕМОНТ] Шахта #{self.mine_id} отремонтирована!")
            return True
        return False

    def upgrade(self):
        """Улучшить шахту"""
        if not self.is_broken and not self.is_upgrading:
            self.is_upgrading = True
            print(f"[УЛУЧШЕНИЕ] Шахта #{self.mine_id} улучшается...")
            time.sleep(5)
            self.level += 1
            self.production_rate = int(self.production_rate * 1.5)
            self.is_upgrading = False
            print(f"[ГОТОВО] Шахта #{self.mine_id} теперь уровень {self.level} (+{self.production_rate}/сек)")

    def get_status(self) -> str:
        """
        Получить текстовый статус шахты

        Returns:
            Строка со статусом шахты
        """
        status = "работает"
        if self.is_broken:
            status = "требует ремонта!"
        elif self.is_upgrading:
            status = "улучшается"

        return f"[Шахта {self.mine_id}] {self.resource_type.value}: +{self.production_rate}/сек ({status})"

    def stop(self):
        """Остановить работу шахты"""
        self.is_running = False