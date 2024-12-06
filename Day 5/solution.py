from collections import defaultdict
from itertools import permutations

from utils import parse_input

file_name = "test.txt"
# file_name = "input.txt"


def part_1():
    total = 0

    with open(file_name) as f:
        text = f.read()
        first_part, second_part = text.split("\n\n")
        rules = defaultdict(list)

        def check_rules(lhs: str, rhs: list[str]) -> bool:
            return all(item in rules.get(lhs, []) for item in rhs)

        pairs = [line.strip().split("|") for line in first_part.split()]
        for pair in pairs:
            if rules.get(pair[0]) is None:
                rules[pair[0]] = [pair[1]]
            else:
                rules[pair[0]].append(pair[1])

        for line in second_part.split():
            page_nums = line.split(",")
            checks = [check_rules(page_nums[i], page_nums[i + 1:]) for i in range(len(page_nums))]

            if all(checks):
                # Assume each line of page numbers have odd number of entries.
                middle_index = int(len(page_nums) / 2)
                print(page_nums, page_nums[middle_index])

                total += int(page_nums[middle_index])

    print("Part 1: ", total)


def part_2():
    total = 0

    with open(file_name) as f:
        text = f.read()
        first_part, second_part = text.split("\n\n")
        rules = defaultdict(list)

        def check_rules(lhs: str, rhs: list[str]) -> bool:
            return all(item in rules.get(lhs, []) for item in rhs)

        pairs = [line.strip().split("|") for line in first_part.split()]
        for pair in pairs:
            if rules.get(pair[0]) is None:
                rules[pair[0]] = [pair[1]]
            else:
                rules[pair[0]].append(pair[1])

        for line in second_part.split():
            page_nums = line.split(",")
            checks = [check_rules(page_nums[i], page_nums[i + 1:]) for i in range(len(page_nums))]
            # Assume each line of page numbers have odd number of entries.
            middle_index = int(len(page_nums) / 2)

            if not all(checks):
                for index, page_num in enumerate(page_nums):
                    a = page_nums.copy()
                    b = a.pop(index)
                    c = int(len(a) / 2)
                    print(b, a[:c], a[c:])
                # print(line, checks)
                # for permutation in permutations(page_nums, len(page_nums)):
                #     print(permutation)
                # permutation = list(permutation)
                # checks_2 = [check_rules(permutation[i], permutation[i + 1:]) for i in range(len(permutation))]
                #
                # if all(checks_2):
                #     total += int(permutation[middle_index])
                #     break

    print("Part 2: ", total)


if __name__ == "__main__":
    # part_1()
    part_2()
