import math
import time
from collections import deque
from functools import cache

from utils import parse_input

# file_name = "test.txt"
file_name = "input.txt"


def flatten_list(mixed_list):
    flattened = deque()
    for item in mixed_list:
        if isinstance(item, tuple):
            flattened.extend(item)
        else:
            flattened.append(item)
    return flattened


@cache
def split_stone(stone: str, iteration: int, max_iteration: int) -> int:
    # Base case
    if iteration > max_iteration:
        return 1

    count = 0

    if stone == "0":
        count += split_stone("1", iteration + 1, max_iteration)
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        # Use int to remove leading 0's from a string.
        left, right = int(stone[:mid]), int(stone[mid:])
        count += split_stone(str(left), iteration + 1, max_iteration)
        count += split_stone(str(right), iteration + 1, max_iteration)
    else:
        count += split_stone(str(int(stone) * 2024), iteration + 1, max_iteration)

    return count


def part_1():
    arrangement = parse_input(file_name)[0].split(" ")

    start = time.time()

    total = 0
    for stone in arrangement:
        # Example gives 55312 for 25 blinks
        total += split_stone(stone, iteration=1, max_iteration=25)

    end = time.time()

    print("Part 1: ", total, f"time: {round(end - start, 3)}")


def part_2():
    arrangement = parse_input(file_name)[0].split(" ")

    start = time.time()

    total = 0
    for stone in arrangement:
        # Example gives 55312 for 25 blinks
        total += split_stone(stone, iteration=1, max_iteration=75)

    end = time.time()

    print("Part 2: ", total, f"time: {round(end - start, 3)}")


if __name__ == "__main__":
    part_1()
    part_2()
