from abc import ABC, abstractmethod

#Abstract Product (Оружие и Щит)
class Weapon(ABC):
    @abstractmethod
    def hit(self):
        pass

class Shield(ABC):
    @abstractmethod
    def defend(self):
        pass

# Concrrete Products (Эльфийский меч, Топор орка)

class ElfWeapon(Weapon):
    def hit(self):
        return ""