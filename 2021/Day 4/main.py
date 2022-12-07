def file_to_list(filename):
    file = open(filename, 'r')
    bingonumbers = file.readline().strip().split(',')
    boards = {}
    arrofboards = [line.strip() for line in file]

    boardnumber = -1
    for line in arrofboards:
        if(line == ''):
            boardnumber+=1
            boards[boardnumber] = []
        row = filter(lambda x: (x != ''), line.split(" "))

        if (line.split(" ")) != ['']:
            boards[boardnumber].append(list(row))
    return {
        "numbers": bingonumbers,
        "boards": boards
    }

def part_one(inputs):
    for num in inputs["numbers"]:
        for i in inputs["boards"]:
            print("board number " + str(i))
            sum = check_for_bingo(inputs["boards"][i], num)
            print("----------------")
            if sum > 0:
                return sum*int(num)
    return 1

def check_for_bingo(board, num):
    print_board(board)
    print("current number")
    print(num)
    for row in board:
        print("current row")
        print(row)
        print("~~~~~~")

        if num in row: #hit!!

            # print(row)
            i = 0
            for i, entry in enumerate(row):
                if entry == num:
                    row[i] = entry + 'x'
                    break
            print_board(board)
            print("index " + str(i))
            # print(row)
            rowbingo = True
            #check row for bingo
            for entry in row:
                if not "x" in entry:
                    rowbingo = False
            if rowbingo:
                print("BBBBBBIIIINNNGGGOOOO")
                return calculate_board(board)

            #check column for bingo
            columnBingo = True
            for row in board:
                if not "x" in row[i]:
                    columnBingo = False
            if columnBingo:
                print("BBBBBBIIIINNNGGGOOOO")
                return calculate_board(board)
            break
    return 0

def calculate_board(board):
    sum = 0
    for row in board:
        for entry in row:
            if not "x" in entry:
                sum += int(entry)

    return sum

def print_board(board):
    for row in board:
        print(row)

def print_boards(boards):
    for board in boards:
        print_board(boards[board])
        print()

def part_two(inputs):
    has_bingo = []
    for j in range(0, len(inputs["boards"])):
        has_bingo.append(False)
    for num in inputs["numbers"]:
        for i in inputs["boards"]:
            print("board number " + str(i))
            sum = check_for_bingo_2(inputs["boards"][i], num, has_bingo, i)
            print("----------------")
            if sum > 0:
                return sum*int(num)
    return 1


def check_for_bingo_2(board, num, has_bingo, indx):

    print_board(board)
    print("current number")
    print(num)
    for row in board:
        print("current row")
        print(row)
        print("~~~~~~")

        if num in row: #hit!!

            # print(row)
            i = 0
            for i, entry in enumerate(row):
                if entry == num:
                    row[i] = entry + 'x'
                    break
            print_board(board)
            print("index " + str(i))
            # print(row)
            rowbingo = True
            #check row for bingo
            for entry in row:
                if not "x" in entry:
                    rowbingo = False
            if rowbingo:
                print("BBBBBBIIIINNNGGGOOOO")

                if is_final_board(has_bingo):
                    return calculate_board(board)
                has_bingo[indx] = True
            else:
                #check column for bingo
                columnBingo = True
                for row in board:
                    if not "x" in row[i]:
                        columnBingo = False
                if columnBingo:
                    print("BBBBBBIIIINNNGGGOOOO")

                    if is_final_board(has_bingo):
                        return calculate_board(board)
                    has_bingo[indx] = True
            break
    return 0

def is_final_board(has_bingo):
    sum = 0

    for entry in has_bingo:
        if not entry:
            sum +=1

    print(sum)
    if sum == 1:
        return True
    return False

if __name__ == '__main__':
    inputs = file_to_list("input.txt")
    print(inputs)
    print(inputs["boards"])
    # print("final part 1 : " + str(part_one(inputs)))

    print("final : " + str(part_two(inputs)))
