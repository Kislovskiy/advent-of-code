from utils import read_input_file

inp = read_input_file("data/puzzle_04.txt")

counter_1 = 0
for line in inp:
    part_1, part_2 = line.split(",")
    start_1, end_1 = [int(x) for x in part_1.split("-")]
    start_2, end_2 = [int(x) for x in part_2.split("-")]

    if (start_1 <= start_2 and end_1 >= end_2) or (
        start_1 >= start_2 and end_1 <= end_2
    ):
        counter_1 += 1

print(f"part_1 = {counter_1}")

counter_2 = 0
for line in inp:
    part_1, part_2 = line.split(",")
    start_1, end_1 = [int(x) for x in part_1.split("-")]
    start_2, end_2 = [int(x) for x in part_2.split("-")]

    if (
        (start_1 <= start_2 and end_1 >= end_2)
        or (start_1 >= start_2 and end_1 <= end_2)
        or (start_1 <= start_2 and start_2 <= end_1)
        or (start_2 <= start_1 and start_1 <= end_2)
    ):
        counter_2 += 1

print(f"part_2 = {counter_2}")
