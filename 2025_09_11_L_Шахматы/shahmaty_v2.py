

# print(init_board())
#
# print("""Король: ♔ (белый), ♚ (чёрный)
# Ферзь: ♕ (белый), ♛ (чёрный)
# Ладья: ♖ (белый), ♜ (чёрный)
# Слон: ♗ (белый), ♝ (чёрный)
# Конь: ♘ (белый), ♞ (чёрный)
# Пешка: ♙ (белый), ♟ (чёрный)""")




def print_help():
    print("\n=== Шпаргалка по фигурам и их ходам ===")
    print("P (Пешка):     Ход вперёд на 1, бьёт по диагонали")
    print("R (Ладья):     По вертикали и горизонтали")
    print("N (Конь):      Ход \"буквой Г\" (2+1)")
    print("B (Слон):      По диагонали")
    print("Q (Ферзь):     Слон + Ладья (все направления)")
    print("K (Король):    На 1 клетку в любом направлении")
    print("Пример хода:   e2 e4")
    print("Введите 'help' чтобы снова увидеть это меню\n")


def create_piece(symbol, color):
    return {'symbol': symbol, 'color': color}

def init_board():

    board = [[None for _ in range(8)] for _ in range(8)]


    for i in range(8):
        board[1][i] = create_piece('P', 'black')

    board[0][0] = create_piece('R', 'black')
    board[0][1] = create_piece('N', 'black')
    board[0][2] = create_piece('B', 'black')
    board[0][3] = create_piece('Q', 'black')
    board[0][4] = create_piece('K', 'black')
    board[0][5] = create_piece('B', 'black')
    board[0][6] = create_piece('N', 'black')
    board[0][7] = create_piece('R', 'black')


    for i in range(8):
        board[6][i] = create_piece('P', 'white')

    board[7][0] = create_piece('R', 'white')
    board[7][1] = create_piece('N', 'white')
    board[7][2] = create_piece('B', 'white')
    board[7][3] = create_piece('Q', 'white')
    board[7][4] = create_piece('K', 'white')
    board[7][5] = create_piece('B', 'white')
    board[7][6] = create_piece('N', 'white')
    board[7][7] = create_piece('R', 'white')

    return board


def print_board(board):
    print("    a   b   c   d   e   f   g   h")
    print("  +---+---+---+---+---+---+---+---+")

    for y in range(8):
        row = f'{8 - y} |'
        for x in range(8):
            piece = board[y][x]
            if piece:
                symbol = piece['symbol']
                if piece['color'] == 'white':
                    symbol = symbol.upper()
                else:
                    symbol = symbol.lower()
                row += f' {symbol} |'
            else:
                row += '   |'
        print(row + f' {8 - y}')
        print("  +---+---+---+---+---+---+---+---+")

    print("    a   b   c   d   e   f   g   h\n")


print_board(init_board())

def get_moves(piece, position, board):
    pass

def linear_moves(position, board, directions):
    pass

def move_piece(state, from_pos, to_pos):
    pass

def get_all_valid_moves(board, color):
    pass

def in_check(board, color):
    pass

def is_checkmate(board, color):
    pass

def user_turn(state):
    pass

def bot_turn(state):
    pass

def save_history(history):
    pass

def play():
    state = {
        'board': [],
        'history': [],
        'turn': 'white'
    }
    print_help()
    while True:
        print_board()
        #вывод истории ходов
        if is_checkmate(board, 'white'):
            print('ШАХ и МАТ!')
            print('GAME OVER')
            save_history(history)
            break

        if is_checkmate(board, 'black'):
            print('ШАХ и МАТ!')
            print('YOU WIN!')
            save_history(history)
            break

        if in_check(board, 'black'):
            print('ШАХ черному королю')

        if in_check(board, 'white'):
            print('ШАХ белому королю')

        if move % 2 == 0:
            bot_turn(state)
        else:
            user_turn(state)
        move += 1