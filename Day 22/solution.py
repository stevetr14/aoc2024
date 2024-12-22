import time
from collections import defaultdict, Counter
from functools import cache
from itertools import pairwise

from utils import parse_input


# file_name = "test.txt"
file_name = "input.txt"


@cache
def get_next_secret_number(value: int) -> int:
    modulo = 16777216

    value = (value ^ (value * 64)) % modulo
    value = (value ^ (value // 32)) % modulo  # Divide and floor
    value = (value ^ (value * 2048)) % modulo

    return value


def part_one():
    numbers = list(map(int, parse_input(file_name)))
    total = 0

    for number in numbers:
        secret = get_next_secret_number(number)
        for i in range(1999):
            secret = get_next_secret_number(secret)

        total += secret

    print("Part 1: ", total)


def part_two():
    numbers = list(map(int, parse_input(file_name)))
    sequences = defaultdict(list)

    start = time.time()

    for number in numbers:
        sequence = [str(number)[-1]]  # Including the initial secret number
        secret = get_next_secret_number(number)

        # Precompute the sequence using a loop
        for _ in range(2000):
            sequence.append(str(secret)[-1])
            secret = get_next_secret_number(secret)

        sequences[number] = sequence

    z = Counter()

    # Map unique 4 price changes sequence to a price value, only care about the first time the sequence occurs for each
    # secret number.
    for k, v in sequences.items():
        prices = list(map(int, v))
        changes = [b - a for a, b in pairwise(prices)]
        # Note prices have 2001 entries, changes have 2000 entries. Start from the 5th item in prices mapping to the
        # 4th item in changes.
        x = {tuple(changes[idx - 4:idx]): prices[idx] for idx in range(4, len(prices))}
        z += Counter(x)

    end = time.time()

    print("Part 2: ", max(z.values()), "- time: ", round(end - start, 2))


if __name__ == "__main__":
    part_one()
    part_two()
