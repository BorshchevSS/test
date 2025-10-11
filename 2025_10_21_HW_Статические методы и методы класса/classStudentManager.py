#Класс: Студент (Имя, Список оценок)
#Функция: добавление студента (экземпляра класса студент)

'''Описание задачи: создайте программу, которая управляет данными о студентах и их средних оценках, используя методы
экземпляра, методы класса и статические методы. Программа должна:
1. Позволять добавлять студентов с именем и списком их оценок.
2. Вычислять и выводить среднюю оценку студента.
3. Вычислять и выводить среднюю оценку всех студентов с помощью метода класса.
4. Проверять, является ли оценка допустимой (от 1 до 5), с помощью статического метода.
Указания:
1. Используйте метод экземпляра для добавления студентов и вычисления средней оценки для каждого студента.
2. Используйте метод класса для вычисления средней оценки всех студентов.
3. Реализуйте статический метод для проверки допустимости оценки.
4. Данные о студентах должны храниться в списке в классе.
5. Предусмотрите обработку ошибок, если передаётся некорректная оценка.
Ожидаемый результат:
1. Программа запрашивает действия у пользователя:
2. Добавить нового студента.
3. Добавить оценки студенту.
4. Вывести среднюю оценку студента.
5. Вывести среднюю оценку всех студентов.
6. Проверить допустимость оценки.
2. Программа корректно вычисляет средние значения.
3. При вводе недопустимой оценки (например, 6 или 0) программа выдаёт предупреждение.'''

class StudentManager:
    """Класс для управления студентами"""
    _students = [] # список всех студентов

    def __init__(self, name_student):
        self.name_student = name_student
        self.grades = [] # оценки студента (при создании экземпляра класса "Студент" список создается пустой

    def add_grade(self, grade):
        """Метод экземпляра: добавляет оценку студенту"""
        if self.is_valid_grade(grade):  # Если оценка проходит проверку
            self.grades.append(grade)
            print(f"Оценка {grade} добавлена студенту {self.name_student}")
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
            print(f"Средняя оценка студента {self.name_student}: {average:.2f}")
        else:
            print(f"У студента {self.name_student} нет оценок")

    @classmethod
    def add_student(cls, name_student):
        """Метод класса: добавляет нового студента"""
        """@classmethod в Python используется для определения метода, который привязан к классу, а не к его экземплярам.
         Он помечается декоратором @classmethod и автоматически принимает сам класс в качестве первого аргумента (по общепринятому соглашению, cls). 
         Это позволяет работать с классовыми атрибутами или использовать класс в качестве фабрики для создания экземпляров, даже когда метод вызывается из дочернего класса. """
        student = cls(name_student) # создаю объект класса StudentManager
        cls._students.append(student) # добавляю объект в переменную в которой хранится список студентов
        print(f"Студент {student} добавлен")
        return student

    @classmethod
    def calculate_class_average(cls):
        """Метод класса: ВЫЧИСЛЯЕТ среднюю оценку всех студентов"""
        if not cls._students: # Если студентов нет
            return 0
        total_grades = []
        for student in cls._students: # Если студенты есть
            total_grades.extend(student.grades)
        if not total_grades: # Если у студентов нет оценок
            return 0
        return sum(total_grades) / len(total_grades)

    @classmethod
    def display_class_average(cls):
        """Метод класса: ВЫВОДИТ среднюю оценку всех студентов"""
        average = cls.calculate_class_average()
        if average > 0:
            print(f"Средняя оценка всех студентов: {average:.2f}")
        else:
            print("Нет данных об оценках студентов")

    @classmethod
    def find_student(cls, name_student):
        """Метод класса: находит студента по имени"""
        for student in cls._students:
            if student.name_student == name_student:
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
            print(f"{i}. {student.name_student}: оценки [{grades_str}], средняя: {avg:.2f}")

    @staticmethod
    def is_valid_grade(grade):
        """Статический метод: проверяет допустимость оценки"""
        return isinstance(grade, (int, float)) and 1 <= grade <= 5


    def __str__(self):
        return f"\nИмя студента: {self.name_student}; список оценок: {", ".join(map(str, self.grades))}" #Тут функция map применяет функцию str (перевод в строку) к каждому элементу объекта grades; метод join() объединяет элементы

    def __repr__(self):
        return f"StudentManager('{self.name_student}', '{self.grades}')"







# st1 = StudentManager("BSS")
# print(st1)


# gr1 = [2,4,5]
# gr11 = map(str, gr1)
# #so = gr1[i] for i in range(len(gr1))
#
# so = ", ".join(map(str, gr1))
# print(", ".join(map(str, gr1)))

if __name__ == "__main__":
    pass