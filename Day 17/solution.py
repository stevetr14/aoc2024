from random import randint
from collections import defaultdict

from utils import parse_input

# file_name = "test.txt"
file_name = "input.txt"


def get_adv_combo_operand_output(operand, register_mappings: defaultdict) -> int:
    if 0 <= operand <= 3:
        return int(register_mappings["A"] / (2 ** operand))
    elif operand == 4:
        return int(register_mappings["A"] / (2 ** register_mappings["A"]))
    elif operand == 5:
        return int(register_mappings["A"] / (2 ** register_mappings["B"]))
    elif operand == 6:
        return int(register_mappings["A"] / (2 ** register_mappings["C"]))


def get_mod_combo_operand_output(operand, register_mappings: defaultdict) -> int:
    if 0 <= operand <= 3:
        return operand % 8
    elif operand == 4:
        return register_mappings["A"] % 8
    elif operand == 5:
        return register_mappings["B"] % 8
    elif operand == 6:
        return register_mappings["C"] % 8


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
    pass
    # sections = parse_input(file_name, "\n\n")
    #
    # program = list(map(int, sections[1].replace("Program: ", "").split(",")))
    #
    # for line in sections[0].split("\n"):
    #     register, value = line.replace("Register ", "").split(": ")
    #     register_mappings[register] = int(value)
    #
    # outputs = []
    # instruction_pointer = 0
    #
    # while instruction_pointer < len(program):
    #     i = instruction_pointer
    #
    #     # Instruction x, operand y
    #     x, y = program[i], program[i + 1]
    #
    #     match x:
    #         case 0:
    #             register_mappings["A"] = get_adv_combo_operand_output(y)
    #             instruction_pointer += 2
    #         case 1:
    #             register_mappings["B"] = register_mappings["B"] ^ y
    #             instruction_pointer += 2
    #         case 2:
    #             register_mappings["B"] = get_mod_combo_operand_output(y)
    #             instruction_pointer += 2
    #         case 3:
    #             instruction_pointer = instruction_pointer + 2 if register_mappings["A"] == 0 else y
    #         case 4:
    #             register_mappings["B"] = register_mappings["B"] ^ register_mappings["C"]
    #             instruction_pointer += 2
    #         case 5:
    #             outputs.append(get_mod_combo_operand_output(y))
    #             instruction_pointer += 2
    #         case 6:
    #             register_mappings["B"] = get_adv_combo_operand_output(y)
    #             instruction_pointer += 2
    #         case 7:
    #             register_mappings["C"] = get_adv_combo_operand_output(y)
    #             instruction_pointer += 2
    #
    # print(int("".join(list(map(str, outputs)))))
    #
    # print("Part 1: ", ",".join(list(map(str, outputs))))


def test(program: list[int], register_mappings: defaultdict) -> int:
    outputs = []
    instruction_pointer = 0

    while instruction_pointer < len(program):
        i = instruction_pointer

        # Instruction x, operand y
        x, y = program[i], program[i + 1]

        match x:
            case 0:
                register_mappings["A"] = get_adv_combo_operand_output(y, register_mappings)
                instruction_pointer += 2
            case 1:
                register_mappings["B"] = register_mappings["B"] ^ y
                instruction_pointer += 2
            case 2:
                register_mappings["B"] = get_mod_combo_operand_output(y, register_mappings)
                instruction_pointer += 2
            case 3:
                instruction_pointer = instruction_pointer + 2 if register_mappings["A"] == 0 else y
            case 4:
                register_mappings["B"] = register_mappings["B"] ^ register_mappings["C"]
                instruction_pointer += 2
            case 5:
                outputs.append(get_mod_combo_operand_output(y, register_mappings))
                instruction_pointer += 2
            case 6:
                register_mappings["B"] = get_adv_combo_operand_output(y, register_mappings)
                instruction_pointer += 2
            case 7:
                register_mappings["C"] = get_adv_combo_operand_output(y, register_mappings)
                instruction_pointer += 2

    return int("".join(list(map(str, outputs))))


def part_2():
    register_mappings = defaultdict(int)
    sections = parse_input(file_name, "\n\n")

    program = list(map(int, sections[1].replace("Program: ", "").split(",")))

    # count = 100_000_000_000_000

    def get_random_seed():
        s = ""
        for i in range(16):
            s = s + str(randint(1, 7))

        return int(s)

    output = 0

    while output != int("".join(list(map(str, program)))):
        register_mappings["A"] = get_random_seed()
        output = test(program, register_mappings)
        print(output)

    # print("Part 2: ", 0)


if __name__ == "__main__":
    # part_1()
    part_2()
