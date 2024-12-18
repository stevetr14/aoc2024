from collections import deque
from pprint import pprint

from utils import parse_input

# file_name = "test.txt"
file_name = "input.txt"


def bfs(maze, start, end):
    queue = deque([(start, [start])])
    seen = {start}
    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):  # directions
            if (
                0 <= x2 < len(maze[0]) and  # X-axis in range
                0 <= y2 < len(maze) and   # y-axis
                maze[y2][x2] != '#' and  # not a wall
                (x2, y2) not in seen
            ):  # not visited
                queue.append(((x2, y2), path + [(x2, y2)]))
                seen.add((x2, y2))
    return []


def part_1():
    lines = parse_input(file_name)
    start = (0, 0)
    # end = (6, 6)
    end = (70, 70)

    # matrix = [["." for _ in range(7)] for _ in range(7)]
    matrix = [["." for _ in range(71)] for _ in range(71)]

    for coord in lines[:1024]:
        x, y = tuple(map(int, coord.split(",")))
        matrix[y][x] = "#"

    total = len(bfs(matrix, start, end)) - 1
    # print(bfs(matrix, start, end))
    # for coord in bfs(matrix, start, end):
    #     x, y = coord
    #     matrix[y][x] = "0"
    #     total += 1
    #
    # for row in matrix:
    #     print("".join(row))

    print("Part 1: ", total)


def part_2():
    lines = parse_input(file_name)
    print(lines)

    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    part_1()
    # part_2()
