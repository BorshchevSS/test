# # # OOP
# #
# # # n = 5
# # # s = 'asd'
# # # l1 = [1, 3, 4]
# # # def func():
# # #     pass
# # #
# # # class Test:
# # #     pass
# # #
# # # print(type(n))
# # # print(type(s))
# # # print(type(l1))
# # # print(type(func))
# # # print(type(Test))
# #
# #
# # class Dog:
# #
# #     def __init__(self, name_arg, age_arg, breed_arg='taksa'):
# #         self.name = name_arg
# #         self.age = age_arg
# #         self.breed = breed_arg
# #
# #     # name = 'Luna'
# #     # age = 5
# #     #self-указатель на объект
# #     def wooff(self, owner):
# #         print(f'"Woof Woof" say {self.name} ({owner})')
# #
# #     def __str__(self): #строковое представление объекта
# #         return f'{self.name} {self.age} {self.breed}'
# #
# #
# # dog1 = Dog('Luna', 6)
# # dog2 = Dog('Bobik', 3, 'овчарка')
# # dog3 = Dog('Jim', 2)
# # owner = input('Enter your name: ')
# # dog1.wooff(owner)
# # # dog2.wooff()
# # # dog3.wooff()
# # print(dog1)
# #
# # # print(dog1.name, dog1.age)
# # # dog1.wooff()
# # # dog1.name = 'Bobik'
# # # print(dog1.name)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# class Transport:
#     def __init__(self, speed, color, brand):
#         self.speed = speed
#         self.color = color
#         self.brand = brand
#
#     def sound(self):
#         print(f'Beep beep')
#
# class Car(Transport):
#     def __init__(self, speed_p, color_p, brand_p, seats):
#         super().__init__(speed_p, color_p, brand_p)
#         self.seats = seats
#
#     def beeeeep(self):
#         print('какой-то звук')
#
#     def sound(self):
#         print('beep')
#
# car = Car(250, 'red', 'bmw', 3)
# print(car.color)
# car.sound()
# car.beeeeep()

class Employee:

    def __init__(self, name, position, salary, **kwargs):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return (f'Name: {self.name}, Position: {self.position},'
                f' Salary: {self.salary}')

class Manager(Employee):

    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

    def get_info(self):
        return super().get_info() + f'Team Size: {self.team_size}'

class Developer(Employee):

    def __init__(self, pr_lang, **kwargs):
        super().__init__(**kwargs)
        self.pr_lang = pr_lang

    def write_code(self):
        return f'write code on {self.pr_lang}'


class TechLead(Manager, Developer):

    def __init__(self, name, position, salary, team_size, pr_lang):
        super().__init__(name=name, position=position, salary=salary,
                         team_size=team_size, pr_lang=pr_lang)

# (MRO)
t1 = TechLead('Ivan', 'Teach Lead', 3000000, 10, 'C++')
print(t1.write_code())
print(t1.get_info())


