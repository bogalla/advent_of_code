import math


def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def part_one():
    inputs = file_to_list("input.txt")
    print(inputs)
    initial = int(inputs[0])
    buses = inputs[1].split(",")
    print(buses)
    times = dict()
    for bus in buses:
        if bus != "x":
            print(bus)
            times[((math.ceil(initial/int(bus))*int(bus)) - initial)] = bus
            print(times)
    print(times)
    list_keys = times.keys()
    minimum_time = min(list_keys)
    return int(minimum_time)*int(times[minimum_time])


if __name__ == '__main__':
    print("final : " + str(part_one()))
    # print("final : " + str(part_two()))
