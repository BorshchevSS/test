"""
Модуль тяжёлых задач - работа с процессами (Multiprocessing)
"""

import random
from enums import Planet, Resource


def calculate_profit(prices_data):
    """
    Расчёт наиболее выгодной сделки (Multiprocessing)

    Args:
        prices_data: Данные о ценах и текущем грузе

    Returns:
        Информация о самой выгодной сделке
    """
    prices, current_cargo = prices_data
    best_profit = 0
    best_trade = None

    for buy_planet in Planet.get_all():
        for sell_planet in Planet.get_all():
            if buy_planet == sell_planet:
                continue

            for resource in Resource.get_all():
                buy_price = prices[buy_planet.value][resource.value]
                sell_price = prices[sell_planet.value][resource.value]

                if sell_price > buy_price:
                    profit = sell_price - buy_price
                    if profit > best_profit:
                        best_profit = profit
                        best_trade = (buy_planet.value, sell_planet.value, resource.value, profit)

    return best_trade


def battle_simulation(strength_data):
    """
    Симуляция боя с пиратами (Multiprocessing)

    Args:
        strength_data: Силы игрока и пиратов

    Returns:
        Результат боя
    """
    player_strength, pirate_strength = strength_data

    # Простая симуляция с элементами случайности
    player_roll = random.randint(1, player_strength)
    pirate_roll = random.randint(1, pirate_strength)

    if player_roll > pirate_roll:
        damage = player_roll - pirate_roll
        return ("ПОБЕДА", damage)
    elif player_roll < pirate_roll:
        damage = pirate_roll - player_roll
        return ("ПОРАЖЕНИЕ", damage)
    else:
        return ("НИЧЬЯ", 0)


def find_best_route(planets_data):
    """
    Поиск оптимального маршрута (Multiprocessing)

    Args:
        planets_data: Данные о планетах и текущем положении

    Returns:
        Информация о лучшем маршруте
    """
    planets, current_planet = planets_data

    # Простой алгоритм поиска маршрута
    distances = {
        planet: random.randint(1, 10)
        for planet in planets
        if planet != current_planet
    }

    if distances:
        best_planet = min(distances, key=distances.get)
        return (best_planet, distances[best_planet])

    return None


def market_prediction(market_data):
    """
    Предсказание изменения цен (Multiprocessing)

    Args:
        market_data: Данные о текущих ценах и трендах

    Returns:
        Предсказания изменения цен
    """
    prices, trends = market_data
    predictions = []

    for planet in Planet.get_all():
        for resource in Resource.get_all():
            current_price = prices[planet.value][resource.value]
            trend = trends[planet.value][resource.value]

            # Простой алгоритм предсказания
            if trend > 0.05:
                change_percent = int(trend * 100)
                predictions.append(
                    f"Цена на {resource.value} на {planet.value} вырастет на {change_percent}% в ближайшее время"
                )
            elif trend < -0.05:
                change_percent = int(abs(trend) * 100)
                predictions.append(
                    f"Цена на {resource.value} на {planet.value} упадёт на {change_percent}% в ближайшее время"
                )

    return predictions[:3]  # Возвращаем только 3 предсказания