from collections import deque
from pprint import pprint
from itertools import groupby, chain

from utils import parse_input

# file_name = "test.txt"
file_name = "input.txt"


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
                test_idx -= 2
            elif diff == 0:
                file_num_occurrence[test_idx], file_num_occurrence[start_idx] = (
                    file_num_occurrence[start_idx], file_num_occurrence[test_idx]
                )
            else:
                start_idx -= 1
                test_idx -= 2
        else:
            test_idx += 1
            continue
    else:
        start_idx -= 1

    # result_string = ' '.join([f" {item[0]} " * item[1] for item in file_num_occurrence])
    #
    # print(result_string)

    check_sum = 0
    x = -1

    for item in file_num_occurrence:
        for i in range(item[1]):
            x += 1
            check_sum += item[0] * x if item[0] != "." else 0

    print("Part 2: ", check_sum)


def main():
    with open(file_name, 'r') as file:
        disk_map = file.read()
        disk_map = disk_map.rstrip('\n')

    file_blocks, free_blocks = getBlockLists(disk_map)
    blocks = createBlocks(file_blocks, free_blocks)
    blocks = moveFiles(blocks)
    print(blocks)
    # result = checkSum(blocks)
    # print(result)


# Splits the disk map into 2 int lists representing the file blocks and the free space blocks
def getBlockLists(disk_map):
    free_blocks = []
    file_blocks = []

    for i in range(len(disk_map)):
        if i % 2 == 0:  # even indices are file blocks and odd are free blocks
            file_blocks.append(int(disk_map[i]))
        else:
            free_blocks.append(int(disk_map[i]))

    return file_blocks, free_blocks


# Returns a single list representing the block representation of the original puzzle input
def createBlocks(file_blocks, free_blocks):
    block_list = []
    for i in range(len(file_blocks)):
        block_list.append([str(i)] * file_blocks[i])
        if i < len(free_blocks):  # free_blocks list has 1 less element than file_blocks
            block_list.append(["."] * free_blocks[i])
    return block_list


# Moves file blocks into valid memory blocks and returns the new list
def moveFiles(block_list):
    # Move files by descending ID
    for file_index in range(len(block_list) - 1, -1, -1):
        file_block = block_list[file_index]

        # Skip free blocks
        if all(char == "." for char in file_block): continue

        file_len = len(file_block)

        # Find a block of free memory that can fit the file
        for i in range(file_index):  # Only check free_blocks that appear before the file block
            if "." in block_list[i] and len(block_list[i]) >= file_len:
                # Move the file into the free block
                free_len = len(block_list[i])
                block_list[i] = file_block
                block_list[file_index] = ["."] * file_len

                # Handle remaining free space
                remaining_mem = free_len - file_len
                if remaining_mem > 0:
                    # Insert the remaining memory as a new free block
                    block_list.insert(i + 1, ["."] * remaining_mem)
                break  # move on to the next file

    # Expand every file_block so every ID occupies its own index and every free_block so every "." occupies its own index
    expanded_block_list = []
    for block in block_list:
        expanded_block_list.extend(block)
    return expanded_block_list


# Multiplies file ID by its index and returns the sum of these values for all file blocks
def checkSum(block_list):
    result = 0
    for i, block in enumerate(block_list):
        if block != ".":
            result += i * int(block)
    return result


if __name__ == "__main__":
    # part_1()
    part_2()
    # main()
