import math


def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def part_one():
    seat_list = file_to_list("input.txt")
    # print(seat_list)
    final_list = []
    row = 0
    seat = 0
    for entry in seat_list:
        # print(entry)
        i = 0
        lower_bound = 0
        upper_bound = 127
        while i < 7:
            midpoint = (upper_bound + lower_bound) / float(2)
            # print("midpoint " + str(midpoint))
            # print(entry[i])
            if entry[i] == 'F':
                upper_bound = math.floor(midpoint)
            elif entry[i] == 'B':
                lower_bound = math.ceil(midpoint)
            i += 1
            # print("upper: " + str(upper_bound))
            # print("lower: " + str(lower_bound))
        row = upper_bound
        # print("--------------------------------")
        lower_bound = 0
        upper_bound = 7
        while i < 10:
            # print(entry[i])
            midpoint = (upper_bound + lower_bound) / float(2)
            # print("midpoint: " + str(midpoint))
            if entry[i] == 'L':
                upper_bound = math.floor(midpoint)
            elif entry[i] == 'R':
                lower_bound = math.ceil(midpoint)
            i += 1
            # print("upper: " + str(upper_bound))
            # print("lower: " + str(lower_bound))
        seat = upper_bound
        final_list.append((row*8)+seat)
    # print(final_list)
    print(sorted(final_list))
    return sorted(final_list)


def multiply(listi):
    maximum = 0
    for item in listi:
        if item > maximum:
            maximum = item
    return maximum


def part_two():
    final_list = part_one()
    i = 0
    while i < len(final_list):
        if final_list[i+1] != final_list[i] + 1:
            print(final_list[i])
        i += 1


if __name__ == '__main__':
    # print("final : " + str(multiply(part_one())))
    print("final : " + str(part_two()))
    # print(part_three())