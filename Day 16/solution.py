from pprint import pprint

from utils import parse_input, find_position_in_matrix

file_name = "test.txt"
# file_name = "input.txt"


directions = [
    # Top, right, bottom, left
    (-1, 0), (0, 1), (1, 0), (0, -1)
]


def part_1():
    lines = parse_input(file_name)
    matrix = [list(line) for line in lines]
    maze = [[1 if c == "#" else 0 for c in row] for row in matrix]

    start = find_position_in_matrix(matrix, "S")
    end = find_position_in_matrix(matrix, "E")

    total = 0

    print("Part 1: ", total)


def part_2():
    lines = parse_input(file_name)
    print(lines)

    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    part_1()
    # part_2()
