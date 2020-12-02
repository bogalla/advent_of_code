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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(part_one())
    # print(part_two())
