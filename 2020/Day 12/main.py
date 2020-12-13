ship_pos = [0, 0]
wayship_pos = [10, 1]
facing = "E"
hashmap = {
    "ER": "S",
    "EL": "N",
    "SR": "W",
    "SL": "E",
    "WR": "N",
    "WL": "S",
    "NR": "E",
    "NL": "W"
}


def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def move_ship(opcode, num):
    global ship_pos
    if opcode == "N":
        ship_pos[1] += num
    elif opcode == "S":
        ship_pos[1] -= num
    elif opcode == "E":
        ship_pos[0] += num
    elif opcode == "W":
        ship_pos[0] -= num
    else:
        print("oopsies!!")


def move_forward(num):
    move_ship(facing, num)


def rotate_ship(opcode, num):
    global facing
    print("facing : " + facing)
    i = 0
    while i < num:
        print(i)
        key = facing + opcode
        facing = hashmap[key]
        print("facing : " + facing)
        i += 90


def part_one():
    global ship_pos
    inputs = file_to_list("input.txt")
    for line in inputs:
        opcode = line[:1]
        num = int(line[1:])
        print("opcode: " + opcode)
        if opcode == "N" or opcode == "S" or opcode == "E" or opcode == "W":
            move_ship(opcode, num)
        elif opcode == "F":
            move_forward(num)
        elif opcode == "R" or opcode == "L":
            rotate_ship(opcode, num)
    print(ship_pos)
    return abs(ship_pos[0]) + abs(ship_pos[1])


def move_wayship(opcode, num):
    global wayship_pos
    if opcode == "N":
        wayship_pos[1] += num
    elif opcode == "S":
        wayship_pos[1] -= num
    elif opcode == "E":
        wayship_pos[0] += num
    elif opcode == "W":
        wayship_pos[0] -= num
    else:
        print("oopsies!!")


def move_forward_wayship(num):
    global wayship_pos
    global ship_pos
    ship_pos[0] += (wayship_pos[0] * num)
    ship_pos[1] += (wayship_pos[1] * num)


def rotate_ship_wayship(opcode, num):
    i = 0
    while i < num:
        print(i)
        temp = wayship_pos[0]
        wayship_pos[0] = wayship_pos[1]
        wayship_pos[1] = temp
        if opcode == "R":
            wayship_pos[1] -= (wayship_pos[1] * 2)
        elif opcode == "L":
            wayship_pos[0] -= (wayship_pos[0] * 2)
        i += 90


def part_two():
    global ship_pos
    inputs = file_to_list("input.txt")
    for line in inputs:
        print("ship position: " + str(ship_pos))
        opcode = line[:1]
        num = int(line[1:])
        print("opcode: " + opcode)
        if opcode == "N" or opcode == "S" or opcode == "E" or opcode == "W":
            move_wayship(opcode, num)
        elif opcode == "F":
            move_forward_wayship(num)
        elif opcode == "R" or opcode == "L":
            rotate_ship_wayship(opcode, num)
    print(ship_pos)
    return abs(ship_pos[0]) + abs(ship_pos[1])


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
