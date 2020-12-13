def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def count_adjacent(grid, row, seat):
    directions = [(-1, -1), (-1, 1), (-1, 0), (1, -1), (1, 1), (1, 0), (0, 1), (0, -1)]
    count = 0
    for dif in directions:
        position = (row + dif[0], seat + dif[1])
        if 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]):
            try:
                count += 1 if grid[position[0]][position[1]] == "#" else 0
            except IndexError:
                print(position)
                raise
    return count


def make_new_grid(grid):
    new_grid = []
    i = 0
    while i < len(grid):
        row = i
        line = grid[i]
        new_line = ""
        j = 0
        while j < len(line):
            char = line[j]
            new_char = char
            seat = j
            count = count_adjacent(grid, row, seat) if char != "." else 0
            if char == "L" and count == 0:
                new_char = "#"
            elif char == "#" and count >= 4:
                new_char = "L"
            new_line += new_char
            j += 1
        new_grid.append(new_line)
        i += 1
    return new_grid


def count_occupied(grid):
    count = 0
    for line in grid:
        for char in line:
            if char == "#":
                count += 1
    return count


def part_one():
    old_grid = file_to_list("input.txt")
    while bool(True):
        new_grid = make_new_grid(old_grid)
        for line in new_grid:
            print(line)
        if new_grid == old_grid:
            break
        old_grid = new_grid
        print("-----------------------------")
    return count_occupied(new_grid)


def count_visible(grid, row, seat):
    directions = [(-1, -1), (-1, 1), (-1, 0), (1, -1), (1, 1), (1, 0), (0, 1), (0, -1)]
    count = 0
    for dif in directions:
        found = False
        multiplier = 1
        while not found:
            x, y = (row + (multiplier * dif[0]), seat + (multiplier * dif[1]))
            # print("x : " + str(x))
            # print("y : " + str(y))
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                # print(grid[x][y])
                if grid[x][y] == "#":
                    count += 1
                    found = True
                elif grid[x][y] == "L":
                    found = True
                else:
                    multiplier += 1
            else:
                found = True
    return count


def make_new_grid_2(grid):
    new_grid = []
    i = 0
    while i < len(grid):
        row = i
        line = grid[i]
        new_line = ""
        j = 0
        while j < len(line):
            char = line[j]
            new_char = char
            seat = j
            count = count_visible(grid, row, seat) if char != "." else 0
            if char == "L" and count == 0:
                new_char = "#"
            elif char == "#" and count >= 5:
                new_char = "L"
            new_line += new_char
            j += 1
        new_grid.append(new_line)
        i += 1
    return new_grid


def part_two():
    old_grid = file_to_list("input.txt")
    while bool(True):
        new_grid = make_new_grid_2(old_grid)
        for line in new_grid:
            print(line)
        if new_grid == old_grid:
            break
        old_grid = new_grid
    return count_occupied(new_grid)


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
