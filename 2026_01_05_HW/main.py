"""
Космический шахтёр: Гонка за ресурсами
Главный файл запуска игры
"""

import asyncio
import multiprocessing
from game.game_loop import game_loop


def main():
    """Основная функция запуска игры"""
    print("=" * 60)
    print("КОСМИЧЕСКИЙ ШАХТЁР: ГОНКА ЗА РЕСУРСАМИ")
    print("=" * 60)
    print("Цель: заработать 10,000 кредитов")
    print("Используются три технологии параллелизма:")
    print("1. Threading - для работы шахт")
    print("2. Asyncio - для рынка и полётов корабля")
    print("3. Multiprocessing - для тяжёлых вычислений")
    print("=" * 60)
    print("\nЗагрузка...")

    # Для корректной работы multiprocessing в Windows
    multiprocessing.freeze_support()

    try:
        # Запуск игрового цикла
        asyncio.run(game_loop())
    except KeyboardInterrupt:
        print("\n\nИгра прервана пользователем")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")

    print("\nСпасибо за игру!")


if __name__ == "__main__":
    main()