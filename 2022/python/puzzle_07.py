from pathlib import Path

pwd = Path()
dirs = [Path("/")]
files = {}

with open("data/puzzle_07.txt", "r") as fi:
    for line in fi:
        if line.startswith("$ cd"):
            if line.strip().endswith(".."):
                pwd = pwd.parent
            else:
                directory = line.split()[-1]
                pwd = pwd.joinpath(directory)
            continue
        if line.startswith("$ ls"):
            continue
        if line.startswith("dir"):
            dirs.append(pwd.joinpath(line.split()[1]))
        else:
            try:
                files[pwd] += int(line.split()[0])
            except KeyError:
                files[pwd] = int(line.split()[0])


def compute_size_part1(dirname):
    size = 0
    for k, v in files.items():
        if str(k).startswith(f"{str(dirname)}"):
            size += v
    if size > 100_000:
        return 0
    else:
        return size


sizes = [compute_size_part1(dirname) for dirname in dirs]

# print(sizes)
print(f"part1 = {sum(sizes)}")


def compute_size_part2(dirname):
    size = 0
    for k, v in files.items():
        if str(k).startswith(f"{str(dirname)}"):
            size += v
    else:
        return size


total_size = 70_000_000
size_required = 30_000_000

sizes = [compute_size_part2(dirname) for dirname in dirs]
# print(sizes)
free_space = total_size - sizes[0]
# print(f"{free_space=}")
target = size_required - free_space

results = []
for x in sizes:
    diff = x - target
    if diff > 0:
        results.append(diff)
    else:
        results.append(1e10)

# print(f"{results=}")
# print(min(results))
# print(results.index(min(results)))

print(f"part2 = {sizes[results.index(min(results))]}")
