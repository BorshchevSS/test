# Дескрипторы
# @property
# # __get__  __set__  __delete__
# class MyDescriptor:
#     def __get__(self, instance, owner): #Non-data, только метод get
#         print('метод __get__')
#         return 42
#
# class MyClass:
#     attr = MyDescriptor()
# obj = MyClass()
# obj.attr = 'new value'
# print(obj.attr)
class MyDescriptor:
    def __get__(self, instance, owner):
        return 'данный дескриптор'

    def __set__(self, instance, value):
        print(f'установка значения {value}, {instance}')

    def __delete__(self, instance):
        print('удаление')
        del instance.__dict__['attr']
        # instance - obj, self-attr

class MyClass:
    attr = MyDescriptor()

obj = MyClass()
obj.attr = 'new value' #вызывается метод set
print(obj.attr)# вызывается метод get
del obj.attr #удаление значения через delete
