class RecipeIterator:
    """
    Класс-итератор для шагов рецепта
    """

    def __init__(self, instructions):
        self.instructions = instructions
        self.index = 0
        self.completed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.instructions):
            self.completed = True
            raise StopIteration

        step_number = self.index + 1
        instruction = self.instructions[self.index]
        self.index += 1
        return step_number, instruction

    def get_progress(self):
        """Возвращает прогресс в процентах"""
        if not self.instructions:
            return 100
        return min(100, (self.index / len(self.instructions)) * 100)


def run_recipe_iterator(instructions):
    """
    Реализация с использованием кастомного итератора
    """
    print("Рецепт начинается! Следуйте инструкциям.\n")

    # Создаем итератор
    recipe_iter = RecipeIterator(instructions)

    try:
        while True:
            # Получаем текущий прогресс ДО получения следующего шага
            progress = recipe_iter.get_progress()
            print(f"Прогресс: {progress:.1f}%")

            # Получаем следующий шаг
            step_number, instruction = next(recipe_iter)

            # Показываем шаг
            input(f"Шаг {step_number}/{len(instructions)}: {instruction}\n(Нажмите Enter для продолжения...)\n")

    except StopIteration:
        print("\n🎉 Поздравляем! Вы завершили рецепт!")

# Список шагов рецепта
recipe_instructions = [
    "Подготовить все ингредиенты.",
    "Нарезать овощи кубиками.",
    "Обжарить лук до золотистого цвета.",
    "Добавить морковь и тушить 5 минут.",
    "Залить водой и довести до кипения.",
    "Посолить и поперчить по вкусу.",
    "Подавать горячим."
]

# Запускаем с итератором
run_recipe_iterator(recipe_instructions)