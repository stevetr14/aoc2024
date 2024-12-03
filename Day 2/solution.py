from itertools import pairwise, combinations

from utils import parse_input

# file_name = "test.txt"
file_name = "input.txt"


def part_1():
    lines = parse_input(file_name)
    total = 0

    for line in lines:
        x = [int(c) for c in line.split(" ")]

        if x == sorted(x) or x == sorted(x, reverse=True):
            total += 1
        else:
            continue

        for a, b in list(pairwise(line.split(" "))):
            diff = abs(int(a) - int(b))
            if diff < 1 or diff > 3:
                total -= 1
                break

    print("Part 1: ", total)


def part_2():
    lines = parse_input(file_name)
    total = 0

    def is_safe(levels: list[int]) -> bool:
        j = [a - b for a, b in pairwise(levels)]
        k = [True if 1 <= abs(i) <= 3 else False for i in j]

        # Not in descending or ascending order - invalid
        # There is a difference less than 1 or greater than 3 - invalid
        if not (levels == sorted(levels) or levels == sorted(levels, reverse=True)) or not all(k):
            return False

        return True

    for line in lines:
        x = [int(c) for c in line.split(" ")]

        if not is_safe(x):
            for combo in combinations(x, len(x) - 1):
                if is_safe(list(combo)):
                    total += 1
                    break
        else:
            total += 1

    print("Part 2: ", total)


if __name__ == "__main__":
    part_1()
    part_2()
