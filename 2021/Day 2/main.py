def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def part_one(inputs):
    print("pt 1")
    horiPos = 0
    depth = 0
    for elem in inputs:
        x = elem.split()
        print(x)
        if x[0] == "forward":
            horiPos+=int(x[1])
        elif x[0] == "up":
            depth-=int(x[1])
        elif x[0] == "down":
            depth+=int(x[1])

    print(horiPos)
    print(depth)
    return horiPos*depth

def part_two(inputs):
    print("pt 2")
    print("pt 1")
    horiPos = 0
    aim = 0
    depth = 0
    for elem in inputs:
        x = elem.split()
        print(x)
        if x[0] == "forward":
            horiPos += int(x[1])
            depth += int(x[1])*aim
        elif x[0] == "up":
            aim -= int(x[1])
        elif x[0] == "down":
            aim += int(x[1])

    print(horiPos)
    print(aim)
    return horiPos * depth


if __name__ == '__main__':
    inputs = file_to_list("input.txt")
    print(inputs)
    # print("final : " + str(part_one(inputs)))

    print("final : " + str(part_two(inputs)))
