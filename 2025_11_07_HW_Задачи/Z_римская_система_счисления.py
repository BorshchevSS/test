"""1. Основные символы и их значения: dict (словарь)
◦ I = 1
◦ V = 5
◦ X = 10
◦ L = 50
◦ C = 100
◦ D = 500
◦ M = 1000
2. Если меньшая цифра стоит перед большей, она вычитается
(правило вычитания):
◦ IV = 4 (5 - 1)
◦ IX = 9 (10 - 1)
◦ XL = 40 (50 - 10)
◦ XC = 90 (100 - 10)
◦ CD = 400 (500 - 100)
◦ CM = 900 (1000 - 100)
3. Если большая цифра стоит перед меньшей или равной, они
складываются:
◦ VI = 6 (5 + 1)
◦ XI = 11 (10 + 1)
◦ XX = 20 (10 + 10)
4. Вычитаться могут только степени десятки (I, X, C) и только от"""

def conversion_roman_in_decimal_numeral_system (roman_num: str):
    dict_symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    dict_symbols_conversion = []
    for i in roman_num:
        for j in dict_symbols:
            if i == j:
                dict_symbols_conversion.append(dict_symbols[j])

    decimal_num = 0
    new_step = False
    for k in range((len(dict_symbols_conversion)-1), -1, -1):
        #Лунная походка :)
        if new_step:
            new_step = False
            continue  # Переходим к следующей итерации
        if k == 0:
            #Прибавляем последнее число (первое число в массиве) и останавливаем цикл
            decimal_num = decimal_num + dict_symbols_conversion[k]
            #print(f"{decimal_num}____{k}")
            break
        else:
            #print(f"{dict_symbols_conversion[k-1]}_{dict_symbols_conversion[k]}")
            if dict_symbols_conversion[k] > dict_symbols_conversion[k-1]:
                #Если текущее число больше предыдущего, то вычитай его и пропускай 1 шаг (лунной походки)
                decimal_num += dict_symbols_conversion[k] - dict_symbols_conversion[k-1]
                #print(f"{decimal_num}___{k}")
                new_step = True
            else:
                decimal_num = decimal_num + dict_symbols_conversion[k]
                #print(f"{decimal_num}__{k}")

        # print(decimal_num)
    #print(dict_symbols_conversion)
    #print(decimal_num)
    return decimal_num

num1 = "MCMLXXXIV"
print(f"{num1} = {conversion_roman_in_decimal_numeral_system(num1)}")

num2 = "MCCXXXIV"
print(f"{num2} = {conversion_roman_in_decimal_numeral_system(num2)}")

num3 = "MCMXC"
print(f"{num3} = {conversion_roman_in_decimal_numeral_system(num3)}")

num4 = "I"
print(f"{num4} = {conversion_roman_in_decimal_numeral_system(num4)}")

num5 = "IV"
print(f"{num5} = {conversion_roman_in_decimal_numeral_system(num5)}")

num6 = "VIII"
print(f"{num6} = {conversion_roman_in_decimal_numeral_system(num6)}")
