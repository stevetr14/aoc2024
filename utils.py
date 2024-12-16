import heapq
from itertools import islice

from typing import Any

import numpy as np


def parse_input(file_name: str, split_char: str = "\n") -> list[str]:
    with open(file_name) as f:
        return [section for section in f.read().split(split_char) if section.strip() != ""]


def batched(iterable, n):
    """
    Implementation of batched for python < 3.12 (https://docs.python.org/3/library/itertools.html#itertools.batched).
    """
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def transpose_list(list_: list[any]) -> list[any]:
    return list(map(list, zip(*list_)))


def rotate_matrix_90_anti_clockwise(matrix: list[any]) -> list[any]:
    return [[x[i] for x in matrix] for i in range(len(matrix))][::-1]


def rotate_matrix_90_clockwise(matrix: list[any]) -> list[any]:
    return list(list(x)[::-1] for x in zip(*matrix))


def find_position_in_matrix(matrix: list[list[str]], char: str) -> tuple[int, int] | None:
    """Return the (x, y) position of a given character in a 2D matrix."""
    if not matrix:
        return None

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == char:
                return i, j

    return None
