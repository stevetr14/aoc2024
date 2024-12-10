from collections import deque
from pprint import pprint
from itertools import groupby, chain

from utils import parse_input

file_name = "test.txt"
# file_name = "input.txt"


def is_valid_move(matrix, x, y, nx, ny):
    return 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == matrix[x][y] + 1


def bfs(matrix, start):
    queue = deque([start])
    visited = set()
    score = 0

    while queue:
        current = queue.popleft()
        x, y = current

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and is_valid_move(matrix, x, y, nx, ny):
                if matrix[nx][ny] == 9:
                    score += 1
                queue.append((nx, ny))
                visited.add((nx, ny))

    return score


def part_1():
    lines = parse_input(file_name)
    total = 0

    grid = [list(map(int, row)) for row in lines]

    print(bfs(grid, (2, 0)))

    print("Part 1: ", total)


def part_2():
    pass


if __name__ == "__main__":
    part_1()
    # part_2()
