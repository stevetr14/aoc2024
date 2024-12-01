from utils import parse_input

# file_name = "test.txt"
file_name = "input.txt"


def part_1():
    lines = parse_input(file_name)
    first, second = zip(*[line.split() for line in lines])
    first = sorted([int(c) for c in first])
    second = sorted([int(c) for c in second])

    total = 0
    for a, b in zip(first, second):
        total += abs(b - a)

    print("Part 1: ", total)


def part_2():
    lines = parse_input(file_name)
    first, second = zip(*[line.split() for line in lines])

    total = 0
    for i in first:
        total += int(i) * second.count(i)

    print("Part 2: ", total)


if __name__ == "__main__":
    part_1()
    part_2()
