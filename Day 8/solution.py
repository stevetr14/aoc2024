from collections import defaultdict
from itertools import combinations

from utils import parse_input


# file_name = "test.txt"
file_name = "input.txt"


def get_x_y_negative_diff(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int]:
    return tuple(i - j for i, j in zip(first, second))


def get_x_y_positive_diff(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int]:
    return tuple(i + j for i, j in zip(first, second))


def part_one():
    lines = parse_input(file_name)

    max_y_coord = len(lines) - 1
    max_x_coord = len(lines[0]) - 1

    mappings = defaultdict(list)

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != ".":
                mappings[c].append((x, y))

    antinodes = set()

    for k, v in mappings.items():
        pairs = list(combinations(v, 2))

        for a, b in pairs:
            diff = get_x_y_negative_diff(a, b)
            first_antinode = get_x_y_positive_diff(a, diff)
            second_antinode = get_x_y_negative_diff(b, diff)

            if 0 <= first_antinode[0] <= max_x_coord and 0 <= first_antinode[1] <= max_y_coord:
                antinodes.add(first_antinode)

            if 0 <= second_antinode[0] <= max_x_coord and 0 <= second_antinode[1] <= max_y_coord:
                antinodes.add(second_antinode)

    print("Part 1: ", len(antinodes))


def part_two():
    lines = parse_input(file_name)

    max_y_coord = len(lines) - 1
    max_x_coord = len(lines[0]) - 1

    mappings = defaultdict(list)

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != ".":
                mappings[c].append((x, y))

    antinodes = set()

    for k, v in mappings.items():
        # Include the antennas as well as antinodes can appear on top of them now.
        antinodes = antinodes.union(set(v))
        pairs = list(combinations(v, 2))

        for a, b in pairs:
            diff = get_x_y_negative_diff(a, b)
            first_antinode = get_x_y_positive_diff(a, diff)
            second_antinode = get_x_y_negative_diff(b, diff)

            # Get all antinodes within boundary above the pair
            while 0 <= first_antinode[0] <= max_x_coord and 0 <= first_antinode[1] <= max_y_coord:
                antinodes.add(first_antinode)
                first_antinode = get_x_y_positive_diff(first_antinode, diff)

            # Get all antinodes within boundary below the pair
            while 0 <= second_antinode[0] <= max_x_coord and 0 <= second_antinode[1] <= max_y_coord:
                antinodes.add(second_antinode)
                second_antinode = get_x_y_negative_diff(second_antinode, diff)

    print("Part 2: ", len(antinodes))


if __name__ == "__main__":
    # part_one()
    part_two()
