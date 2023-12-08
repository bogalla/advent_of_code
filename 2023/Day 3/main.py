def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def part_one():
    inputs = file_to_list("input.txt")


if __name__ == '__main__':
    print("final : " + str(part_one()))
    # print("final : " + str(part_two()))
