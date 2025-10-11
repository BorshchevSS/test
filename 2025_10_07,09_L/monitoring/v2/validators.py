class PercentageValidator:

    def __set_name__(self, owner, name):
        self.private_name = '_' + name
        #сохранили имя приватного атрибуты
        #защищенный атрибут

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError('должно быть числом')
        if not 0 <= value <= 100:
            raise ValueError('должно быть от 0 до 100')

        rounded_value = round(value, 2)
        setattr(instance, self.private_name, rounded_value)
        #setattr(объект, имя_атрибута, значение)

# obj = MyClass()
# obj.name = 'aaaa'
# print(obj.name)