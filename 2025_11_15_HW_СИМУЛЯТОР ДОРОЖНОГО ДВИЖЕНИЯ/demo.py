from simulation import Car, TrafficFlowSimulator, Truck




def demo_simulation():
    """Демонстрация работы симулятора дорожного движения"""

    # Создаем симулятор с дорогой 500 метров и 2 полосами
    simulator = TrafficFlowSimulator(road_length=500.0, lanes=2)

    # Добавляем начальные транспортные средства
    print("Инициализация симуляции...")

    # Добавляем несколько автомобилей
    simulator.add_vehicle(Car(x=0, lane=0))
    simulator.add_vehicle(Car(x=20, lane=1))
    simulator.add_vehicle(Truck(x=50, lane=0))
    simulator.add_vehicle(Car(x=80, lane=1))

    # Запускаем симуляцию на 20 циклов
    simulator.run_simulation(
        cycles=20,
        cycle_duration=1.0,
        auto_spawn=True,
        spawn_probability=0.2
    )


def interactive_demo():
    """Интерактивная демонстрация"""
    simulator = TrafficFlowSimulator(road_length=300.0, lanes=1)

    print("Интерактивная демонстрация симулятора дорожного движения")
    print(
        "Команды: r - добавить случайное ТС, c - добавить автомобиль, t - добавить грузовик, n - следующий цикл, q - выход")

    while True:
        command = input("\nВведите команду: ").lower().strip()

        if command == 'q':
            break
        elif command == 'r':
            vehicle = simulator.add_random_vehicle()
            print(f"Добавлен: {vehicle}")
        elif command == 'c':
            vehicle = Car(x=0, lane=0)
            simulator.add_vehicle(vehicle)
            print(f"Добавлен автомобиль: {vehicle}")
        elif command == 't':
            vehicle = Truck(x=0, lane=0)
            simulator.add_vehicle(vehicle)
            print(f"Добавлен грузовик: {vehicle}")
        elif command == 'n':
            simulator.run_cycle()
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    print("СИМУЛЯТОР ДОРОЖНОГО ДВИЖЕНИЯ")
    print("=" * 50)

    # Запуск демонстрации
    demo_simulation()

    # Раскомментируйте для интерактивного режима
    # interactive_demo()