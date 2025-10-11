
class StudentManager:
    _students = []  # список всех студентов

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Метод экземпляра: добавляет оценку студенту"""
        if self.is_valid_grade(grade):
            self.grades.append(grade)
            print(f"Оценка {grade} добавлена студенту {self.name}")
        else:
            print(f"Ошибка: оценка {grade} недопустима!")

    def calculate_average(self):
        """Метод экземпляра: вычисляет среднюю оценку студента"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_student_average(self):
        """Метод экземпляра: выводит среднюю оценку студента"""
        average = self.calculate_average()
        if average > 0:
            print(f"Средняя оценка студента {self.name}: {average:.2f}")
        else:
            print(f"У студента {self.name} нет оценок")

    @classmethod
    def add_student(cls, name):
        """Метод класса: добавляет нового студента"""
        student = cls(name)
        cls._students.append(student)
        print(f"Студент {name} добавлен")
        return student

    @classmethod
    def calculate_class_average(cls):
        """Метод класса: вычисляет среднюю оценку всех студентов"""
        if not cls._students:
            return 0

        total_grades = []
        for student in cls._students:
            total_grades.extend(student.grades)

        if not total_grades:
            return 0

        return sum(total_grades) / len(total_grades)

    @classmethod
    def display_class_average(cls):
        """Метод класса: выводит среднюю оценку всех студентов"""
        average = cls.calculate_class_average()
        if average > 0:
            print(f"Средняя оценка всех студентов: {average:.2f}")
        else:
            print("Нет данных об оценках студентов")

    @classmethod
    def find_student(cls, name):
        """Метод класса: находит студента по имени"""
        for student in cls._students:
            if student.name == name:
                return student
        return None

    @classmethod
    def display_all_students(cls):
        """Метод класса: отображает всех студентов"""
        if not cls._students:
            print("Нет зарегистрированных студентов")
            return

        print("\nСписок всех студентов:")
        for i, student in enumerate(cls._students, 1):
            avg = student.calculate_average()
            grades_str = ', '.join(map(str, student.grades)) if student.grades else "нет оценок"
            print(f"{i}. {student.name}: оценки [{grades_str}], средняя: {avg:.2f}")

    @staticmethod
    def is_valid_grade(grade):
        """Статический метод: проверяет допустимость оценки"""
        return isinstance(grade, (int, float)) and 1 <= grade <= 5


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


# Демонстрация работы программы
if __name__ == "__main__":
    # Пример использования
    print("Демонстрация работы программы:")

    # Создаем студентов
    student1 = StudentManager.add_student("Иван Иванов")
    student2 = StudentManager.add_student("Мария Петрова")

    # Добавляем оценки
    student1.add_grade(4)
    student1.add_grade(5)
    student1.add_grade(3)

    student2.add_grade(5)
    student2.add_grade(4)
    student2.add_grade(5)

    # Пытаемся добавить недопустимую оценку
    student1.add_grade(6)  # Должно выдать ошибку

    # Выводим средние оценки
    student1.display_student_average()
    student2.display_student_average()
    StudentManager.display_class_average()

    # Проверяем допустимость оценок
    print(f"Оценка 3 допустима: {StudentManager.is_valid_grade(3)}")
    print(f"Оценка 0 допустима: {StudentManager.is_valid_grade(0)}")

    print("\n" + "="*50)

    # Запускаем интерактивный режим
    main()

"""
Этот код реализует все требуемые функции:

## Основные возможности:

1. **Методы экземпляра**:
   - `add_grade()` - добавляет оценку студенту
   - `calculate_average()` - вычисляет среднюю оценку студента
   - `display_student_average()` - выводит среднюю оценку студента

2. **Методы класса**:
   - `add_student()` - добавляет нового студента
   - `calculate_class_average()` - вычисляет среднюю оценку всех студентов
   - `find_student()` - находит студента по имени
   - `display_all_students()` - показывает всех студентов

3. **Статический метод**:
   - `is_valid_grade()` - проверяет, находится ли оценка в диапазоне 1-5

## Особенности программы:

- Данные хранятся в списке `_students` класса
- Реализована обработка ошибок для недопустимых оценок
- Интерактивное меню для удобства пользователя
- Возможность добавлять несколько оценок за раз
- Проверка на существование студентов
- Форматированный вывод результатов

Программа корректно обрабатывает все указанные сценарии и предоставляет удобный интерфейс для управления данными студентов."""