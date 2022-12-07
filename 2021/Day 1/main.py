# this is day 1
def part_one(numbers):
    incr = 0
    for i, k in enumerate(numbers):
        if i != 0 and k > numbers[i - 1]:
            incr += 1
    return incr


def part_two(numbers):
    incr = 0
    for i, k in enumerate(numbers):
        if i == 0:
            currentTriple = k + numbers[i + 1] + numbers[i + 2]
        if i < len(numbers) - 3:

            nextTriple = numbers[i + 1] + numbers[i + 2] + numbers[i + 3]
            if nextTriple > currentTriple:
                incr += 1

        currentTriple = nextTriple
    return incr


def file_to_list(filename):
    file = open(filename, 'r')
    number_list = []
    for x in file:
        number_list.append(int(x))
    return number_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = file_to_list('2021d1.txt')
    # print(part_one(numbers))
    print(part_two(numbers))
