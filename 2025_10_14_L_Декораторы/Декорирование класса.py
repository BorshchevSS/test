class Decorator:
    def __init__(self, func):
        self.func = func
        self.count = 0

        print(f"{self.func.__name__} готов")


    def __call__(self, *args, **kwargs):
# Вызываем класс как объект (аналог wraper в обычной функции)
        self.count += 1
        print(f"{self.func.__name__}. Вызов №{self.count}")
        return self.func(*args, **kwargs)

@Decorator
def test(name):
    return f"hello, {name}"

print(test("a"))
print(test("b"))
print(test("c"))
print(test.count)
print(type(test))