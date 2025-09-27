#Абстрактный класс (шаблон для класса)
#raise NotImplementedError
from abc import ABC, abstractmethod

class PayProcess(ABC): #Абстрактный класс,
    """Абстрактный класс имеет хотя бы один абстрактный метод"""
    def __init__(self, amount):
        self.amount = amount
    """Абстрактный метод - метод, который не имеет реализации (будет реализован в дочерних классах)"""
    @abstractmethod
    def pay(self, amount):
        pass

    def info(self):
        print("Это обычный метод")


class CreditPayProcess(PayProcess):
    def pay(self, amount):
        self.amount += amount
        return f"Credit pay: {self.amount}"

#pp = PayProcess(100)
cpp = CreditPayProcess(200)
print(cpp.pay(200))
cpp.info()