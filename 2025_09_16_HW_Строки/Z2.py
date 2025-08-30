print(f"""Пользователь вводит с клавиатуры арифметическое выражение. 
Например, 23+12.Необходимо вывести на экран результат выражения. В нашем примере это 35.
Арифметическое выражение может состоять только из трёх частей: число, операция, число. 
Возможные операции: +,-,*,/""")

def inputMath():
    inputMathText = input("Введите выражение (например 23+12; допускается использовать только +;-;*;/): ")
    return inputMathText

def calculation (num1_num2_operator):
    result = 0
    if num1_num2_operator[2] == "+":
        result = num1_num2_operator[0] + num1_num2_operator[1]
    elif num1_num2_operator[2] == "-":
        result = num1_num2_operator[0] - num1_num2_operator[1]
    elif num1_num2_operator[2] == "*":
        result = num1_num2_operator[0] * num1_num2_operator[1]
    elif num1_num2_operator[2] == "/":
        result = num1_num2_operator[0] / num1_num2_operator[1]
    return result

def textInMathOperator (text):
    mathOperations = ["+", "-", "*", "/"]  # доступные математические операции
    mathOperator = ""
    for i in range(len(text)):
        for j in range(len(mathOperations)):
            #print(f"{text[i]}_{mathOperations[j]}")
            if text[i] == mathOperations[j]:
                mathOperator = mathOperations[j]
    if mathOperator == "":
        print(f"ERROR_Вы ввели '{text}', данный набор символов не содержит математических операторов '{mathOperations}'! Повторите ввод.")
        textInMathOperator(inputMath())

    # Выделяю из строки список из двух чисел
    listInputMathText = text.split(mathOperator) # строка в число
    listInputMathText = [int(listInputMathText[i].strip()) for i in range(len(listInputMathText))] # убираю лишние пробелы и превращаю их в числа

    calculation([listInputMathText[0], listInputMathText[1], mathOperator])

    return print(f"{listInputMathText[0]} {mathOperator} {listInputMathText[1]} = {calculation([listInputMathText[0], listInputMathText[1], mathOperator])}")

textInMathOperator (inputMath())