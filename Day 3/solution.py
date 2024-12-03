import re

# file_name = "test.txt"
file_name = "input.txt"


def process_mul_expression(text):
    total = 0
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, text)

    for a, b in matches:
        total += int(a) * int(b)

    return total


def part_1():
    with open(file_name) as f:
        text = f.read()

        print("Part 1: ", process_mul_expression(text))


def part_2():
    total = 0

    with open(file_name) as f:
        text = f.read()
        x = text.split("don't()")

        # Check for any possible value on the first split before don't since these should be counted.
        total += process_mul_expression(x[0])

        # For the rest, split by do(). The first split are the ones followed by don't() above, disregard it.
        for item in x[1:]:
            do_lines = item.split("do()")[1:]

            for do_line in do_lines:
                total += process_mul_expression(do_line)

    print("Part 2: ", total)


if __name__ == "__main__":
    part_1()
    part_2()
