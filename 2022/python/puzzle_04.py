fully_contained = 0
overlap = 0

with open("data/puzzle_04.txt", "r") as fi:
    for line in fi:
        [start_1, end_1, start_2, end_2] = [
            int(element) for element in line.replace("-", ",").split(",")
        ]

        if (start_2 <= start_1 <= end_1 <= end_2) or (
            start_1 <= start_2 <= end_2 <= end_1
        ):
            fully_contained += 1

        if (start_1 <= start_2 <= end_1) or (start_2 <= start_1 <= end_2):
            overlap += 1


print(f"part_1 = {fully_contained}")
print(f"part_2 = {overlap}")
