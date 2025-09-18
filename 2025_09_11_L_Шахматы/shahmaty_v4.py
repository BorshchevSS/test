import copy
from datetime import datetime
import random

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

    for i in range(8):
        board[6][i] = create_piece('P', 'white')

    board[0][0] = create_piece('R', 'black')
    board[0][1] = create_piece('N', 'black')
    board[0][2] = create_piece('B', 'black')
    board[0][3] = create_piece('Q', 'black')
    board[0][4] = create_piece('K', 'black')
    board[0][5] = create_piece('B', 'black')
    board[0][6] = create_piece('N', 'black')
    board[0][7] = create_piece('R', 'black')

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


# print_board(init_board())

def get_moves(piece, position, board):
    x, y = position
    moves = [] #список возможных ходов
    color = piece['color']
    # [[{}, {}, {}], [{}, {}, {}], [{},{},{}]]
    # dy dx -направления
    symbol = piece['symbol'].upper()

    if symbol == 'P':#пешка
        if color == 'white':
            direction = -1
        else:
            direction = 1
        # direction = -1 if color=='white' else 1
        start_row = 6 if color == 'white' else 1

        #ход на одну клетку
        if 0 <= y + direction < 8 and board[y+direction][x] is None:
            moves.append((x, y+direction))

            #ход на 2 первый ход
            if y == start_row and board[y+2*direction][x] is None:
                moves.append((x, y+2*direction))

        #взятие по диагонали
        for dx in [-1, 1]:
            # nx, ny - новые координаты
            nx, ny = x + dx, y + direction
            if 0 <= nx < 8 and 0 <= ny < 8:
                target = board[ny][nx]#цель, новая позиция
                if target is None or target['color'] != color:
                    moves.append((nx, ny))
    elif symbol == 'N': #конь
        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-1, -2), (1, -2), (2, -1), (-2,-1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                target = board[ny][nx]  # цель, новая позиция
                if target is None or target['color'] != color:
                    moves.append((nx, ny))
    elif symbol == 'K': #король
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    target = board[ny][nx]  # цель, новая позиция
                    if target is None or target['color'] != color:
                        moves.append((nx, ny))

    elif symbol == 'B': #слон
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        moves = linear_moves(position, board, directions)

    elif symbol == 'R':#ладья
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        moves = linear_moves(position, board, directions)

    elif symbol == 'Q': #королева (ферзь)
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1),
                      (1, 0), (-1, 0), (0, 1), (0, -1)]
        moves = linear_moves(position, board, directions)

    return moves


def linear_moves(position, board, directions):
    x, y = position
    moves = []
    color = board[y][x]['color']
    for dx, dy in directions:
        for i in range(1, 8): #i-кол-во клеток на сколько двигаемся
            nx, ny = x + dx*i, y + dy*i
            if 0 <= nx < 8 and 0 <= ny < 8:
                target = board[ny][nx]
                if target is None:
                    moves.append((nx, ny))
                elif target['color'] != color:
                    moves.append((nx, ny))
                    break
                else:
                    break
            else:
                break
    return moves

def move_piece(state, from_pos, to_pos):
    #перемещаем фигуру, обновляем доску и историю
    board = state['board']
    history = state['history']

    fx, fy = from_pos
    tx, ty = to_pos

    piece = board[fy][fx]
    target = board[ty][tx]

    #запись хода
    from_note = f'{chr(97+fx)}{8 - fy}'
    to_note = f'{chr(97+tx)}{8 - ty}'
    now = datetime.now().strftime('%H:%M:%S')
    move_str = f'({now}){piece["symbol"].upper() if piece["color"] == "white" else piece["symbol"].lower()} {from_note} --> {to_note}'

    if target:
        move_str += f' (взятие {target["symbol"]})'
    history.append(move_str)
    # перемещаем фигуры
    board[ty][tx] = piece
    board[fy][fx] = None

    #смена хода
    state['turn'] = 'black' if state['turn'] == 'white' else 'white'

    return state




def get_all_valid_moves(board, color):
    valid_moves = []

    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            if piece and piece['color'] == color:
                moves = get_moves(piece, (x, y), board)

                for move in moves:
                    copy_board = [row[:] for row in board]
                    copy_board[move[1]][move[0]]= copy_board[y][x]
                    copy_board[y][x] = None

                    if not in_check(copy_board, color):
                        valid_moves.append(((x, y), move))
    return valid_moves


def in_check(board, color):
    king_pos = None
    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            if piece and piece['symbol'].upper() == 'K' and piece['color'] == color:
                king_pos = (x, y)
                break
        if king_pos:
            break
    if king_pos is None:
        return False

    opponent_color = 'black' if color == 'white' else 'white'

    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            if piece and piece['color'] == opponent_color:
                moves = get_moves(piece, (x, y), board)
                if king_pos in moves:
                    return True
    return False


def is_checkmate(board, color):
    return in_check(board, color) and len(get_all_valid_moves(board, color)) == 0

def user_turn(state):
    while True:
        move_input = input('Введите ход (e2 e4) или help')
        if move_input == 'help':
            print_help()
            continue
        try:
            parts = move_input.split()
            if len(parts) != 2:
                print('неверный формат')
                continue
            from_str, to_str = parts

            fx = ord(from_str[0].lower()) - 97
            fy = 8 - int(from_str[1])
            tx = ord(to_str[0].lower()) - 97
            ty = 8 - int(to_str[1])

            if not(0 <= fx < 8 and 0 <= fy < 8 and 0 <= tx < 8 and 0 <= ty < 8 ):
                print('неверный ход')
                continue

            piece = state['board'][fy][fx]
            if not piece or piece['color'] != 'white':
                print('неверный или не ваш ход')
                continue

            valid_moves = get_all_valid_moves(state['board'], 'white')
            from_to_moves = [move for pos, move in valid_moves if pos == (fx, fy)]

            if (tx, ty) not in from_to_moves:
                print('неверный ход')
                #вывести доступные ходы для фигуры
                continue

            state = move_piece(state, (fx, fy), (tx, ty))
            break
        except Exception as e:
            print(f'ошибка ввода {e}')

    return state



def bot_turn(state):
    valid_moves = get_all_valid_moves(state['board'], 'black')

    if valid_moves:
        from_pos, to_pos = random.choice(valid_moves)
        state = move_piece(state, from_pos, to_pos)
        print(f'Бот сходил: {chr(97+from_pos[0])}{8-from_pos[1]}->'
              f'{chr(97+to_pos[0])}{8-to_pos[1]}')
    else:
        print('у бота нет доступных ходов')

    return state

def save_history(history):
    with open('game_history.txt', 'a', encoding='utf-8') as f:
        f.write(f"New Game ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
        for str_move in history:
            f.write(f'{str_move}\n')
        f.write('\n------------------------------')

def play():
    state = {
        'board': init_board(),
        'history': [],
        'turn': 'white'
    }
    print_help()
    while True:
        print_board(state['board'])
        #вывод истории ходов
        if state['history']:
            print('История ходов: ')
            for i, move in enumerate(state['history'][-5:], 1):
                print(f'  {i}. {move}')
            print()

        if is_checkmate(state['board'], 'white'):
            print('ШАХ и МАТ!')
            print('GAME OVER')
            save_history(state['history'])
            break

        if is_checkmate(state['board'], 'black'):
            print('ШАХ и МАТ!')
            print('YOU WIN!')
            save_history(state['history'])
            break

        if in_check(state['board'], 'black'):
            print('ШАХ черному королю')

        if in_check(state['board'], 'white'):
            print('ШАХ белому королю')

        if state['turn'] == 'white':
            state = user_turn(state)
        else:
            bot_turn(state)

if __name__ == '__main__':
    play()
# move = 'e 2'
# print(chr(97+4))