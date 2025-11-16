from abc import ABC, abstractmethod
import random
import time
from typing import List


class Road:
    """
    Класс для моделирования дорожного полотна
    """

    def __init__(self, length: float, lanes: int = 1):
        """
        Инициализация дороги

        Args:
            length (float): Длина дороги в метрах
            lanes (int): Количество полос движения
        """
        self.length = length
        self.lanes = lanes
        self.vehicles = []  # Список всех транспортных средств на дороге

    def add_vehicle(self, vehicle: 'Vehicle'):
        """Добавляет транспортное средство на дорогу"""
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: 'Vehicle'):
        """Удаляет транспортное средство с дороги"""
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def get_vehicles_in_lane(self, lane: int):
        """Возвращает список транспортных средств на указанной полосе"""
        return [v for v in self.vehicles if v.lane == lane]

    def get_vehicle_ahead(self, vehicle: 'Vehicle'):
        """
        Возвращает транспортное средство впереди на той же полосе
        или None, если впереди никого нет
        """
        vehicles_in_lane = self.get_vehicles_in_lane(vehicle.lane)
        vehicles_ahead = [v for v in vehicles_in_lane if v.x > vehicle.x]

        if not vehicles_ahead:
            return None

        # Возвращаем ближайшее транспортное средство
        return min(vehicles_ahead, key=lambda v: v.x - vehicle.x)

    def cleanup_finished_vehicles(self):
        """Удаляет транспортные средства, достигшие конца дороги"""
        finished_vehicles = [v for v in self.vehicles if v.x >= self.length]
        for vehicle in finished_vehicles:
            self.remove_vehicle(vehicle)
        return len(finished_vehicles)


#2. Абстрактный класс Vehicle
class Vehicle(ABC):
    """
    Абстрактный базовый класс для всех транспортных средств
    """

    _id_counter = 1  # Счетчик для генерации уникальных ID

    def __init__(self, x: float = 0, lane: int = 0, max_speed: float = 33.33):
        """
        Инициализация транспортного средства

        Args:
            x (float): Начальная позиция на дороге (метры)
            lane (int): Номер полосы (0-based)
            max_speed (float): Максимальная скорость (м/с)
        """
        self.id = Vehicle._id_counter
        Vehicle._id_counter += 1
        self.x = x
        self.lane = lane
        self.speed = 0
        self.max_speed = max_speed
        self.acceleration = 2.0  # Стандартное ускорение м/с²
        self.safe_distance = 20.0  # Безопасная дистанция в метрах
        self.length = 4.5  # Длина транспортного средства в метрах

    def accelerate(self, acceleration: float):
        """
        Ускоряет транспортное средство

        Args:
            acceleration (float): Ускорение (м/с²)
        """
        self.speed += acceleration
        # Ограничение скорости
        self.speed = min(self.speed, self.max_speed)
        self.speed = max(self.speed, 0)  # Не может двигаться назад

    def move(self):
        """Двигает транспортное средство на основе текущей скорости"""
        self.x += self.speed

    def get_distance_to(self, other: 'Vehicle') -> float:
        """Возвращает расстояние до другого транспортного средства"""
        return other.x - self.x - other.length

    @abstractmethod
    def decide_action(self, road: Road):
        """
        Абстрактный метод для принятия решения о движении
        Должен быть реализован в подклассах
        """
        pass

    def __str__(self):
        return f"{self.__class__.__name__} {self.id}: pos={self.x:.1f}m, speed={self.speed:.1f}m/s, lane={self.lane}"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, x={self.x:.1f}, speed={self.speed:.1f})"


#3. Класс Car(Легковой автомобиль)
class Car(Vehicle):
    """
    Класс легкового автомобиля
    """

    def __init__(self, x: float = 0, lane: int = 0):
        super().__init__(x, lane, max_speed=33.33)  # 120 км/ч
        self.acceleration = 2.5
        self.safe_distance = 15.0
        self.length = 4.5

    def decide_action(self, road: Road):
        """
        Принимает решение об ускорении/замедлении:
        - Ускоряется, если впереди нет машин в пределах безопасной дистанции
        - Замедляется, если впереди есть машина слишком близко
        """
        vehicle_ahead = road.get_vehicle_ahead(self)

        if vehicle_ahead is None:
            # Впереди никого - можно ускоряться до максимальной скорости
            if self.speed < self.max_speed:
                self.accelerate(self.acceleration)
        else:
            # Впереди есть транспортное средство
            distance = self.get_distance_to(vehicle_ahead)

            if distance > self.safe_distance * 1.5:
                # Достаточно места - можно ускоряться
                if self.speed < self.max_speed:
                    self.accelerate(self.acceleration * 0.5)
            elif distance < self.safe_distance:
                # Слишком близко - нужно замедлиться
                required_deceleration = (self.speed - vehicle_ahead.speed) / 2.0
                self.accelerate(-min(required_deceleration, 3.0))
            else:
                # Поддерживаем текущую скорость
                pass

        # Небольшая случайность для реалистичности
        if random.random() < 0.1:
            self.accelerate(random.uniform(-0.5, 0.5))


#4. Класс Truck(Грузовик)
class Truck(Vehicle):
    """
    Класс грузовика
    """

    def __init__(self, x: float = 0, lane: int = 0):
        super().__init__(x, lane, max_speed=25.0)  # 90 км/ч
        self.acceleration = 1.2  # Медленнее разгоняется
        self.safe_distance = 25.0  # Большая безопасная дистанция
        self.length = 12.0  # Длиннее автомобиля

    def decide_action(self, road: Road):
        """
        Принимает более осторожные решения:
        - Требует большей безопасной дистанции
        - Медленнее ускоряется и замедляется
        """
        vehicle_ahead = road.get_vehicle_ahead(self)

        if vehicle_ahead is None:
            # Впереди никого - медленно ускоряемся
            if self.speed < self.max_speed:
                self.accelerate(self.acceleration)
        else:
            # Впереди есть транспортное средство
            distance = self.get_distance_to(vehicle_ahead)

            if distance > self.safe_distance * 2.0:
                # Много места - медленно ускоряемся
                if self.speed < self.max_speed:
                    self.accelerate(self.acceleration * 0.3)
            elif distance < self.safe_distance * 0.8:
                # Очень близко - активно замедляемся
                required_deceleration = (self.speed - vehicle_ahead.speed) / 1.5
                self.accelerate(-min(required_deceleration, 2.5))
            elif distance < self.safe_distance:
                # Близко - плавно замедляемся
                self.accelerate(-0.5)
            else:
                # Поддерживаем скорость
                pass

        # Грузовики менее подвержены случайным изменениям скорости
        if random.random() < 0.05:
            self.accelerate(random.uniform(-0.3, 0.3))


#5. Класс TrafficFlowSimulator
class TrafficFlowSimulator:
    """
    Основной класс для управления симуляцией дорожного движения
    """

    def __init__(self, road_length: float = 1000.0, lanes: int = 2):
        """
        Инициализация симулятора

        Args:
            road_length (float): Длина дороги в метрах
            lanes (int): Количество полос
        """
        self.road = Road(road_length, lanes)
        self.time_elapsed = 0
        self.cycle_count = 0
        self.vehicles_finished = 0

    def add_vehicle(self, vehicle: Vehicle):
        """Добавляет транспортное средство на дорогу"""
        self.road.add_vehicle(vehicle)

    def add_random_vehicle(self, vehicle_type: str = "car", **kwargs):
        """Добавляет случайное транспортное средство"""
        lane = random.randint(0, self.road.lanes - 1)
        x = random.uniform(0, 100)  # Начальная позиция в первых 100 метрах

        if vehicle_type.lower() == "truck":
            vehicle = Truck(x, lane, **kwargs)
        else:
            vehicle = Car(x, lane, **kwargs)

        self.add_vehicle(vehicle)
        return vehicle

    def run_cycle(self, cycle_duration: float = 1.0):
        """
        Запускает один цикл симуляции

        Args:
            cycle_duration (float): Длительность цикла в секундах
        """
        self.cycle_count += 1
        self.time_elapsed += cycle_duration

        print(f"\n=== Цикл {self.cycle_count} (Время: {self.time_elapsed:.1f}с) ===")

        # 1. Все транспортные средства принимают решения
        for vehicle in self.road.vehicles:
            vehicle.decide_action(self.road)

        # 2. Все транспортные средства двигаются
        for vehicle in self.road.vehicles:
            vehicle.move()

        # 3. Удаляем транспортные средства, достигшие конца дороги
        finished_count = self.road.cleanup_finished_vehicles()
        self.vehicles_finished += finished_count

        # 4. Выводим информацию о текущем состоянии
        self.print_status()

        return len(self.road.vehicles)

    def print_status(self):
        """Выводит текущее состояние симуляции"""
        print(f"Транспортных средств на дороге: {len(self.road.vehicles)}")
        print(f"Всего завершило путь: {self.vehicles_finished}")

        for lane in range(self.road.lanes):
            vehicles_in_lane = self.road.get_vehicles_in_lane(lane)
            print(f"Полоса {lane}: {len(vehicles_in_lane)} транспортных средств")

            for vehicle in sorted(vehicles_in_lane, key=lambda v: v.x):
                print(f" {vehicle}")

    def run_simulation(self, cycles: int, cycle_duration: float = 1.0,
                       auto_spawn: bool = True, spawn_probability: float = 0.3):
        """
        Запускает симуляцию на указанное количество циклов

        Args:
            cycles (int): Количество циклов симуляции
            cycle_duration (float): Длительность цикла в секундах
            auto_spawn (bool): Автоматически добавлять новые транспортные средства
            spawn_probability (float): Вероятность добавления нового ТС за цикл
        """
        print(f"Запуск симуляции на {cycles} циклов")
        print(f"Дорога: {self.road.length}м, {self.road.lanes} полос(ы)")

        for cycle in range(cycles):
            vehicles_remaining = self.run_cycle(cycle_duration)

            # Автоматическое добавление новых транспортных средств
            if auto_spawn and random.random() < spawn_probability:
                vehicle_type = random.choice(["car", "car", "truck"])  # 2/3 cars, 1/3 trucks
                self.add_random_vehicle(vehicle_type)
                print(f"→ Добавлен новый {vehicle_type}")

            # Задержка для удобства наблюдения
            time.sleep(0.5)

            # Остановка если на дороге никого нет
            if vehicles_remaining == 0 and cycle > 10:
                print("\nНа дороге не осталось транспортных средств. Симуляция завершена.")
                break

        print(f"\n=== СИМУЛЯЦИЯ ЗАВЕРШЕНА ===")
        print(f"Всего циклов: {self.cycle_count}")
        print(f"Всего обработано транспортных средств: {self.vehicles_finished}")


