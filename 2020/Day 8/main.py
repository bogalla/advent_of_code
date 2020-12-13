import re


def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def part_one(inputs):
    print(inputs)
    hashmap = dict()
    counter = 0
    i = 0
    while bool(True):
        # print(i)
        # print(inputs[i])
        if i == len(inputs):
            print("---------------------------------")
            print(counter)
            print("---------------------------------")
            return 0
        if i in hashmap:
            # print("infinite loop at index : " + str(i))
            break
        else:
            hashmap[i] = 0
        op, code = re.match(r'^(.+) (.+)$', inputs[i]).groups()
        # print(op)
        # print(code)
        if op == "nop":
            i += 1
            continue
        elif op == "acc":
            if code[:1] == "+":
                counter = counter + int(code[1:])
            else:
                counter = counter - int(code[1:])
            i += 1
            continue
        elif op == "jmp":
            if code[:1] == "+":
                i = i + int(code[1:])
            else:
                i = i - int(code[1:])
    return counter


def part_two():
    base_input = file_to_list("input.txt")
    list_of_possible = []
    new_entry = ""
    i = 0
    while i < len(base_input):
        base_input = file_to_list("input.txt")
        op, code = re.match(r'^(.+) (.+)$', base_input[i]).groups()
        if op == "nop":
            new_entry = "jmp " + code
        elif op == "jmp":
            new_entry = "nop " + code
        else:
            i += 1
            continue
        base_input[i] = new_entry
        list_of_possible.append(base_input)
        i += 1
    # print(list_of_possible)
    for option in list_of_possible:
        if part_one(option) == 0:
            return 0


if __name__ == '__main__':
    # print("final : " + str(part_one(file_to_list("input.txt"))))
    print("final : " + str(part_two()))
