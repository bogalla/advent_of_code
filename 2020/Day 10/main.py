def file_to_list(filename):
    file = open(filename, 'r')
    return [int(line.strip()) for line in file]


def part_one():
    inputs = file_to_list("input.txt")
    inputs.sort()
    print(inputs)
    answers = []
    i = 0
    while i < len(inputs):
        if i == len(inputs)-1:
            print("end")
            break
        answers.append(inputs[i+1] - inputs[i])
        i += 1
    print(answers)
    count_1 = 1
    count_3 = 1
    for a in answers:
        if a == 1:
            count_1 += 1
        elif a == 3:
            count_3 += 1
    print(count_1)
    print(count_3)
    return count_1 *count_3


def part_two():
    inputs = [0] + file_to_list("input_2.txt")
    inputs.sort()
    print(inputs)
    answers = []
    i = 0
    while i < len(inputs):
        if i == len(inputs) - 1:
            print("end")
            break
        answers.append(inputs[i + 1] - inputs[i])
        i += 1
    answers.append(3)
    print(answers)
    count = 0
    i_answers = []
    for j in answers:
        if j == 1:
            count += 1
        else:
            i_answers.append(count)
            count = 0
    print(i_answers)
    ans = 1
    for j in i_answers:
        if j == 2:
            ans = ans * 2
        elif j == 3:
            ans = ans * 4
        elif j == 4:
            ans = ans * 7
    return ans


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
