#Абстрактный класс (шаблон для класса)
#raise NotImplementedError
from abc import ABC, abstractmethod

class PayProcess:
    def __init__(self, amout):
        self.amout = amout

    def pay(self):
        #pass
        raise NotImplementedError()

class CreditPayProcess(PayProcess):
    pass

pp = PayProcess(100)
cpp = CreditPayProcess(200)
cpp.pay()