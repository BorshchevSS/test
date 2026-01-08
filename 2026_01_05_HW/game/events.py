"""
Модуль обработки игровых событий
"""

import asyncio
import random
import multiprocessing
from enums import GameEvent, Resource
from game_state import GameState
from processes import battle_simulation


async def handle_events():
    """
    Асинхронная обработка случайных событий
    """
    event_types = [
        (GameEvent.PIRATE_ATTACK, 30, 60),
        (GameEvent.SOLAR_FLARE, 20, 40),
        (GameEvent.METEOR_SHOWER, 15, 30)
    ]

    game = GameState.instance()

    while not game.game_over:
        # Случайная пауза между событиями
        await asyncio.sleep(random.randint(10, 20))

        if game.game_over:
            break

        # Выбор случайного события
        event_type, min_time, max_time = random.choice(event_types)

        if event_type == GameEvent.PIRATE_ATTACK:
            await handle_pirate_attack()
        elif event_type == GameEvent.SOLAR_FLARE:
            await handle_solar_flare()
        elif event_type == GameEvent.METEOR_SHOWER:
            await handle_meteor_shower()


async def handle_pirate_attack():
    """Обработка пиратской атаки"""
    game = GameState.instance()

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
                strength = game.health // 10 + len(game.get_available_mines())
                result = pool.apply(battle_simulation, [(strength, random.randint(5, 20))])

            outcome, damage = result

            if outcome == "ПОБЕДА":
                print(f"[БОЙ] {outcome}! Потеряно {damage} HP")
                game.health -= damage
                loot = random.randint(100, 500)
                game.money += loot
                print(f"[ДОБЫЧА] Получено {loot} кредитов!")
            elif outcome == "ПОРАЖЕНИЕ":
                print(f"[БОЙ] {outcome}! Потеряно {damage * 10} HP и 20% ресурсов")
                game.health -= damage * 10
                for resource in game.resources:
                    game.resources[resource] = int(game.resources[resource] * 0.8)
            else:  # НИЧЬЯ
                print(f"[БОЙ] {outcome}! Никто не победил")

        elif choice == 2:
            if game.money >= 500:
                game.money -= 500
                print("[ВЫКУП] Пираты довольны и улетают")
            else:
                print("[ОШИБКА] Недостаточно денег для выкупа!")

        elif choice == 3:
            print("[СКРЫТИЕ] Станция затихает на 10 секунд...")
            await asyncio.sleep(10)

    except ValueError:
        print("[ОШИБКА] Неверный выбор!")


async def handle_solar_flare():
    """Обработка солнечной вспышки"""
    game = GameState.instance()

    print(f"\n[СОБЫТИЕ] Солнечная вспышка!")
    print("- Шахты работают на 50% скорости 15 сек")
    print("- Цены на Энергию +20%")

    # Влияние на цены
    game.market.apply_solar_flare()

    # Временное замедление шахт
    original_rates = []
    for mine in game.mines:
        if not mine.is_broken and not mine.is_upgrading:
            original_rates.append(mine.production_rate)
            mine.production_rate = max(1, mine.production_rate // 2)

    await asyncio.sleep(15)

    # Восстановление скорости шахт
    for mine, original_rate in zip(game.mines, original_rates):
        if not mine.is_broken and not mine.is_upgrading:
            mine.production_rate = original_rate


async def handle_meteor_shower():
    """Обработка метеоритного дождя"""
    game = GameState.instance()

    print(f"\n[СОБЫТИЕ] Метеоритный дождь!")
    print("- Все цены -10%")

    # Влияние на цены
    game.market.apply_meteor_shower()

    # Небольшой урон станции
    damage = random.randint(1, 5)
    game.health -= damage
    print(f"- Станция получила {damage} урона от метеоритов")