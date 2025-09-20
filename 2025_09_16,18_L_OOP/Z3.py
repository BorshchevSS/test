"""5p Разработайте классы для банковской системы.

Требования:
( Базовый класс Account с атрибутами owner (владелец) и
balance (баланс)p
( Дочерние классы2
1 SavingsAccount (добавьте атрибут interest_rate –
процентная ставка)p
1 CreditAccount (атрибут credit_limit)p
( Класс PremiumAccount должен наследоваться и от
SavingsAccount, и от CreditAccountp
( Реализуйте методы deposit() и withdraw().

premium = PremiumAccount("Анна", 50000, interest_rate=5,
credit_limit=100000)
premium.deposit(10000)
premium.withdraw(20000)"""


class Account:
    def __init__(self, owner, balance): #Базовый класс Account с атрибутами owner (владелец) и balance (баланс)
        self.owner = owner
        self.balance = balance

    # пополнение
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит: {amount}, Новый баланс: {self.balance}")
        else:
            print("Сумма должна быть положительной")

    # снятие
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Снятие: {amount}, Новый баланс: {self.balance}")
            else:
                print("Недостаточно средств")
        else:
            print("Сумма должна быть положительной")


class  SavingsAccount(Account):
    def __init__(self, owner, balans, interest_rate=15):
        super().__init__(owner,balans)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
        print(f"Начислен процент на остаток {interest}")

    def __str__(self):
        return f"Сберегательный счет {self.owner}. Баланс: {self.balance}"

class CreditAccount(Account):
    def __init__(self, owner, balance, credit_limit = 20000):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    # Переопределяем метод родительского класса
    def withdraw(self, amount):
        if amount > 0:
            if self.balance + self.credit_limit >= amount:
                self.balance -= amount
                print(f"Снятие: {amount}, Новый баланс: {self.balance}")
            else:
                print("Превышен кредитный лимит")
        else:
            print("Сумма должна быть положительной")


class PremiumAccount (SavingsAccount, CreditAccount):
    def __init__(self, owner, balance, interest_rate=20, credit_limit = 20000):
        Account.__init__(self, owner, balance)
        self.interest_rate = interest_rate
        self.credit_limit = credit_limit

premium = PremiumAccount("Катя", 200000)
premium.deposit(10000)
premium.withdraw(150000)
premium.add_interest()
print(premium.balance)
premium.withdraw(300000)