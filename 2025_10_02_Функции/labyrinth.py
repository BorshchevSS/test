# Генерация начального поля и начальной координаты (для этой задачи можно сделать отдельную функцию)
maze = [
["#", "#", "#", "#", "#", "#", "#"],
["#", " ", " ", " ", " ", " ", "#"],
["#", " ", "#", "#", "#", " ", "#"],
["#", " ", "#", " ", " ", " ", "#"],
["#", " ", "#", "#", "#", " ", "#"],
["#", " ", " ", " ", "#", "E", "#"],
["#", "#", "0", "#", "#", "#", "#"]
]
exitMaze = "0"
player = "E"

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
    for i in range():


    pass
listAvailableStep(maze)

def inputStepXY(maze):
    x_old, y_old = searchPlayer(maze) #Определяю координату игрока в лабиринте

    #Ввод новой координаты
    while True:
        try:
            x_new = int(input("Введи координату 'x' новой точки: "))
            y_new = int(input("Введи координату 'y' новой точки: "))
            break
        except:
            print("Введите число!")

    maze[6 - y_new][x_new] = player
    print_maze(maze)
    return maze

#inputStepXY(maze)


# def labirintGame():
#
#     labirint = find_exit(maze_2, 3, 3)
#     print_maze(labirint)
#     #print(labirint)
#
# labirintGame ()