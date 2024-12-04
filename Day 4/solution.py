from utils import parse_input

file_name = "test.txt"
# file_name = "input.txt"


def part_1():
    lines = parse_input(file_name)
    total = 0

    for x in range(len(lines[0])):
        for y in range(len(lines)):
            print(lines[y][x])

    print("Part 1: ", total)


def part_2():
    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    part_1()
    # part_2()
