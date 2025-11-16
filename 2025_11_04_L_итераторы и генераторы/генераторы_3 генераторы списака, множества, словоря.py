import sys

num_list = [x**2 for x in range(1000000)] # списковое включение
num_gen = (x**2 for x in range(1000000)) # генераторное выражение (КРУГЛЫЕ СКОБКИ, оператор yield уже зашит в логике)
sq_dict = {x: x**2 for x in range(1000000)}

print(f"Размер списка: {sys.getsizeof(num_list)} байт (сразу же рассчитывает значения и хранит их)")
print(f"Размер генератора: {sys.getsizeof(num_gen)} байт (не хранит значение, хранит рецепт расчета)")
print(f"Размер : {sys.getsizeof(sq_dict)} байт")