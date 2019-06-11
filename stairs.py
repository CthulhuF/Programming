i = "#"


def inp_num_of_stairs(height):
    try:
        int(height)
        return True
    except ValueError:
        return False


while True:

    height = input("height = ")

    if inp_num_of_stairs(height) is False or int(height) < 1 or int(height) > 23:
        print("enter correct number")
        continue
    else:
        height = int(height)
        for z in range(height):
            height -= 1
            i += "#"
            print((" " * height) + i)
    break
