def file_to_list(filename):
    file = open(filename, 'r')
    listy = [line.strip() for line in file]
    newList = []
    for x in listy:
        newList.append([x[0], x[2]])
    return newList

# rock = A, X, 1 point. paper = B, Y, 2 points. scissors = C, Z, 3 points.
def part_one():
    inputs = file_to_list("input.txt")
    print(inputs)
    score = 0
    for tup in inputs:
        print(tup[0])
        if tup[0] == "A": #rock
            if tup[1] == "X": #rock
                score+=3
                score+=1
            elif tup[1] =="Y": #paper
                score+=6
                score+=2
            elif tup[1] == "Z": #scissors
                score+=0
                score+=3
        elif tup[0] == "B": #paper
            if tup[1] == "X": #rock
                score+=0
                score+=1
            if tup[1] == "Y": #paper
                score+=3
                score+=2
            if tup[1] == "Z": #scissors
                score+=6
                score+=3
        elif tup[0] == "C": #scissors
            if tup[1] == "X": #rock
                score+=6
                score+=1
            if tup[1] == "Y": #paper
                score+=0
                score+=2
            if tup[1] == "Z": #scissors
                score+=3
                score+=3
    return score

# rock = A, 1 point. paper = B, 2 points. scissors = C, 3 points. X = lose. Y = draw. Z = win
def part_two():
    inputs = file_to_list("input.txt")
    print(inputs)
    score = 0
    for tup in inputs:
        print(tup[0])
        if tup[0] == "A": #rock
            if tup[1] == "X": #scissors, lose
                score+=0
                score+=3
            elif tup[1] =="Y": #rock, draw
                score+=3
                score+=1
            elif tup[1] == "Z": #paper, win
                score+=6
                score+=2
        elif tup[0] == "B": #paper
            if tup[1] == "X": #lose, rock
                score+=0
                score+=1
            if tup[1] == "Y": #draw, paper
                score+=3
                score+=2
            if tup[1] == "Z": #win, scissors
                score+=6
                score+=3
        elif tup[0] == "C": #scissors
            if tup[1] == "X": #lose, paper
                score+=0
                score+=2
            if tup[1] == "Y": #draw, scissors
                score+=3
                score+=3
            if tup[1] == "Z": #win rock
                score+=6
                score+=1
    return score

if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
