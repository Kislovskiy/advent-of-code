from copy import deepcopy

stack_9000 = {
    1: ["F", "C", "J", "P", "H", "T", "W"],
    2: ["G", "R", "V", "F", "Z", "J", "B", "H"],
    3: ["H", "P", "T", "R"],
    4: ["Z", "S", "N", "P", "H", "T"],
    5: ["N", "V", "F", "Z", "H", "J", "C", "D"],
    6: ["P", "M", "G", "F", "W", "D", "Z"],
    7: ["M", "V", "Z", "W", "S", "J", "D", "P"],
    8: ["N", "D", "S"],
    9: ["D", "Z", "S", "F", "M"],
}

stack_9001 = deepcopy(stack_9000)

with open("data/puzzle_05.txt", "r") as fi:
    for line in fi:
        if line.startswith("move"):
            [crates, location_from, location_to] = [
                int(element) for element in line.split() if element.isdigit()
            ]
            for i in range(crates):
                stack_9000[location_to] += [stack_9000[location_from].pop()]
            stack_9001[location_to] += stack_9001[location_from][-crates:]
            stack_9001[location_from] = stack_9001[location_from][:-crates]

print("part_1 = ", "".join([stack_9000[key].pop() for key in stack_9000.keys()]))
print("part_2 = ", "".join([stack_9001[key].pop() for key in stack_9001.keys()]))
