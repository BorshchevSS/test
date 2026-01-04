"""Метаклассы
Задание 1. Метакласс для ограничения наследования
Создайте метакласс FinalMeta, который запретит наследование от классов, использующих этот метакласс.
Это может использоваться, когда у вас есть класс, который должен оставаться финальным и не наследоваться далее.
Условия:
• Поднятие исключения при попытке создания класса-наследника.
• Поддержка пользовательских сообщений для исключения, которые объясняют причину запрета.
• Возможность указать список исключений, от которых можно наследоваться."""

class FinalClassError(TypeError):
    """Пользовательское исключение при попытке наследования от финального класса
    TypeError - ошибка в системе типов и наследования
    """
    pass


class FinalMeta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        default_message = f"ERROR! Класс {name} финальный (нельзя наследовать)"
        for base in bases:
            if isinstance(base, FinalMeta):
                base_message = getattr(base, "FinalMeta__message", default_message)
                allowed_subclasses = getattr(base, "FinalMeta__allowed_subclasses", ())
                if name not in allowed_subclasses:
                    raise FinalClassError(base_message)
        return super().__new__(cls, name, bases, attrs, **kwargs)

class BaseFinal(metaclass=FinalMeta):
    def final_method(self):
        return "Финальный метод"

class ConfigError(metaclass=FinalMeta):
    FinalMeta__message = " наследование от класса ConfigError запрещено"
    pass

class AllowedFinal(metaclass=FinalMeta):
    FinalMeta__allowed_subclasses = ("Spec", )

base_instance = BaseFinal()
try:
    class ChildBase(BaseFinal):
        pass

except FinalClassError as e:
    print(e)


try:
    class ChildConfig(ConfigError):
        pass
except FinalClassError as e:
    print(e)

class Spec(AllowedFinal):
    print("Наследник успешно создан")
    pass


