from utils import read_input_file

current_calories = 0
elf_calories = []

for calory in read_input_file("data/puzzle_01.txt"):
    if calory:
        current_calories += int(calory)
    else:
        elf_calories.append(current_calories)
        current_calories = 0

print(f"Max Calories= {max(elf_calories)}")
print(f"TOP-3 Calories = {sum(sorted(elf_calories, reverse=True)[:3])}")
