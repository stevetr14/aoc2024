from collections import defaultdict

from utils import parse_input

# file_name = "test.txt"
file_name = "input.txt"


def part_1():
    """
    Each instruction is followed by an operand as input.
    e.g. 0,1,2,4 -> Instruction 0 with operand 1, then instruction 2 with operand 4

    7 combo operands:
    - 0 to 3: literal 0 to 3
    - 4: register A
    - 5: register B
    - 6: register C
    - 7: invalid

    Eight instructions:
    - adv (opcode 0): A / (2 ** combo operand) -> store in A
    - bxl (opcode 1): Bitwise XOR of register B and LITERAL operand -> store in B
    - bst (opcode 2): Combo operand mod 8 -> store in B
    - jnz (opcode 3): Does nothing if A is 0, else jump instruction pointer to the value of its literal operand
    - bxc (opcode 4): Bitwise XOR of register B and register C (ignore its combo operand) -> store in B
    - out (opcode 5): Combo operand mod 8 -> output comma separated value
    - bdv (opcode 6): Same as adv, but store value in B
    - cdv (opcode 7): Same as adv, but store value in C
    """
    sections = parse_input(file_name, "\n\n")

    register_mappings = defaultdict(int)
    program = list(map(int, sections[1].replace("Program: ", "").split(",")))

    for line in sections[0].split("\n"):
        register, value = line.replace("Register ", "").split(": ")
        register_mappings[register] = int(value)

    # print(register_mappings, program)

    outputs = []

    instruction_pointer = 0

    while instruction_pointer < len(program):
        i = instruction_pointer

        # Instruction x, operand y
        x, y = program[i], program[i + 1]

        match x:
            case 0:
                if 0 <= y <= 3:
                    register_mappings["A"] = int(register_mappings["A"] / (2 ** y))
                elif y == 4:
                    register_mappings["A"] = int(register_mappings["A"] / (2 ** register_mappings["A"]))
                elif y == 5:
                    register_mappings["A"] = int(register_mappings["A"] / (2 ** register_mappings["B"]))
                elif y == 6:
                    register_mappings["A"] = int(register_mappings["A"] / (2 ** register_mappings["C"]))
                instruction_pointer += 2
            case 1:
                register_mappings["B"] = register_mappings["B"] ^ y
                instruction_pointer += 2
            case 2:
                if 0 <= y <= 3:
                    register_mappings["B"] = y % 8
                elif y == 4:
                    register_mappings["B"] = register_mappings["A"] % 8
                elif y == 5:
                    register_mappings["B"] = register_mappings["B"] % 8
                elif y == 6:
                    register_mappings["B"] = register_mappings["C"] % 8
                instruction_pointer += 2
            case 3:
                if register_mappings["A"] == 0:
                    instruction_pointer += 2
                else:
                    instruction_pointer = y
            case 4:
                register_mappings["B"] = register_mappings["B"] ^ register_mappings["C"]
                instruction_pointer += 2
            case 5:
                if 0 <= y <= 3:
                    outputs.append(y % 8)
                elif y == 4:
                    outputs.append(register_mappings["A"] % 8)
                elif y == 5:
                    outputs.append(register_mappings["B"] % 8)
                elif y == 6:
                    outputs.append(register_mappings["C"] % 8)
                instruction_pointer += 2
            case 6:
                if 0 <= y <= 3:
                    register_mappings["B"] = int(register_mappings["A"] / (2 ** y))
                elif y == 4:
                    register_mappings["B"] = int(register_mappings["A"] / (2 ** register_mappings["A"]))
                elif y == 5:
                    register_mappings["B"] = int(register_mappings["A"] / (2 ** register_mappings["B"]))
                elif y == 6:
                    register_mappings["B"] = int(register_mappings["A"] / (2 ** register_mappings["C"]))
                instruction_pointer += 2
            case 7:
                if 0 <= y <= 3:
                    register_mappings["C"] = int(register_mappings["A"] / (2 ** y))
                elif y == 4:
                    register_mappings["C"] = int(register_mappings["A"] / (2 ** register_mappings["A"]))
                elif y == 5:
                    register_mappings["C"] = int(register_mappings["A"] / (2 ** register_mappings["B"]))
                elif y == 6:
                    register_mappings["C"] = int(register_mappings["A"] / (2 ** register_mappings["C"]))
                instruction_pointer += 2

    print(len(outputs), len(program))
    print("Part 1: ", ",".join(list(map(str, outputs))))


def part_2():
    lines = parse_input(file_name)
    print(lines)

    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    part_1()
    # part_2()
