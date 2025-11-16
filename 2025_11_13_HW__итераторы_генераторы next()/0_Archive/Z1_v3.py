class Recipe:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        self.current_step_index = 0
        self.completed = False

    def get_current_step(self):
        """Возвращает текущий шаг или None если рецепт завершен"""
        if self.completed:
            return None
        return self.instructions[self.current_step_index]

    def go_to_next_step(self):
        """Переходит к следующему шагу"""
        if self.current_step_index < len(self.instructions) - 1:
            self.current_step_index += 1
            return True
        else:
            self.completed = True
            return False

    def go_to_previous_step(self):
        """Возвращается к предыдущему шагу"""
        if self.current_step_index > 0:
            self.current_step_index -= 1
            self.completed = False
            return True
        return False

    def restart(self):
        """Начинает рецепт заново"""
        self.current_step_index = 0
        self.completed = False

    def get_progress(self):
        """Возвращает прогресс в процентах"""
        return (self.current_step_index + 1) / len(self.instructions) * 100

# Использование класса Recipe
def main():
    # Создаем рецепт
    borscht_recipe = Recipe(
        name="Классический борщ",
        instructions=[
            "Подготовить все ингредиенты.",
            "Нарезать овощи кубиками.",
            "Обжарить лук до золотистого цвета.",
            "Добавить морковь и тушить 5 минут.",
            "Залить водой и довести до кипения.",
            "Посолить и поперчить по вкусу.",
            "Подавать горячим."
        ]
    )

    print(f"Рецепт: {borscht_recipe.name}")
    print("Начинаем готовить!\n")

    # Основной цикл выполнения рецепта
    while not borscht_recipe.completed:
        current_step = borscht_recipe.get_current_step()
        progress = borscht_recipe.get_progress()

        print(f"Прогресс: {progress:.1f}%")
        print(f"Шаг {borscht_recipe.current_step_index + 1}/{len(borscht_recipe.instructions)}:")
        print(f"➡️  {current_step}")

        command = input("\nВведите 'n' для следующего шага или 'q' для выхода: ").lower()

        if command in ['n', 'next', '']:
            if not borscht_recipe.go_to_next_step():
                print("\n🎉 Поздравляем! Вы завершили рецепт!")
        elif command in ['q', 'quit']:
            print("Выход из рецепта.")
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")

        print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()