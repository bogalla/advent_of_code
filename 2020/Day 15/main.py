def file_to_list(filename):
    file = open(filename, 'r')
    return file.readline().strip().split(",")


def part_one():
    inputs = file_to_list("input.txt")
    # print(inputs)
    ans = dict()
    for inx, val in enumerate(inputs[:-1]):
        ans[int(val)] = inx + 1
    # print(ans)
    current_num = int(inputs[-1])
    for i in range(len(inputs), 30000001):
        # print("index = " + str(i) + ", " + str(current_num))
        # print("current ans = " + str(ans))
        if i == 30000000:
            return current_num
        if current_num in ans.keys():
            last_turn = ans[current_num]
            # print("last turn this existed: " + str(last_turn))
            diff = i - last_turn
            # print("difference =  " + str(diff))
            ans[current_num] = i
            current_num = diff
        else:
            # first time getting this number
            ans[current_num] = i
            current_num = 0
        # print("----------------------------")


if __name__ == '__main__':
    print("final : " + str(part_one()))
    # print("final : " + str(part_two()))
