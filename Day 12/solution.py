from collections import defaultdict, Counter

from utils import parse_input

file_name = "test.txt"
# file_name = "input.txt"


checking_directions = [
    # Top, right, bottom, left
    (-1, 0), (0, 1), (1, 0), (0, -1)
]


def count_edges(grid: list[list[str]], curr_pos: tuple[int, int], max_y: int, max_x: int) -> int:
    y, x = curr_pos
    curr_char = grid[y][x]
    count = 0

    for direction in checking_directions:
        new_y, new_x = tuple(map(lambda a, b: a + b, curr_pos, direction))

        # Top and bottom edge
        if new_y < 0 or new_y >= max_y or new_x < 0 or new_x >= max_x:
            count += 1
        elif grid[new_y][new_x] != curr_char:
            count += 1

    return count


def part_1():
    lines = [list(row) for row in parse_input(file_name)]

    perimeters = defaultdict(int)
    areas = defaultdict(int)

    max_y = len(lines)
    max_x = len(lines[0])

    for i in range(max_y):
        for k, v in Counter(lines[i]).items():
            areas[k] += v
        for j in range(max_x):
            perimeters[lines[i][j]] += count_edges(lines, (i, j), max_y, max_x)

    result = {key: areas[key] * perimeters[key] for key in areas if key in perimeters}

    print(areas, perimeters, result)
    print("Part 1: ", sum(result.values()))


def part_2():
    lines = parse_input(file_name)
    print(lines)

    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    part_1()
    # part_2()
