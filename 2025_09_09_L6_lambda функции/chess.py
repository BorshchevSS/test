def print_help():
    print("\n=== Шпаргалка по фигурам и их ходам ===")
    print("P (Пешка):     Ход вперёд на 1 (первый ход допустимо 2 клетки), бьёт по диагонали")
    print("R (Ладья):     По вертикали и горизонтали")
    print("N (Конь):      Ход \"буквой Г\" (2+1)")
    print("B (Слон):      По диагонали")
    print("Q (Ферзь):     Слон + Ладья (все направления)")
    print("K (Король):    На 1 клетку в любом направлении")
    print("Пример хода:   e2 e4")
    print("Введите 'help' чтобы снова увидеть это меню\n")

#Клетка - элемент массива
#https://ru.wikipedia.org/wiki/%D0%A8%D0%B0%D1%85%D0%BC%D0%B0%D1%82%D0%BD%D1%8B%D0%B5_%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8B_%D0%B2_%D0%AE%D0%BD%D0%B8%D0%BA%D0%BE%D0%B4%D0%B5

#Создаёт и возвращает начальное расположение фигур.
def init_bord():
    pass

#Отображает доску в ASCII-графике.
def print_bord(bord):
    pass

#Возвращает все возможные ходы для фигуры на указанной позиции.
def get_moves(piece, position, board):
    pass

#Универсальная функция для расчёта ходов по линиям (используется для ладьи, слона и ферзя).
def linear_moves(position, board, derection):
    pass

#Перемещает фигуру, обновляет доску и историю.
def move_piece(state, from_pos, to_pos):
    pass

#Возвращает все допустимые ходы для цвета, исключая те, что оставляют короля под шахом.
def get_all_valid_moves(board, color):
    pass

#Проверяет, находится ли король указанного цвета под атакой.
def in_check(board, color):
    pass

#Проверяет, является ли ситуация матом.
def is_checkmate(board, color):
    pass

#Обрабатывает ввод игрока (e2 e4), проверяет корректность и возвращает обновлённое состояние.
def user_turn(state):
    pass

#Делает случайный допустимый ход за бота.
def bot_turn(state):
    pass

#Сохраняет ходы в файл game_history.txt, добавляя пометку "New Game".
def save_history(history):
    pass

#Запускает игру: чередует ходы пользователя и бота, печатает доску и историю, проверяет шах/мат, завершает игру.
def play():
    print_help()
    while True:
        print_bord() #Печатаем достку
        #вывод истории ходов
        if is_checkmate(board, "white"):
            print("Шах и мат!")
            print("Game over")
            save_history(history)
            break
        if is_checkmate(board, "black"):
            print("Шах и мат!")
            print("Game over")
            save_history(history)
            break

        if in_check(board, "white"):
            print("Шах белому королю")

        if in_check(board, "black"):
            print("Шах черному королю")