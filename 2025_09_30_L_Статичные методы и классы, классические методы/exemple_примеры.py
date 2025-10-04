# @staticmethod
# @classmethod
from multiprocessing.pool import worker


class Converter:
    ed_iz = "" # атрибут класса
    def __init__(self, value):
        self.value = value

    @staticmethod #декоратор
    def cel_to_fah(celsius):
        return (celsius*9/5) + 32

print(Converter.cel_to_fah(9))
convert = Converter(25)
print(convert.cel_to_fah(20))



class Worker():
    percent = 1.05 #атрубут класса

    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary

    def get_full_name(self):
        return f"{self.name} {self.lastname}"

    @classmethod
    def set_up_percent(cls, new_percent):
        if new_percent > 1:
            cls.percent = new_percent
            print(cls.percent)
        else:
            print("должен быть больше 1")

    @classmethod
    def from_str(cls, str_worker):
        name, lastname, salary = str_worker.split("-")
        return cls(name, lastname, salary)

worker_str = "Вася-Пупкин-50000"
worker = Worker.from_str(worker_str)
print(worker.get_full_name())
print(Worker.percent)
Worker.set_up_percent(2.5)
print(Worker.percent)