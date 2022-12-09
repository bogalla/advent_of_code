def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]

# rock = A, X, 1 point. paper = B, Y, 2 points. scissors = C, Z, 3 points.
def part_one():
    inputs = file_to_list("input.txt")
    print(inputs)

    return 0

# rock = A, 1 point. paper = B, 2 points. scissors = C, 3 points. X = lose. Y = draw. Z = win
def part_two():
    inputs = file_to_list("input.txt")
    print(inputs)
    ans = []
    triple = []
    for ruck in inputs:
        triple.append(ruck)
        if len(triple) == 3:
            print(triple)
            for letter in triple[0]:
                if letter in triple[1] and letter in triple[2]:
                    ans.append(letter)
                    break
            triple = []

    sum = 0
    for letter in ans:
        sum += letter_to_priority(letter)
    return sum


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
