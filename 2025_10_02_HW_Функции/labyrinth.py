# Генерация начального поля и начальной координаты (для этой задачи можно сделать отдельную функцию)
maze = [
["#", "#", "#", "#", "#", "#", "#"],
["#", " ", " ", " ", " ", " ", "#"],
["#", " ", "#", "#", "#", " ", "#"],
["#", " ", "#", "E", " ", " ", "#"],
["#", " ", "#", "#", "#", " ", "#"],
["#", " ", " ", " ", "#", " ", "#"],
["#", "#", "0", "#", "#", "#", "#"]
]

maze_xy = [
["06", "16", "26", "36", "46", "56", "66"],
["05", "15", "25", "35", "45", "55", "65"],
["04", "14", "24", "34", "44", "54", "64"],
["03", "13", "23", "33", "43", "53", "63"],
["02", "12", "22", "32", "42", "52", "62"],
["01", "11", "21", "31", "41", "51", "61"],
["00", "10", "20", "30", "40", "50", "60"]
]
exitMaze = "0"
player = "E"
blank = " "
step = "-"

# Печать поля
def print_maze(maze):
    for i in range(len(maze)):
        strL = " ".join(maze[i])
        print(strL)


# Функция используется один раз (в начале) что бы поместить игрока на поле
def find_exit(maze, x, y):
    maze[6-y][x] = player
    return maze


#Определяю координату игрока в лабиринте
def searchPlayer(maze):
    x = None
    y = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            #print(f"i={i}_j={j}")
            if maze[i][j] == player:
                x = j
                y = 6 - i
                break
        if x != None:
            break
    return x, y

# список доступных ходов
def listAvailableStep(maze):
    x, y = searchPlayer(maze)
    list_permissible_steps = []  # Массив допустимых ходов
    #print(f"{x}_{y}")
    for i in range(x-1, x+2):
        if maze[6 - y][i] == blank or maze[6 - y][i] == exitMaze:
            list_permissible_steps.append((i, y))
    for j in range(y - 1, y + 2):
        if maze[6-j][x] == blank or maze[6-j][x] == exitMaze:
            list_permissible_steps.append((x, j))

            #print(f"i={i}_j={j}_{maze[6-j][i]}")
    #print(list_permissible_steps)
    return list_permissible_steps


def inputStepXY(maze):
    x_old, y_old = searchPlayer(maze) #Определяю координату игрока в лабиринте
    x_new, y_new = None, None

    #Ввод новой координаты
    while True:
        try:
            x_new = int(input("Введи координату 'x' новой точки: "))
            y_new = int(input("Введи координату 'y' новой точки: "))
            flag = False
            for (i, j) in listAvailableStep(maze):
                if (i, j) == (x_new, y_new):
                    flag = True
                    break
            if flag:
                break
            else:
                print(f"Введённая координата ({x_new}, {y_new}) не доступна, cписок доступных координат: {listAvailableStep(maze)}")
        except:
            print("Введите число!")

    #maze[6 - y_new][x_new] = player
    #print_maze(maze)
    return x_old, y_old, x_new, y_new

#print(inputStepXY(maze))
#inputStepXY(maze)


def labirintGame():
    flag_game_ower = False
    maze_game = maze
    while True:
        #Печатаю поле
        print("Перед Вами поле с координатами (первая цифра, координата x; вторая цифра, координата y: ")
        print_maze(maze_xy)
        print(f"\nПеред Вами игровое поле (Игрок: {player}; Выход: {exitMaze})")
        print_maze(maze_game)
        #Запрашиваю координаты для шага
        x_old, y_old, x_new, y_new = inputStepXY(maze_game)
        if maze_game[6 - y_new][x_new] == exitMaze:
            print(f"Поздравляю, Вы победили!")
            break
        else:
            maze_game[6 - y_old][x_old] = step
            maze_game[6 - y_new][x_new] = player

        #Если список доступных ходов пуст, то вы проиграли
        if listAvailableStep(maze_game) == []:
            print_maze(maze_game)
            print("Вы проиграли!")
            break

labirintGame ()