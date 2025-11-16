def generator():
    """При обращении замораживает состояние"""
    yield 1
    yield 2
    yield 3

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))