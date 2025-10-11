from classStudentManager import StudentManager # Подключаю

def main():
    """Основная функция программы"""
    print("=== Система управления студентами ===")

    while True:
        print("\nДоступные действия:")
        print("1. Добавить нового студента")
        print("2. Добавить оценки студенту")
        print("3. Вывести среднюю оценку студента")
        print("4. Вывести среднюю оценку всех студентов")
        print("5. Проверить допустимость оценки")
        print("6. Показать всех студентов")
        print("7. Выйти")

        choice = input("\nВыберите действие (1-7): ").strip()

        if choice == '1':
            name = input("Введите имя студента: ").strip()
            if name:
                StudentManager.add_student(name)
            else:
                print("Ошибка: имя не может быть пустым!")

        elif choice == '2':
            name = input("Введите имя студента: ").strip()
            student = StudentManager.find_student(name)
            if student:
                try:
                    grades_input = input("Введите оценки через пробел: ").strip()
                    grades = [float(grade) for grade in grades_input.split()]

                    for grade in grades:
                        student.add_grade(grade)

                except ValueError:
                    print("Ошибка: введите числа через пробел!")
            else:
                print(f"Студент {name} не найден!")

        elif choice == '3':
            name = input("Введите имя студента: ").strip()
            student = StudentManager.find_student(name)
            if student:
                student.display_student_average()
            else:
                print(f"Студент {name} не найден!")

        elif choice == '4':
            StudentManager.display_class_average()

        elif choice == '5':
            try:
                grade = float(input("Введите оценку для проверки: ").strip())
                if StudentManager.is_valid_grade(grade):
                    print(f"Оценка {grade} допустима")
                else:
                    print(f"Оценка {grade} недопустима! Допустимый диапазон: 1-5")
            except ValueError:
                print("Ошибка: введите число!")

        elif choice == '6':
            StudentManager.display_all_students()

        elif choice == '7':
            print("Выход из программы...")
            break

        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == '__main__':
    main()