class Employee:
    WORK_HOURLY = 2080

    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"Имя: {self.name}, Должность:{self.position} , Ставка:{self.salary:.2f} руб/час"

    @classmethod
    def from_str(cls, str_crm: str):
        try:
            name, position, year_salary = str_crm.split(";")
            year_salary = float(year_salary)
            salary = year_salary / cls.WORK_HOURLY
            return cls(name, position, salary)
        except ValueError:
            print("Ошибка при парсинге строки CRM")
            return None

    @classmethod
    def from_dict(cls, data: dict):
        try:
            return cls(
                name=data["name"],
                position=data["position"],
                salary=data["salary"]
            )
        except KeyError:
            print("Ошибка: неверный формат данных")
            return None

emp1 = Employee("Петр", "Бухгалтер", 200)
print(emp1.get_info())

crm_dada = "Екатерина Смирнова;Продавец;200000"
emp2 = Employee.from_str(crm_dada)
if emp2:
    print(emp2.get_info())

data_dict = {
    "name": "Иван",
    "position": "Маркетолог",
    "salary": 1400
}

emp3 = Employee.from_dict(data_dict)
if emp3:
    print(emp3.get_info())