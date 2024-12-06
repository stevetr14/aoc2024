from utils import parse_input

# file_name = "test.txt"
file_name = "input.txt"


def part_1():
    lines = parse_input(file_name)
    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1
    total = 0

    def count_xmas(y_: int, x_: int) -> int:
        count = 0
        # Left
        if x_ - 3 >= 0 and lines[y_][x_ - 1] + lines[y_][x_ - 2] + lines[y_][x_ - 3] == "MAS":
            count += 1

        # Right
        if x_ + 3 <= max_x and lines[y_][x_ + 1] + lines[y_][x_ + 2] + lines[y_][x_ + 3] == "MAS":
            count += 1

        # Up
        if y_ - 3 >= 0 and lines[y_ - 1][x_] + lines[y_ - 2][x_] + lines[y_ - 3][x_] == "MAS":
            count += 1

        # Down
        if y_ + 3 <= max_y and lines[y_ + 1][x_] + lines[y_ + 2][x_] + lines[y_ + 3][x_] == "MAS":
            count += 1

        # Diagonal bottom left
        if (
            x_ - 3 >= 0
            and y_ + 3 <= max_y
            and lines[y_ + 1][x_ - 1] + lines[y_ + 2][x_ - 2] + lines[y_ + 3][x_ - 3] == "MAS"
        ):
            count += 1

        # Diagonal bottom right
        if (
            x_ + 3 <= max_x
            and y_ + 3 <= max_y
            and lines[y_ + 1][x_ + 1] + lines[y_ + 2][x_ + 2] + lines[y_ + 3][x_ + 3] == "MAS"
        ):
            count += 1

        # Diagonal top left
        if (
            y_ - 3 >= 0
            and x_ - 3 >= 0
            and lines[y_ - 1][x_ - 1] + lines[y_ - 2][x_ - 2] + lines[y_ - 3][x_ - 3] == "MAS"
        ):
            count += 1

        # Diagonal top right
        if (
            x_ + 3 <= max_x
            and y_ - 3 >= 0
            and lines[y_ - 1][x_ + 1] + lines[y_ - 2][x_ + 2] + lines[y_ - 3][x_ + 3] == "MAS"
        ):
            count += 1

        return count

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if lines[y][x] == "X":
                total += count_xmas(y, x)

    print("Part 1: ", total)


def part_2():
    lines = parse_input(file_name)
    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1
    total = 0
    patterns = ["SAM", "MAS"]

    def count_xmas(y_: int, x_: int) -> int:
        if not (0 <= x_ - 1 and x + 1 <= max_x) or not (0 <= y_ - 1 and y + 1 <= max_y):
            return 0

        left_mas = lines[y_ - 1][x_ - 1] + lines[y_][x_] + lines[y_ + 1][x_ + 1]
        right_mas = lines[y_ - 1][x_ + 1] + lines[y_][x_] + lines[y_ + 1][x_ - 1]

        # Diagonal from left - MAS
        if (
            (left_mas in patterns and right_mas in patterns)
            or (right_mas in patterns and left_mas in patterns)
        ):
            return 1

        return 0

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if lines[y][x] == "A":
                total += count_xmas(y, x)

    print("Part 2: ", total)


if __name__ == "__main__":
    part_1()
    part_2()
