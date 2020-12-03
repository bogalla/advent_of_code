def file_to_list(filename):
    file = open(filename, 'r')
    number_list = []
    for x in file:
        number_list.append(str(x))
    return number_list


def part_one():
    counter = 0
    grid = file_to_list('input.txt')
    length_of_grid = len(grid[0]) - 1
    print(length_of_grid)
    i = 1
    pointer = 0
    while i < len(grid):
        print("----------")
        print(grid[i])
        pointer = (pointer + 3) % length_of_grid
        print(pointer)
        print(grid[i][pointer])
        if grid[i][pointer] == '#':
            counter += 1
        i += 1

    return counter


def part_two():
    list_of_increases = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    answer_list = []
    grid = file_to_list('input.txt')
    length_of_grid = len(grid[0]) - 1
    print(length_of_grid)
    j = 0
    while j < len(list_of_increases):
        print("==================\n\n\n\n\n\n\n=====================")
        counter = 0
        print(list_of_increases[j])
        right = list_of_increases[j][0]
        down = list_of_increases[j][1]
        i = down
        pointer = 0
        while i < len(grid):
            print("----------")
            print(grid[i])
            pointer = (pointer + right) % length_of_grid
            print(pointer)
            print(grid[i][pointer])
            if grid[i][pointer] == '#':
                counter += 1
            i += down
        answer_list.append(counter)
        j += 1
    print(answer_list)
    return multiply(answer_list)


def multiply(answer_list):
    counter = 1
    for num in answer_list:
        counter = counter * num
    return counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print(part_two())