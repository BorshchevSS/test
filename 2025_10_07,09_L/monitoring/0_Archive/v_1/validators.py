class PercentageValidator:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name            #"""Сохраняем имя атрибута"""

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Должно быть числом")
        if not 0 <= value <= 100:
            raise ValueError("Должно быть от 0 до 100")

        rounded_value = round(value, 2) # округлять до 2 знаков
        setattr(instance, self.private_name, rounded_value)
        #setattr(объект, имя_атрибута, значение_атрибута) - устанавливает объекту значение атрибута