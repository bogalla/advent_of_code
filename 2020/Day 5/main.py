import math


def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def part_one():
    seat_list = file_to_list("input.txt")
    final_list = []
    for entry in seat_list:
        i = 0
        lower_bound = 0
        upper_bound = 127
        while i < 7:
            midpoint = (upper_bound + lower_bound) / float(2)
            if entry[i] == 'F':
                upper_bound = math.floor(midpoint)
            elif entry[i] == 'B':
                lower_bound = math.ceil(midpoint)
            i += 1
        # upper bound and lower bound are the same here
        row = upper_bound
        lower_bound = 0
        upper_bound = 7
        while i < 10:
            midpoint = (upper_bound + lower_bound) / float(2)
            if entry[i] == 'L':
                upper_bound = math.floor(midpoint)
            elif entry[i] == 'R':
                lower_bound = math.ceil(midpoint)
            i += 1
        # upper bound and lower bound are the same here
        seat = upper_bound
        final_list.append((row*8)+seat)
    return sorted(final_list)


def multiply(inputs):
    maximum = 0
    for item in inputs:
        if item > maximum:
            maximum = item
    return maximum


def part_two():
    final_list = part_one()
    i = 0
    while i < len(final_list)-1:
        if final_list[i+1] != final_list[i] + 1:
            return final_list[i + 1]
        i += 1


if __name__ == '__main__':
    # print("final : " + str(multiply(part_one())))
    print("final : " + str(part_two()))
