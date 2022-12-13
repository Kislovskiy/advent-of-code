from functools import cmp_to_key


def compare(left, right):
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            for items in zip(left, right):
                out = compare(*items)
                if out:
                    return out
            return compare(len(left), len(right))
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])


result = 0
with open("data/puzzle_13.txt", "r") as fi:
    for i, pair in enumerate(fi.read().split("\n\n"), 1):
        left, right = pair.splitlines()
        left = eval(left)
        right = eval(right)
        if compare(left, right) < 0:
            result += i

print(f"part_1 = {result}")


def distress_signal(data):
    distress = [[[2]], [[6]]]
    data.extend(distress)
    sorted_list = sorted(data, key=cmp_to_key(compare))
    return [i for i, item in enumerate(sorted_list, 1) if item in distress]


with open("data/puzzle_13.txt", "r") as fi:
    data = [eval(x.strip()) for x in fi.readlines() if x != "\n"]
    a, b = distress_signal(data)
    print(f"{a=} * {b=} = {a * b}")
