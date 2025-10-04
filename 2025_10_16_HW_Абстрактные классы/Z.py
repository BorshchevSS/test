"""Иерархия сотрудников и задачи проекта

Требования: Создайте систему классов для управления сотрудниками, задачами и проектами в компании.
1. Создайте абстрактный класс Employee с атрибутами:
◦ Имя
◦ Роль (менеджер, разработчик и т.д.)
◦ Метод work(), который будет реализован в подклассах для выполнения конкретных обязанностей.

2. Создайте классы для разных типов сотрудников:
◦ Developer (разработчик): реализуйте метод work() для выполнения программирования.
◦ Tester: реализуйте метод work() для тестирования кода.
◦ Manager: метод work() будет управлять командой.

3. Создайте класс Task, который содержит задачу и ссылку на сотрудника, который её выполняет.
4. Создайте класс Project, который содержит несколько задач и сотрудников.
Перегрузите операторы сравнения для сотрудников (==, >, <), чтобы можно было сравнивать сотрудников по количеству выполненных задач.

Используйте множественное наследование, например, для создания класса LeadDeveloper, который является
одновременно разработчиком и менеджером, чтобы он мог выполнять обе роли (программировать и управлять командой)."""

from abc import ABC, abstractmethod

class Employee(ABC):
    """Абстрактный класс Employee с атрибутами:◦ Имя; ◦ Роль (менеджер, разработчик и т.д.)"""
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def work(self):
        """Метод work(), который будет реализован в подклассах для выполнения конкретных обязанностей."""
        pass

    def __str__(self):
        return f"\nИмя работника: {self.name};\n роль: {self.role}"

    def __repr__(self):
        return f"Employee(ABC)('{self.name}', {self.role})"

class Developer(Employee):
    def __init__(self, name, role = "разработчик ПО"):
        super().__init__(name, role)

    def work(self):
        return f"{self.name} - разработчик ПО, для выполнения программирования"

    def __str__(self):
        return f"\nИмя разработчика ПО: {self.name}"

    def __repr__(self):
        return f"Developer(Employee)('{self.name}', '{self.role}')"

class Tester(Employee):
    def __init__(self, name, role = "Тестировщик"):
        super().__init__(name, role)

    def work(self):
        return f"{self.name} - тестировщик кода"

    def __str__(self):
        return f"\nИмя тестировщика кода: {self.name}"

    def __repr__(self):
        return f"Tester(Employee)('{self.name}', '{self.role}')"

class Manager(Employee):
    def __init__(self, name, role = "Менеджер"):
        super().__init__(name, role)

    def work(self):
        return f"{self.name} - будет управлять командой"

    def __str__(self):
        return f"\nИмя управленца командой: {self.name}"

    def __repr__(self):
        return f"Manager(Employee)('{self.name}', '{self.role}')"

t_m = Manager("Name1")
t_d = Developer("БСС")
# print(t_m)
# print(t_m.__repr__())

class Task:
    def __init__(self, work: str, employee: Employee):
        if not isinstance(work, str) or not work:
            raise ValueError("Наименование работы должно быть непустой строкой")
        if not isinstance(employee, Employee):
            raise TypeError("В качестве исполнителя можно указать только объекты класса Employee")
        self.work = work
        self.employee = employee

    def __str__(self):
        return f"\nНаименование работы: {self.work}; имя исполнителя: {self.employee.name}"

    def __repr__(self):
        return f"Task('{self.work}', '{self.employee.name}')"

t_t = Task("Разработка сайта", t_d)
# print(t_t)

class Project:
    pass