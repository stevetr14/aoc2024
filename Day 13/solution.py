import re

# from sympy import Eq, solve, symbols

from utils import parse_input

# file_name = "test.txt"
file_name = "input.txt"


def solve_multiple_variables(offset: int = 0) -> int:
    machines = parse_input(file_name, "\n\n")
    total = 0

    for machine in machines:
        x_values = list(map(int, re.findall(r"X\+([0-9]+)", machine)))
        y_values = list(map(int, re.findall(r"Y\+([0-9]+)", machine)))
        x_target = int(re.findall(r"X=([0-9]+)", machine)[0]) + offset
        y_target = int(re.findall(r"Y=([0-9]+)", machine)[0]) + offset

        x1, x2 = x_values
        y1, y2 = y_values

        # Represent b in terms of a after scaling up a's on both equations.
        b = (x1 * y_target - y1 * x_target) / (x1 * y2 - y1 * x2)
        a = (x_target - x2 * b) / x1

        # Only whole numbers are valid
        if a == int(a) and b == int(b):
            total += int(a) * 3 + int(b)

    return total


# def solve_multiple_variables(offset: int = 0) -> int:
#     machines = parse_input(file_name, "\n\n")
#     total = 0
#
#     for machine in machines:
#         x_values = list(map(int, re.findall(r"X\+([0-9]+)", machine)))
#         y_values = list(map(int, re.findall(r"Y\+([0-9]+)", machine)))
#         x_target = int(re.findall(r"X=([0-9]+)", machine)[0]) + offset
#         y_target = int(re.findall(r"Y=([0-9]+)", machine)[0]) + offset
#
#         a, b = symbols("a b")
#         eq1 = Eq(x_values[0] * a + x_values[1] * b, x_target)
#         eq2 = Eq(y_values[0] * a + y_values[1] * b, y_target)
#
#         solved_a, solved_b = solve((eq1, eq2), (a, b)).values()
#
#         if solved_a.is_integer and solved_b.is_integer:
#             total += solved_a * 3 + solved_b
#
#     return total


def part_1():
    print("Part 1: ", solve_multiple_variables())


def part_2():
    print("Part 2: ", solve_multiple_variables(10_000_000_000_000))


if __name__ == "__main__":
    part_1()
    part_2()
