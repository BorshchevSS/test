def get_daily_calories(date):
    total_calories = 0
    try:
        with open('food_log.txt', 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(', ')
                if len(parts) >= 3 and parts[0] == date:
                    try:
                        total_calories += int(parts[2])
                    except ValueError:
                        continue
        return total_calories
    except FileNotFoundError:
        return 0

def get_most_caloric_food(date):
    max_calories = 0
    most_caloric_food = ""

    try:
        with open('food_log.txt', 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(', ')
                if len(parts) >= 3 and parts[0] == date:
                    try:
                        calories = int(parts[2])
                        if calories > max_calories:
                            max_calories = calories
                            most_caloric_food = parts[2]
                    except ValueError:
                        continue
            return most_caloric_food
    except FileNotFoundError:
        return  'файл не найден'



print(get_daily_calories('2025-09-02'))

print(get_most_caloric_food('2025-09-02'))

