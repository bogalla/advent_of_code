def file_to_list(filename):
    file = open(filename, 'r')
    return[line.strip() for line in file]

def part_one():
    inputs = file_to_list("input.txt")
    sum = 0
    for line in inputs:
        nums = [int(x) for x in line if x.isdigit()]
        print(nums)
        firstNum = int(nums[0])
        lastNum = int(nums[-1])
        elem = firstNum*10 + lastNum
        print(elem)
        sum += int(elem)
    return sum


def part_two():
    inputs = file_to_list("input.txt")
    sum = 0
    for line in inputs:
        print(line)
        if "one" in line:
            line = line.replace("one", "one1one")
        if "two" in line:
            line = line.replace("two", "two2two")
        if "three" in line:
            line = line.replace("three", "three3three")
        if "four" in line:
            line = line.replace("four", "four4four")
        if "five" in line:
            line = line.replace("five", "five5five")
        if "six" in line:
            line = line.replace("six", "six6six")
        if "seven" in line:
            line = line.replace("seven", "seven7seven")
        if "eight" in line:
            line = line.replace("eight", "eight8eight")
        if "nine" in line:
            line = line.replace("nine", "nine9nine")
        nums = [int(x) for x in line if x.isdigit()]
        print(nums)
        firstNum = int(nums[0])
        lastNum = int(nums[-1])
        elem = firstNum * 10 + lastNum
        print(elem)
        sum += int(elem)

    return sum


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
