from collections import Counter, defaultdict
from itertools import chain, combinations
from pprint import pprint

from utils import parse_input, find_position_in_matrix, bfs

file_name = "test.txt"
# file_name = "input.txt"


def part_1():
    lines = parse_input(file_name)

    matrix = [list(line) for line in lines]
    max_x = len(matrix[0])
    max_y = len(matrix)

    walls = []

    for x in range(max_x):
        for y in range(max_y):
            if matrix[y][x] == "#" and x != 0 and y != 0 and x != max_x - 1 and y != max_y - 1:
                walls.append((x, y))

    start = find_position_in_matrix(matrix, "S")
    end = find_position_in_matrix(matrix, "E")

    # for wall in walls:
    #     wall_x, wall_y = wall
    #     matrix[wall_y][wall_x] = "."

    # pprint(matrix)
    # print(start, end)
    # total = 0
    # pprint(matrix)
    # print(walls)
    # for coord in path:
    #     matrix[coord[0]][coord[1]] = "0"

    base = bfs(matrix, start, end)
    cheats = []

    for wall in walls:
        wall_x, wall_y = wall
        matrix[wall_y][wall_x] = "."
        time_taken = bfs(matrix, start, end)
        if (time := base - time_taken) >= 100:
            cheats.append(time)
        matrix[wall_y][wall_x] = "#"

    print("Part 1: ", len(cheats))


def powerset(iterable):
    "Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def part_2():
    lines = parse_input(file_name)

    matrix = [list(line) for line in lines]
    max_x = len(matrix[0])
    max_y = len(matrix)

    walls = []

    for x in range(max_x):
        for y in range(max_y):
            if matrix[y][x] == "#" and x != 0 and y != 0 and x != max_x - 1 and y != max_y - 1:
                walls.append((x, y))

    start = find_position_in_matrix(matrix, "S")
    end = find_position_in_matrix(matrix, "E")

    base = bfs(matrix, start, end)
    cheats = defaultdict(set)

    for i in range(1, 3):
        for w in combinations(walls, len(walls) - i):
            # print(w)
            for wall in w:
                wall_x, wall_y = wall
                matrix[wall_y][wall_x] = "."

                time_taken = bfs(matrix, start, end)
                if (time := base - time_taken) >= 50:
                    cheats[i].add(time)

            for wall in w:
                wall_x, wall_y = wall
                matrix[wall_y][wall_x] = "#"

    # print(Counter(cheats))
    print(cheats)
    # print("Part 2: ", total)


if __name__ == "__main__":
    # part_1()
    part_2()
