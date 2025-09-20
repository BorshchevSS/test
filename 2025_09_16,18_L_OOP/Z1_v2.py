class Employee:

    def __init__(self, name, position, salary, **kwargs): #**kwargs - позволяет добавлять увелить количество именованных значений
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

    def get_info(self):
        return super().get_info() + f"Team Size: {self.team_size}"





class Developer(Employee):
    def __init__(self, pr_language, **kwargs):
        super().__init__(**kwargs)
        self.pr_language = pr_language

    def write_code(self):
        return f"Напишу сод на {self.pr_language}"

class TechLead(Manager, Developer):
    def __init__(self, name, position, salary, team_size, pr_language):
        super().__init__(name=name, position=position, salary=salary, team_size=team_size, pr_language=pr_language)
