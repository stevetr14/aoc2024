from functools import cache

from utils import parse_input


# file_name = "test.txt"
file_name = "input.txt"

sections = parse_input(file_name, "\n\n")

patterns = sorted(sections[0].split(", "), key=len, reverse=True)
designs = sections[1].strip().split("\n")


@cache
def match(design):
    if not design:
        return 1

    return sum(match(design.removeprefix(p)) for p in patterns if design.startswith(p))


def part_one():
    total = 0

    for d in designs:
        total += 1 if match(d) != 0 else 0

    print("Part 1: ", total)


def part_two():
    total = 0

    for d in designs:
        total += match(d)

    print("Part 2: ", total)


if __name__ == "__main__":
    # part_one()
    part_two()
