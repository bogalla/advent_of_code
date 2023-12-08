import re

def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def part_one():
    inputs = file_to_list("input.txt")
    print(inputs)
    redMax = 12
    blueMax = 14
    greenMax = 13
    sum = 0
    for line in inputs:
        fail = False
        gameID = int(line[line.find(' ')+1 : line.find(':')])
        line = line[line.find(':')+1:]
        print(line)
        games = line.split(';')
        print(games)
        for game in games:
            insts = game.split(',')
            print(insts)
            for inst in insts:
                numL = int(re.findall(r'\d+', inst)[0])
                if "red" in inst:
                    if numL > redMax:
                        fail = True
                if "blue" in inst:
                    if numL > blueMax:
                        fail = True
                if "green" in inst:
                    if numL > greenMax:
                        fail = True

        if not fail:
            sum += gameID
        print("-------------------------")
    return sum


if __name__ == '__main__':
    print("final : " + str(part_one()))
    # print("final : " + str(part_two()))
