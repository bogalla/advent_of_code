def file_to_list(filename):
    file = open(filename, 'r')
    return [int(line.strip()) for line in file]


def part_one():
    inputs = file_to_list("input.txt")
    print(input)
    start = 0
    pointer = 26
    while pointer < len(inputs):
        if not find_sum(inputs, start, pointer):
            return inputs[pointer]
        start += 1
        pointer += 1


def part_two():
    inputs = file_to_list("input.txt")
    sum_goal = 20874512
    i = 0
    answer_list = []
    while i < len(inputs):
        print(inputs[i])
        counter = 0
        j = i
        answer_list = []
        while j < len(inputs):
            answer_list.append(inputs[j])
            print(answer_list)
            counter += inputs[j]
            if counter == sum_goal:
                print(str(inputs[i]) + " + " + str(inputs[j]))
                return answer_list
            elif counter > sum_goal:
                break
            j += 1
        i += 1
    return answer_list[0] + answer_list[len(answer_list)-1]


def find_sum(inputs, start, goal):
    i = start
    while i < goal:
        j = start
        while j < goal:
            print("i = " + str(inputs[i]))
            print("j = " + str(inputs[j]))
            if i != j:
                if inputs[i] + inputs[j] == inputs[goal]:
                    print("found sum : " + str(inputs[i]) + " and " + str(inputs[j]) + " equal " + str(inputs[goal]))
                    return bool(True)
            else:
                print("skip")
            j += 1
        i += 1
    return bool(False)


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    answer_list = part_two()
    print(answer_list)
    print("-----" + str(max(answer_list) + min(answer_list)))
