import random
from abc import ABC, abstractmethod

# дескриптор для проверки на отрицательность числа
class PositiveNumDescriptor:
    def __set_name__(self, owner, name):
        self.name = name #запоминаем имя атрибута

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if not instance(value, (int, float)) or value <= 0:
            raise ValueError(f'{self.name} должно быть положительным')
        instance.__dict__[self.name] = value

#класс для заклинаний
class Spell(ABC):
    def __init__(self, name, cost):
        self.name = name #название заклинания
        self.cost = cost # стоимость заклинания

    @abstractmethod
    def cast(self, caster, target):
        pass

    def __str__(self):
        return f'{self.name} (стоимость: {self.cost})'

class Fireball(Spell):
    def __init__(self):
        super().__init__('Огненный шар', 15)

    def cast(self, caster, target):
        damage = random.randint(10, 25) #урон
        target.health = max(0, target.health - damage)
        caster.magic_power -= damage
        print(f'{caster.name} запускает {self.name} в '
              f'{target.name} и наносит {damage} урона!')
        return target.health == 0 #если цель побеждена True

class Lightning(Spell):
    def __init__(self):
        super().__init__('Молния', 25)

    def cast(self, caster, target):
        damage = random.randint(20, 35) #урон
        target.health = max(0, target.health - damage)
        caster.magic_power -= damage
        print(f'{caster.name} запускает {self.name} в '
              f'{target.name} и наносит {damage} урона!')
        return target.health == 0 #если цель побеждена True

class Healing(Spell):
    def __init__(self):
        super().__init__('Исцеление', 20)

    def cast(self, caster, target):
        heal_amount = random.randint(15, 30)
        caster.health += heal_amount
        caster.magic_power -= heal_amount
        print(f'{caster.name} исцеляет себя на '
              f'{heal_amount} единиц здоровья')
        return False #так как никто не побеждает

class Mage:
    health = PositiveNumDescriptor()
    magic_power = PositiveNumDescriptor()

    def __init__(self, name, health, magic_power):
        self.name = name
        self.health = health
        self.magic_power = magic_power
        self._spells = []

    def learn_spell(self, spell):
        #знает ли маг это заклинание
        if spell not in self._spells:
            self._spells.append(spell)
            print(f'{self.name} выучил заклинание {spell.name}')
        else:
            print(f'{self.name} уже знает это заклинание')

    def cast_spell(self, spell, target):
        if spell not in self._spells:
            print(f'{self.name} не знает этого заклинания!')
            return False
        if self.magic_power < spell.cost:
            print(f'У {self.name} недостаточно силы')
            return False

        return spell.cast(self, target)

    @property
    def spells(self):
        return self._spells.copy()

    @classmethod
    def get_available_spells(cls):
        return [Fireball(), Healing(), Lightning()]
    #список доступных заклинаний

    @staticmethod
    def create_random_mage(name):
        health = random.randint(70, 120)
        magic_power = random.randint(50, 100)
        return Mage(name, health, magic_power)

    def is_dead(self):
        return self.health == 0 #побежден ли маг

    def __str__(self):
        return (f'{self.name} (Здоровье: {self.health},'
                f'Магия: {self.magic_power})')

#доступные заклинания мага
def show_available_spells(mage):
    available_spells = [spell for spell in mage.spells
                        if spell.cost <= mage.magic_power]
    if available_spells:
        print('нет доступных заклинаний')
        return False

    print('\nДоступные заклинания')
    for i, spell in enumerate(available_spells, 1):
        print(f'{i}. {spell}')

    while True:
        try:
            choice = input("Выберете номер заклинания или П для пропуска хода").strip().lower()



