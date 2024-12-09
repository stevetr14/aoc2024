from collections import deque
from pprint import pprint
from itertools import groupby, chain

from utils import parse_input

file_name = "test.txt"
# file_name = "input.txt"


def part_1():
    disk_map = parse_input(file_name)[0]
    translated = deque()
    file_id = 0

    for idx, c in enumerate(disk_map, start=1):
        if idx % 2 != 0:
            # file ID
            translated.extend([file_id] * int(c))
            file_id += 1
        else:
            translated.extend(["."] * int(c))

    while translated:
        file_num: int | str = translated.pop()
        if type(file_num) is int:
            try:
                c = translated.index(".")
            except ValueError:
                translated.append(file_num)
                break
            translated[c] = file_num

    check_sum = sum((idx * i for idx, i in enumerate(translated)))

    print("Part 1: ", check_sum)


def part_2():
    disk_map = parse_input(file_name)[0]
    translated = deque()
    file_id = 0

    for idx, c in enumerate(disk_map, start=1):
        if idx % 2 != 0:
            # file ID
            translated.extend([file_id] * int(c))
            file_id += 1
        else:
            translated.extend(["."] * int(c))

    file_num_occurrence = deque((k, sum(1 for _ in g)) for k, g in groupby(translated))

    test_idx = 0
    start_idx = -1

    while start_idx != -len(file_num_occurrence):
        # print()
        # print(file_num_occurrence)
        entry = file_num_occurrence[start_idx]

        if entry[0] == ".":
            start_idx -= 1
            continue
        elif (len(file_num_occurrence) + start_idx) == test_idx:
            test_idx = 0
            start_idx -= 1
            continue

        item = file_num_occurrence[test_idx]

        if item[0] != ".":
            test_idx += 1
            continue

        item_length = item[1]
        entry_length = entry[1]
        if entry_length <= item_length:
            # If file is before the next empty space then it's already in order
            if file_num_occurrence.index(entry) < file_num_occurrence.index(item):
                continue

            diff = item_length - entry_length
            if diff > 0:
                file_num_occurrence[test_idx] = (".", diff)
                file_num_occurrence[start_idx] = (".", entry[1])
                file_num_occurrence.rotate(-test_idx)
                file_num_occurrence.appendleft(entry)
                file_num_occurrence.rotate(test_idx)
            elif diff == 0:
                file_num_occurrence[test_idx], file_num_occurrence[start_idx] = (
                    file_num_occurrence[start_idx], file_num_occurrence[test_idx]
                )
            else:
                start_idx -= 1
        else:
            test_idx += 1
            continue
    else:
        start_idx -= 1

    # result_string = ''.join([str(item[0]) * item[1] for item in file_num_occurrence])

    # print(result_string)
    # print(file_num_occurrence)

    # check_sum = sum((idx * int(i)) if i != "." else 0 for idx, i in enumerate(result_string))

    check_sum = 0
    x = -1

    for item in file_num_occurrence:
        for i in range(item[1]):
            x += 1
            check_sum += item[0] * x if item[0] != "." else 0

    # check_sum = sum(
    #     idx * int(i) if i != '.' else 0 for idx, i in enumerate(
    #         chain(*((str(item[0]) * item[1] for item in file_num_occurrence)))
    #     )
    # )
    #
    print("Part 2: ", check_sum)


if __name__ == "__main__":
    # part_1()
    part_2()
