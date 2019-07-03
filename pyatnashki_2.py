from math import fabs

n = int(input("Enter a grid size (3 or 4)"))
pole = [[] for i in range(n)]
pole_win = [[] for k in range(n)]
if n == 3:
    pole_numb = 9
    empty_value = [2, 2]
else:
    pole_numb = 16
    empty_value = [3, 3]


def init():
    active_line = 0
    for k in reversed(range(1, pole_numb)):
        pole[active_line].append(k)
        active_line += 1
        if active_line == n:
            active_line = 0
    pole[n - 1].append('_')
    active_line = 0
    for k in range(1, pole_numb):
        pole_win[active_line].append(k)
        active_line += 1
        if active_line == n:
            active_line = 0
    pole_win[n - 1].append('_')


def draw():
    if n == 3:
        print("=============")
        for i in range(n):
            print('||', end="")
            for k in range(n):
                print("", pole[k][i], "", end="")
            print("||")
        print("=============")
    else:
        print("====================")
        for i in range(n):
            print('||', end="")
            for k in range(n):
                print(" ", pole[k][i], "", end="")
            print('')
        print("====================")


def win():
    for i in range(n):
        if pole[i] == pole_win[i]:
            continue
        else:
            return 0
    print("Congratulations! You win!")
    return 1


def move(step):
    print('')
    for i in range(n):
        if step in pole[i]:
            tile_index = [i, pole[i].index(step)]
            for i in range(2):
                if fabs(tile_index[i] - empty_value[i]) > 1:
                    return print("Cannot do this turn")
            a = tile_index[0]
            b = tile_index[1]
            c = empty_value[0]
            d = empty_value[1]
            if tile_index[0] == empty_value[0] - 1 and tile_index[1] == empty_value[1]:
                pole[a][b], pole[c][d] = pole[c][d], pole[a][b]
                empty_value[0] = a
                empty_value[1] = b
                return print("You are two steps away from victory")
            elif tile_index[0] == empty_value[0] + 1 and tile_index[1] == empty_value[1]:
                pole[a][b], pole[c][d] = pole[c][d], pole[a][b]
                empty_value[0] = a
                empty_value[1] = b
                return print("You are doing great")
            elif tile_index[0] == empty_value[0] and tile_index[1] == empty_value[1] + 1:
                pole[a][b], pole[c][d] = pole[c][d], pole[a][b]
                empty_value[0] = a
                empty_value[1] = b
                return print("Can i take a couple of lessons from you")
            elif tile_index[0] == empty_value[0] and tile_index[1] == empty_value[1] - 1:
                pole[a][b], pole[c][d] = pole[c][d], pole[a][b]
                empty_value[0] = a
                empty_value[1] = b
                return print("Without comments")
            else:
                return print("This step cannot be done")
    return print("Entered non-existent cell")


init()
draw()
won = win()

while won == 0:
    step = int(input("Enter an tile for turn"))
    move(step)
    draw()
    won = win()

