def file_to_list(filename):
    list_of_numbers = []
    with open(filename, 'r') as file:
        for line in file:
            for num in line.split(','):
                list_of_numbers.append(int(num))
    return list_of_numbers


def part_one():
    numbers = file_to_list('input.txt.txt')
    return calculate_output(numbers)


def calculate_opcode(num):
    # 1002 becomes [2,0,0,1,0] opcode,
    pos_nums = []
    while num > 0:
        pos_nums.append(num % 10)
        num = num // 10
    print(pos_nums)
    i = 0
    while bool(True):
        if len(pos_nums) < 5:
            break
        pos_nums.append(0)
        i += 1
    print(pos_nums)
    return pos_nums


def do_change(numbers, index, parameter_mode_1, parameter_mode_2, parameter_mode_3):
    num1, num2 = 0, 0
    if parameter_mode_1 == 0:
        # position mode
        num1 = numbers[numbers[index+1]]
    elif parameter_mode_1 == 1:
        # number mode
        num1 = numbers[index + 1]
    if parameter_mode_2 == 0:
        # position mode
        num2 = numbers[numbers[index+2]]
    elif parameter_mode_2 == 1:
        # number mode
        num2 = numbers[index + 2]
    if parameter_mode_3 == 0:
        # position mode
        numbers[numbers[index + 3]] = num1 + num2
    elif parameter_mode_3 == 1:
        # number mode
        numbers[index + 3] = num1 + num2


def calculate_output(numbers):
    index = 0
    while index < len(numbers):
        instruction = calculate_opcode(numbers[index])
        opcode = instruction[0]
        parameter_mode_1 = instruction[2]
        parameter_mode_2 = instruction[3]
        parameter_mode_3 = instruction[4]

        if opcode == 1:
            numbers = do_change(numbers, index, parameter_mode_1, parameter_mode_2, parameter_mode_3)
            numbers[numbers[index + 3]] = numbers[numbers[index + 1]] + numbers[numbers[index + 2]]
            index = index + 4
        elif opcode == 2:
            numbers[numbers[index + 3]] = numbers[numbers[index + 1]] * numbers[numbers[index + 2]]
            index = index + 4
        elif opcode == 99:
            break
    return numbers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(part_one())
    # print(part_two())
