with open("data/puzzle_10.txt", "r") as fi:
    lines = fi.readlines()

X = 1
register = []
cycle = 1
for line in lines:
    instruction = line.strip().split()[0]
    if instruction == "noop":
        register.append(X)
    if instruction == "addx":
        value = int(line.strip().split()[1])
        register.append(X)
        register.append(X)
        X += value

signal_strength = []
for i in (20, 60, 100, 140, 180, 220):
    signal_strength.append(i * register[i - 1])

print(f"part_1 = {sum(signal_strength)}")
