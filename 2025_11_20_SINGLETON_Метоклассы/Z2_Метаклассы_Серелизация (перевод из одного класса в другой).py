"""Задание 2. Автоматическое создание сериализуемых классов
Напишите метакласс SerializableMeta,
который будет добавлять к классу методы сериализации и десериализации (to_dict и from_dict).
Метакласс должен автоматически определять все атрибуты класса и включать их в результат работы метода to_dict.
Это полезно для работы с API и базами данных.
Условия:
• Атрибуты должны сериализоваться рекурсивно, если они содержат экземпляры других классов.
• Метод from_dict должен восстанавливать экземпляр класса из словаря.
• Исключение для private-атрибутов (начинающихся с _)."""

class SerializableMeta(type):
    def __new__(cls, name, bases, attrs):
        def to_dict(self): # преобразовываем в словать
            data = {}
            for key, value in self.__dict__.items():
                if key.startswith("_"):
                    continue
                if hasattr(value, "to_dict") and callable(value.to_dict): #рекурсия
                    print(key, value)
                    data[key] = value.to_dict()
                    print(data[key])
                else:
                    data[key] = value
                    print(data[key])
            return data

        @classmethod
        def from_dict(cls, data):
            return cls(**data)

        attrs["to_dict"] = to_dict
        attrs["from_dict"] = from_dict
        return super().__new__(cls, name, bases, attrs)

#Тестирование
#класс для вложенного объекта
class User(metaclass=SerializableMeta):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

#Класс для основного объекта
class Order(mataclass=SerializableMeta):
    def __init__(self, order_id = None, status=None, user=None, _protected_note=None, **kwargs):
        self.order_id = order_id
        self.status = status
        self._protected_note = _protected_note
        user_data_input = user #в user попадает объект User или словарь
        if isinstance(user_data_input, dict):
            self.user = User.from_dict(user_data_input)
        elif isinstance(user_data_input, User):
            self.user = user_data_input
        else:
            self.user = None

user = User(user_id="111", name="Kate")
order = Order(
    order_id="0123",
    status="process",
    user=user,
    _protected_note="do not show this"
)

order_dict = order.to_dict()
print(order_dict)
restore_order = Order.from_dict(order_dict)
print(restore_order)
print(type(restore_order.user))
print(restore_order.user.name)

assert restore_order.order_id == "0123"
assert restore_order.user.user_id == "111"
