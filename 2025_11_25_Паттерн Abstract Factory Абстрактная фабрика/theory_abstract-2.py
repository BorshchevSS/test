from abc import ABC, abstractmethod

# Abstract Product (Оружие и Щит)
class Weapon(ABC):
    @abstractmethod
    def hit(self):
        pass

class Shield(ABC):
    @abstractmethod
    def defend(self):
        pass

# Concrete Products (Эльфийский меч, Топор Орка)

class ElfWeapon(Weapon):
    def hit(self):
        return 'Эльфийский меч наносит удар'

class OrcWeapon(Weapon):
    def hit(self):
        return 'Топор Орка наносит удар'


class ElfShield(Shield):
    def defend(self):
        return 'Эльфийский щит обеспечивает защиту'

class OrcShield(Shield):
    def defend(self):
        return 'Орочий щит обеспечивает защиту'

# Abstract Factory
class ArmyFactory(ABC):
    @abstractmethod
    def create_weapon(self):
        pass

    @abstractmethod
    def create_shield(self):
        pass

#   Concrete Factories

class ElfFactory(ArmyFactory):
    def create_weapon(self):
        return ElfWeapon()

    def create_shield(self):
        return ElfShield()

class OrcFactory(ArmyFactory):
    def create_weapon(self):
        return OrcWeapon()
    def create_shield(self):
        return OrcShield()

def client_code(factory: ArmyFactory):
    weapon = factory.create_weapon()
    shield = factory.create_shield()
    print(f'новое снаряжение: {weapon.__class__.__name__} и'
          f'{shield.__class__.__name__}')
    print(weapon.hit())
    print(shield.defend())

client_code(ElfFactory())
client_code(OrcFactory())
