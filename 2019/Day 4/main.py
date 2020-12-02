import re


def part_one():
    counter = 0
    for i in range(264360, 746325):
        if has_two_in_a_row(i) and never_decreases(i):
            counter += 1
    return counter


def has_two_in_a_row(num):
    word = str(num)
    index = 0
    while index < len(word):
        if index == len(word)-1:
            return bool(False)
        elif word[index] == word[index + 1]:
            return bool(True)
        index += 1
    return bool(False)


def never_decreases(num):
    word = str(num)
    index = 0
    while index < len(word):
        if index == len(word) - 1:
            return bool(True)
        pointer = word[index]
        next_pointer = word[index+1]
        if pointer > next_pointer:
            return bool(False)
        index += 1
    return bool(True)


def only_two_in_a_row(num):
    word = str(num)
    index = 0
    multiple_number = 10
    print("--------------" + str(num) + "===============")
    while index < len(word):
        if index == len(word)-1:
            print("reached last index, return false")
            return bool(False)
        elif word[index] == multiple_number:
            print("")
        elif word[index] == word[index + 1]:
            print("theres a double")
            if index == len(word) - 2:
                print("return true")
                return bool(True)
            if word[index] == word[index + 2]:
                print("but its more than 2")
                multiple_number = word[index]
            else:
                print("theres no multiple")
                print("return true!!!!")
                return bool(True)
        index += 1
    print("does it ever reach? return false")
    return bool(False)


def part_two():
    counter = 0
    for i in range(264360, 746325):
        if only_two_in_a_row(i) and never_decreases(i):
            counter += 1
    return counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(part_one())
    print(part_two())
