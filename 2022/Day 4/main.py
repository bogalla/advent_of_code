def file_to_list(filename):
    file = open(filename, 'r')
    listy = [line.strip() for line in file]
    print(listy)
    ans = []
    for unit in listy:
        index0 = unit.rfind(",")
        firstgroup = unit[0: index0]
        secondgroup = unit[index0+1: len(unit)]

        # print(firstgroup, secondgroup)
        index1 = firstgroup.rfind("-")
        one = firstgroup[0: index1]
        two = firstgroup[index1+1: len(firstgroup)]

        index2 = secondgroup.rfind("-")
        three = secondgroup[0: index2]
        four = secondgroup[index2+1: len(secondgroup)]
        print(one, two, three, four)
        ans.append([[one, two], [three, four]])
    return ans
def file_to_list2(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]

# if one num is <= three and two is >= four, OR if three <= one and four >= 2 then one
# pair encapsulates the other
def part_one():
    inputs = file_to_list("input.txt")
    print(inputs)
    counter = 0
    for pair in inputs:
        a = int(pair[0][0])
        b = int(pair[0][1])
        c = int(pair[1][0])
        d = int(pair[1][1])
        print(a, b, c, d)
        if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):
            counter+=1
            print(pair)
            print("--------one-------------------")

    return counter

# a and b are less than c or and b are greater than d
def part_two():
    inputs = file_to_list("input.txt")
    print(inputs)
    counter = 0
    for pair in inputs:
        a = int(pair[0][0])
        b = int(pair[0][1])
        c = int(pair[1][0])
        d = int(pair[1][1])
        print(a, b, c, d)
        if (a < c and b < c):
            print(pair)
            print("--------one-------------------")
        elif (a > d and b > d):
            print(pair)
            print("--------two-------------------")
        else:
            counter+=1
    return counter


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
