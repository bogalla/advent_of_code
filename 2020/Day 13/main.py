import math
from sympy.ntheory.modular import crt


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


# def part_two():
#     data = file_to_list("input_t.txt")
#     modulos = []
#     remainders = []
#
#     bus_timestamps = data[1].split(",")
#     for i in range(len(bus_timestamps)):
#         print(bus_timestamps[i])
#         if bus_timestamps[i].isnumeric():
#             modulos.append(int(bus_timestamps[i]))
#             remainders.append((-i) % modulos[-1])
#
#     print(modulos)
#     print(remainders)
#
#     ans = crt(modulos, remainders)
#
#     return ans


def part_two():
    with open("input_t.txt", "r") as f:
        f = f.read().splitlines()

    busses = [(int(b), i) for i, b in enumerate(f[1].split(",")) if b != "x"]
    print(busses)

    jump = i = busses[0][0]
    print("initial jump = " + str(jump))
    print("initial i = " + str(i))
    for b in busses[1:]:
        print(b)
        print("(" + str(i) + " + " + str(b[1]) + ") modulo " + str(b[0]) + " = " + str((i + b[1]) % b[0]))
        while (i + b[1]) % b[0] != 0:
            print("i = " + str(i))
            i += jump
            print("(" + str(i) + " + " + str(b[1]) + ") modulo " + str(b[0]) + " = " + str((i + b[1]) % b[0]))
        jump *= b[0]
        print("jump = " + str(jump))

    return i


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
