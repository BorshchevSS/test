class InteractiveRecipe:
    """
    Интерактивный рецепт с возможностью управления через next()
    """

    def __init__(self, instructions):
        self.instructions = instructions
        self.iterator = iter(enumerate(instructions, 1))
        self.current_step = None
        self.completed = False

    def next_step(self):
        """
        Переходит к следующему шагу с помощью next()
        Возвращает True если шаг получен, False если рецепт завершен
        """
        try:
            self.current_step = next(self.iterator)
            return True
        except StopIteration:
            self.completed = True
            return False

    def display_current_step(self):
        """Показывает текущий шаг"""
        if self.current_step:
            step_number, instruction = self.current_step
            print(f"Шаг {step_number}/{len(self.instructions)}: {instruction}")
        else:
            print("Рецепт еще не начат. Используйте next_step() для начала.")

    def run_interactive(self):
        """Запускает интерактивное выполнение рецепта"""
        print("Рецепт начинается! Используйте команды для навигации.\n")

        # Получаем первый шаг
        if not self.next_step():
            print("Рецепт пустой!")
            return

        while not self.completed:
            # Показываем текущий шаг
            self.display_current_step()

            # Запрашиваем действие
            command = input("\nВведите 'n' для следующего шага, 'c' для повтора текущего или 'q' для выхода: ").lower()

            if command in ['n', 'next', '']:
                if not self.next_step():
                    print("\n🎉 Поздравляем! Вы завершили рецепт!")
            elif command in ['c', 'current']:
                print("Повтор текущего шага...")
            elif command in ['q', 'quit']:
                print("Выход из рецепта.")
                break
            else:
                print("Неизвестная команда. Попробуйте снова.")

            print("-" * 40)

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


# Использование интерактивного рецепта
interactive_recipe = InteractiveRecipe(recipe_instructions)
interactive_recipe.run_interactive()