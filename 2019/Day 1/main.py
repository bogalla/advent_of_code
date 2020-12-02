def part_one():
    counter = 0
    for x in numbers:
        temp = int(x/3) - 2
        counter = counter + temp
    return counter


def part_two():
    counter = 0
    for module in numbers:
        x = module
        while int(x/3) - 2 > 0:
            temp = int(x / 3) - 2
            counter = counter + temp
            x = temp
    return counter


def file_to_list(filename):
    file = open(filename, 'r')
    number_list = []
    for x in file:
        number_list.append(int(x))
    return number_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = file_to_list('input.txt')
    print(part_one())
    print(part_two())
