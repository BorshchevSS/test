"""Вы создаете программное обеспечение для фабрики, которая производит роботов-художников.
Роботы умеют "рисовать" (генерировать строковые паттерны) и их можно комбинировать для создания сложных произведений."""

class PainterBot:
    """базовый класс PainterBot"""
    def __init__(self, name: str, style, efficiency: int):
        """проверки начальных значений"""
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(style, str) or not style:
            raise ValueError("Стиль рисования должен быть непустой строкой")
        if not isinstance(efficiency, int) or efficiency <= 0 or efficiency > 10:
            raise ValueError("Эффективность это целое число от 1 до 10")
        self.name = name # атрибут name - имя
        self.style = style # атрибут style - стиль рисования, например, "Пиксельный"
        self.efficiency = efficiency # эффективность, целое число от 1 до 10

    def paint(self, length: int, symbol = "#") -> str:
        """Метод paint(length): возвращает строку, представляющую рисунок длиной length.
        Базовая реализация: возвращает строку из length символов #."""
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Длина строки это целое число от 1 и более")
        return f"{symbol*length}"


    def __add__(self, other: 'PainterBot') -> 'PainterBot':
        """Объединение двух роботов"""
        if not isinstance(other, PainterBot):
            raise TypeError("Можно объединять только объекты PainterBot")


        new_name = f"Комбо [{self.name} + {other.name}]"
        new_efficiency = min(self.efficiency, other.efficiency)
        new_bot = ComboPainterBot(new_name, "Комбинированный", new_efficiency)
        return new_bot



    def __str__(self):
        return f"\nИмя робота: {self.name};\n стиль рисования: {self.style};\n эффективность: {self.efficiency} (эффективность, целое число от 1 до 10)"

    def __repr__(self):
        return f"PainterBot('{self.name}', {self.style}, {self.efficiency})"


class LinePainterBot(PainterBot):
    """класса-потомок, которые переопределяют метод paint;
    LinePainterBot (рисует линиями): его paint(length) возвращает строку из length символов =."""
    def __init__(self, name: str, style, efficiency: int):
        super().__init__(name, style, efficiency)

    def paint(self, length, symbol = "=") -> str:
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Длина строки это целое число от 1 и более")
        return f"{symbol*length}"


class WavePainterBot(PainterBot):
    """WavePainterBot (рисует волнами): его paint(length) возвращает строку,
    где символы ~ и - чередуются (например, для length=5: ~-~-~)."""
    def __init__(self, name: str, style, efficiency: int):
        super().__init__(name, style, efficiency)

    def paint(self, length, symbol = "~", symbol2 = "-") -> str:
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Длина строки это целое число от 1 и более")
        str_result = ""
        while True:
            if len(str_result) < length:
                str_result = str_result + symbol
            else:
                break
            if len(str_result) < length:
                str_result = str_result + symbol2
            else:
                break
        return str_result

class ComboPainterBot(PainterBot):
    def __init__(self, name: str, style, efficiency: int):
        super().__init__(name, style, efficiency)

    def paint(self, length: int, symbol_1 = "#", symbol_2 = "=") -> str:
        return f"{symbol_1*length}|{symbol_2*length}"

    def __str__(self):
        return f"\nИмя робота: {self.name};\n стиль рисования: {self.style};\n эффективность: {self.efficiency} (эффективность, целое число от 1 до 10)"

    def __repr__(self):
        return f"PainterBot('{self.name}', {self.style}, {self.efficiency})"

test_1 = PainterBot("Robot A", "Пиксельный", 2)
# print(test.name)
# print(test.paint(10))
# print(test)
# print(test.__repr__())

test_2 = LinePainterBot("Robot Б", "Пиксельный", 4)
# print(test_2.paint(3))

test_3 = WavePainterBot("Robot В", "Пиксельный", 6)
# print(test_3.paint(3))

def gallery_exhibition(painter_list, length):
    """Эта функция принимает список роботов-художников (painter_list) и длину рисунка length.
Функция должна вызвать метод paint(length) у каждого робота в списке и напечатать результат вместе с его именем."""
    for i in painter_list:
        print(f"{i.name}: {i.paint(length)}")
    return

# painter_list = [test_1, test_2] #список роботов-художников
# gallery_exhibition(painter_list, 12)

test_4 = test_1+test_2
print(test_4)
print(test_4.paint(3))
print(type(test_4))
