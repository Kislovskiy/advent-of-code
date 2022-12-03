from string import ascii_lowercase, ascii_uppercase
from utils import read_input_file

scores = {}
for i, char in enumerate(ascii_lowercase + ascii_uppercase, start=1):
    scores[char] = i

total = 0
for line in read_input_file("data/puzzle_03.txt"):
    inp_int = [scores.get(char) for char in line]
    compartment_1 = set(inp_int[: int(len(inp_int) / 2)])
    compartment_2 = set(inp_int[int(len(inp_int) / 2):])

    total += compartment_1.intersection(compartment_2).pop()

print(f"part_1 = {total}")

total_2 = 0
counter = 0
group = []
common_elements = set()

for line in read_input_file("data/puzzle_03.txt"):
    if counter == 0:
        common_elements = set([scores.get(char) for char in line])
    if counter != 3:
        common_elements = common_elements.intersection(
            set([scores.get(char) for char in line])
        )
        counter += 1
    if counter == 3:
        total_2 += common_elements.pop()
        common_elements = {}
        counter = 0

print(f"part_2 = {total_2}")
