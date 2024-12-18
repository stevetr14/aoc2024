from utils import parse_input, bfs

# file_name = "test.txt"
file_name = "input.txt"


def part_1():
    lines = parse_input(file_name)
    start = (0, 0)
    end = (70, 70)

    matrix = [["." for _ in range(71)] for _ in range(71)]

    # Check up to first 1024 bytes
    for coord in lines[:1024]:
        x, y = tuple(map(int, coord.split(",")))
        matrix[y][x] = "#"

    total = len(bfs(matrix, start, end)) - 1

    print("Part 1: ", total)


def part_2():
    lines = parse_input(file_name)
    start = (0, 0)
    end = (70, 70)

    matrix = [["." for _ in range(71)] for _ in range(71)]

    idx = 0

    can_solve = True

    while can_solve:
        for coord in lines[:idx]:
            x, y = tuple(map(int, coord.split(",")))
            matrix[y][x] = "#"

        can_solve = len(bfs(matrix, start, end)) > 0
        idx += 1

    print("Part 2: ", lines[idx - 1])


if __name__ == "__main__":
    part_1()
    part_2()
