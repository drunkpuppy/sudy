field = [[" "] * 3 for i in range(3)]
num = 0
def instruction():
    print("Это игра крестики-нолики")
    print("формат ввода x y")
    print("x- номер строки")
    print("y номер столбца")

def show():
    print("   | 0 | 1 | 2 |")
    print(" --------------- ")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print(" --------------- ")

def ask():
    while True:
        cords = input("Ваш ход:").split()

        if len(cords) != 2:
            print("Введите 2 координаты")
            continue

        x, y = cords

        if not  (x.isdigit()) or not(y.isdigit()):
            print("Введите число")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Коодинаты не корректны")
            continue

        if field[x][y] != " ":
            print("Поле занято")
            continue

        return x, y

def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)),((1, 0), (1, 1), (1, 2)),((2, 0),(2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2))]
    for cord in win_cord:
        a = cord[0]
        b = cord[1]
        c = cord[2]

        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != " ":
            print(f"Победа за {field[a[0]][a[1]]}")
            return True
    return False

instruction()

while True:
    num += 1

    show()

    if num % 2 == 1:
        print("Ходит крестик ")
    else:
        print("Ходит нолик ")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print("Ничья")
        break


