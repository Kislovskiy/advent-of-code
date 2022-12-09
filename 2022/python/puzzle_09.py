with open("data/puzzle_09.txt", "r") as fi:
    lines = fi.readlines()

maximum = max([int(x.split()[1]) for x in lines])
field_size = maximum * 100 + 1

field = [[0 for _ in range(field_size)] for _ in range(field_size)]


def move_head(x_h_0: int, y_h_0: int, direction: str) -> tuple([int, int]):
    if direction == "R":
        x_h_1 = x_h_0 + 1
        y_h_1 = y_h_0
    if direction == "L":
        x_h_1 = x_h_0 - 1
        y_h_1 = y_h_0
    if direction == "U":
        x_h_1 = x_h_0
        y_h_1 = y_h_0 + 1
    if direction == "D":
        x_h_1 = x_h_0
        y_h_1 = y_h_0 - 1
    return (x_h_1, y_h_1)


def move_tail(x_h_1, y_h_1, x_t_0, y_t_0) -> tuple([int, int]):
    # move
    if y_t_0 == y_h_1:
        y_t_1 = y_t_0
        delta_x = x_h_1 - x_t_0
        if delta_x == 2:
            x_t_1 = x_t_0 + 1
        elif delta_x == -2:
            x_t_1 = x_t_0 - 1

    if x_t_0 == x_h_1:
        x_t_1 = x_t_0
        delta_y = y_h_1 - y_t_0
        if delta_y == 2:
            y_t_1 = y_t_0 + 1
        elif delta_y == -2:
            y_t_1 = y_t_0 - 1

    # don't move
    if abs(x_h_1 - x_t_0) == 1 and abs(y_h_1 - y_t_0) == 1:
        x_t_1 = x_t_0
        y_t_1 = y_t_0
    if x_t_0 == x_h_1:
        if abs(y_t_0 - y_h_1) == 1:
            x_t_1 = x_t_0
            y_t_1 = y_t_0
    if y_t_0 == y_h_1:
        if abs(x_t_0 - x_h_1) == 1:
            x_t_1 = x_t_0
            y_t_1 = y_t_0

    # move diagonal
    # top
    if (x_h_1 - x_t_0 == 2) and (y_h_1 - y_t_0 == 1):
        x_t_1 = x_t_0 + 1
        y_t_1 = y_h_1
    if (x_h_1 - x_t_0 == -2) and (y_h_1 - y_t_0 == 1):
        x_t_1 = x_t_0 - 1
        y_t_1 = y_h_1
    if (x_h_1 - x_t_0 == 1) and (y_h_1 - y_t_0 == 2):
        x_t_1 = x_h_1
        y_t_1 = y_t_0 + 1
    if (x_h_1 - x_t_0 == -1) and (y_h_1 - y_t_0 == 2):
        x_t_1 = x_h_1
        y_t_1 = y_t_0 + 1
    # bottom
    if (x_h_1 - x_t_0 == 2) and (y_h_1 - y_t_0 == -1):
        x_t_1 = x_t_0 + 1
        y_t_1 = y_h_1
    if (x_h_1 - x_t_0 == 1) and (y_h_1 - y_t_0 == -2):
        x_t_1 = x_h_1
        y_t_1 = y_t_0 - 1
    if (x_h_1 - x_t_0 == -1) and (y_h_1 - y_t_0 == -2):
        x_t_1 = x_h_1
        y_t_1 = y_t_0 - 1
    if (x_h_1 - x_t_0 == -2) and (y_h_1 - y_t_0 == -1):
        y_t_1 = y_h_1
        x_t_1 = x_t_0 - 1

    return (x_t_1, y_t_1)


x_h_0, y_h_0 = maximum, maximum
x_t_0, y_t_0 = maximum, maximum

field[y_t_0][x_t_0] = 1
for line in lines:
    direction, step = line.split()
    step = int(step)
    for i in range(step):
        (x_h_1, y_h_1) = move_head(x_h_0, y_h_0, direction)
        (x_t_1, y_t_1) = move_tail(x_h_1, y_h_1, x_t_0, y_t_0)
        field[y_t_1][x_t_1] = 1
        (x_h_0, y_h_0) = (x_h_1, y_h_1)
        (x_t_0, y_t_0) = (x_t_1, y_t_1)


print(f"{sum([sum(x) for x in field])}")
