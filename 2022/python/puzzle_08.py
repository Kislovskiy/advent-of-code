visible = 0

with open("data/puzzle_08.txt", "r") as fi:
    field = [[int(tree) for tree in x.strip()] for x in fi.readlines()]
    visible = [
        [False for col in range(len(field[0]))] for _ in range(len(field))
        ]

    # count boundaries
    # visible += 2 * len(field) + 2 * (len(field[0]) - 2)
    visible[-1] = [True for _ in range(len(visible[-1]))]
    visible[0] = [True for _ in range(len(visible[0]))]
    for row in range(len(visible)):
        visible[row][0] = True
        visible[row][-1] = True

    # left -> right
    for row_idx in range(1, len(field) - 1):
        maximum = field[row_idx][0]
        for col_idx in range(1, len(field[0]) - 1):
            if (
                field[row_idx][col_idx] > maximum
            ):
                visible[row_idx][col_idx] = True
                maximum = field[row_idx][col_idx]

    # top -> bottom
    for col_idx in range(1, len(field[0]) - 1):
        maximum = field[0][col_idx]
        for row_idx in range(1, len(field) - 1):
            if (
                field[row_idx][col_idx] > maximum
            ):
                visible[row_idx][col_idx] = True
                maximum = field[row_idx][col_idx]

    # bottom -> top
    for col_idx in range(1, len(field[0]) - 1):
        maximum = field[-1][col_idx]
        for row_idx in reversed(range(1, len(field) - 1)):
            if (
                field[row_idx][col_idx] > maximum
            ):
                visible[row_idx][col_idx] = True
                maximum = field[row_idx][col_idx]
    # right -> left
    for row_idx in range(1, len(field) - 1):
        maximum = field[row_idx][-1]
        for col_idx in reversed(range(1, len(field[0]) - 1)):
            if (
                field[row_idx][col_idx] > maximum
            ):
                visible[row_idx][col_idx] = True
                maximum = field[row_idx][col_idx]

print(f"part_1 = {sum([sum(row) for row in visible])}")

score = [
        [0 for col in range(len(field[0]))] for _ in range(len(field))
        ]

for row_idx in range(len(field) - 1):
    for col_idx in range(len(field[0])):
        right = 0
        for j in range(col_idx + 1, len(field[0])):
            if field[row_idx][j] < field[row_idx][col_idx]:
                right += 1
            else:
                right += 1
                break

        bottom = 0
        for i in range(row_idx + 1, len(field)):
            if field[i][col_idx] < field[row_idx][col_idx]:
                bottom += 1
            else:
                bottom += 1
                break

        top = 0
        for i in reversed(range(row_idx)):
            if field[i][col_idx] < field[row_idx][col_idx]:
                top += 1
            else:
                top += 1
                break

        left = 0
        for j in reversed(range(col_idx)):
            if field[row_idx][j] < field[row_idx][col_idx]:
                left += 1
            else:
                left += 1
                break

        score[row_idx][col_idx] = right * bottom * left * top

print(f"part_2 = {max([max(x) for x in score])}")
