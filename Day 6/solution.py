from pprint import pprint

from utils import parse_input

file_name = "test.txt"
# file_name = "input.txt"


def part_1():
    lines = [list(row) for row in parse_input(file_name)]
    total = 0

    pprint(lines)

    start = (0, 0)  # y, x

    max_y = len(lines)
    max_x = len(lines[0])

    for y in range(max_y):
        found = False
        for x in range(max_x):
            if lines[y][x] == "^":
                start = (y, x)
                lines[y][x] = "."
                found = True
                break

        if found:
            break

    curr_dir = "^"

    is_end = False

    while not is_end:
        y, x = start
        # is_end = (y == 0 or y == max_y or x == 0 or x == max_x) and lines[y][x] == "."
        # Up
        if curr_dir == "^":
            for j in range(1, y + 1):
                if (pos := lines[y - j][x]) != "#":
                    print(pos)
                else:
                    is_end = (j == 0 or j == max_y) and lines[j][x] == "."
                    start = (y - j + 1, x)
                    curr_dir = ">"
                    break

        y, x = start
        # Right
        if curr_dir == ">":
            for i in range(1, max_x - x):
                if (pos := lines[y][x + i]) != "#":
                    print(pos)
                else:
                    is_end = (i == 0 or i == max_x) and lines[y][i] == "."
                    start = (y, x + i - 1)
                    curr_dir = "v"
                    break

        y, x = start
        # Down
        if curr_dir == "v":
            for j in range(1, max_y - y):
                if (pos := lines[y + j][x]) != "#":
                    print(pos)
                else:
                    is_end = (j == 0 or j == max_y) and lines[j][x] == "."
                    start = (y + j - 1, x)
                    curr_dir = "<"

        y, x = start
        # Left
        if curr_dir == "<":
            for i in range(1, x + 1):
                if (pos := lines[y][x - i]) != "#":
                    print(pos)
                else:
                    is_end = (i == 0 or i == max_x) and lines[y][i] == "."
                    start = (y, x - i + 1)
                    curr_dir = "^"
                    break

    print("Part 1: ", total)


def part_2():
    lines = parse_input(file_name)
    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    part_1()
    # part_2()
