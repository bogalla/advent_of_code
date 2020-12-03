def file_to_list(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        print(repr(line))
    return lines


def part_one():
    grid = file_to_list('input.txt')
    length_of_grid = len(grid[0]) - 1
    i = 1
    counter = 0
    pointer = 0
    while i < len(grid):
        pointer = (pointer + 3) % length_of_grid
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
        counter = 0
        right = list_of_increases[j][0]
        down = list_of_increases[j][1]
        i = down
        pointer = 0
        while i < len(grid):
            pointer = (pointer + right) % length_of_grid
            if grid[i][pointer] == '#':
                counter += 1
            i += down
        answer_list.append(counter)
        j += 1
    return multiply(answer_list)


def multiply(answer_list):
    counter = 1
    for num in answer_list:
        counter = counter * num
    return counter


def part_three():
    lines = file_to_list('input.txt')

    x = 0
    y = 0
    count = 0
    length = len(lines[322])
    print("length: " + str(len(lines)))
    print("length: " + str(length))
    # part 1
    while y < len(lines):
        if lines[y][x % (length -1)] == '#':
            count += 1
        x += 3
        y += 1

    print(count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print("final : " + str(part_one()))
    # print(part_two())
    print(part_three())