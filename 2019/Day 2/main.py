def file_to_list(filename):
    list_of_numbers = []
    with open(filename, 'r') as file:
        for line in file:
            for num in line.split(','):
                list_of_numbers.append(int(num))
    return list_of_numbers


def part_one():
    numbers = file_to_list('input.txt')
    return calculate_output(numbers)


def calculate_output(numbers):
    index = 0
    while index < len(numbers):
        if numbers[index] == 1:
            numbers[numbers[index + 3]] = numbers[numbers[index + 1]] + numbers[numbers[index + 2]]
            index = index + 4
        elif numbers[index] == 2:
            numbers[numbers[index + 3]] = numbers[numbers[index + 1]] * numbers[numbers[index + 2]]
            index = index + 4
        elif numbers[index] == 99:
            break
    return numbers


def part_two():
    first_variable = 0
    while first_variable < 100:
        second_variable = 0
        while second_variable < 100:
            print("(" + str(first_variable) + ", " + str(second_variable) + ")")
            numbers = file_to_list('input.txt')
            test_numbers = change_set(first_variable, second_variable, numbers)
            final_output = calculate_output(test_numbers)
            if final_output[0] == 19690720:
                print("we found it!")
                return 100 * first_variable + second_variable
            second_variable += 1
        first_variable += 1


def change_set(num1, num2, numbers):
    numbers[1] = num1
    numbers[2] = num2
    return numbers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(part_one())
    print(part_two())
