from itertools import pairwise

from utils import parse_input

# file_name = "test.txt"
file_name = "input.txt"


def part_1():
    lines = parse_input(file_name)
    total = 0

    for line in lines:
        x = [int(c) for c in line.split(" ")]
        print(x, sorted(x), sorted(x, reverse=True))

        if x == sorted(x) or x == sorted(x, reverse=True):
            total += 1
        else:
            continue

        for a, b in list(pairwise(line.split(" "))):
            diff = abs(int(a) - int(b))
            # print(diff)
            if diff < 1 or diff > 3:
                # print("Unsafe", a, b)
                total -= 1
                break

    print("Part 1: ", total)


def part_2():
    lines = parse_input(file_name)
    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    # part_1()
    part_2()
