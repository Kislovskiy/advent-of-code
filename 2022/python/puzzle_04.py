counter_1 = 0
counter_2 = 0

with open("data/puzzle_04.txt", "r") as fi:
    for line in fi:
        [start_1, end_1, start_2, end_2] = [
            int(element) for element in line.replace("-", ",").split(",")
        ]

        if (start_1 <= start_2 and end_1 >= end_2) or (
            start_1 >= start_2 and end_1 <= end_2
        ):
            counter_1 += 1
        if (start_1 <= start_2 and start_2 <= end_1) or (
            start_2 <= start_1 and start_1 <= end_2
        ):
            counter_2 += 1


print(f"part_1 = {counter_1}")
print(f"part_2 = {counter_2}")
