# this is day 1
def part_one():
    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                return i * j


def part_two():
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    return i*j*k


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