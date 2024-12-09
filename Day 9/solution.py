from pprint import pprint
from itertools import groupby

from utils import parse_input

file_name = "test.txt"
# file_name = "input.txt"


def part_1():
    disk_map = parse_input(file_name)[0]

    translated = []

    file_id = 0

    for idx, c in enumerate(disk_map, start=1):
        if idx % 2 != 0:
            # file ID
            for i in range(int(c)):
                translated.append(file_id)
            file_id += 1
        else:
            for i in range(int(c)):
                translated.append(".")

    while translated:
        file_num: int | str = translated.pop()
        if type(file_num) is int:
            try:
                c = translated.index(".")
            except ValueError:
                translated.append(file_num)
                break
            translated[c] = file_num

    print("Part 1: ", sum((idx * i for idx, i in enumerate(translated))))


def part_2():
    disk_map = parse_input(file_name)[0]

    translated = []

    file_id = 0

    for idx, c in enumerate(disk_map, start=1):
        if idx % 2 != 0:
            # file ID
            for i in range(int(c)):
                translated.append(file_id)
            file_id += 1
        else:
            for i in range(int(c)):
                translated.append(".")

    file_num_occurrence = [(k, len(list(g))) for k, g in groupby(translated)]

    print(file_num_occurrence)

    # while len(translated) > 0:
    #     print()
    #     file_num: int | str = translated.pop()
    #     if type(file_num) is int:
    #         try:
    #             c = translated.index(".")
    #         except ValueError:
    #             translated.append(file_num)
    #             break
    #         translated[c] = file_num

    # print("Part 2: ", sum((idx * i for idx, i in enumerate(translated))))


if __name__ == "__main__":
    # part_1()
    part_2()
