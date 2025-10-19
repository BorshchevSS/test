from functools import  wraps
#Декоратор позволяет сохранить и использовать методанные
#__name__
#__doc__

def simple_dec(func):
    @wraps(func) #Добавление декоратора позволяет сохранить название и методанные задекорированной функции
    def wrapper(*args, **kwargs):
        print(f"вызов {func.__name__}")
        res = func(*args, **kwargs)
        print("end")
        return res
    return wrapper

@simple_dec
def calc(a,  b):
    """Здесь находится информация (примечание, комментарий) о функции 'calc', Сложение функций"""
    return a+b

@simple_dec
def hello():
    """Здесь информация (примечание, комментарий) о функции hello, doc"""
    print("Hello")

    return "hello"

print(calc.__name__)
print(calc.__doc__)

print(hello.__name__)
print(hello.__doc__)