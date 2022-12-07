import bisect
def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]

# sum up the groups of numbers and find the max, return the max
def part_one():
    inputs = file_to_list("input.txt")
    print(inputs)
    counter = 0
    maximum = 0
    for x in inputs:
        if x == '':
            print("space between elves")
            if counter > maximum:
                print("new max! " + str(counter))
                maximum = counter
            counter = 0
            continue
        counter += int(x)
        print("current counter: " + str(counter))
    return maximum

# get top 3 sums and return their sum
def part_two():
    inputs = file_to_list("input.txt")
    print(inputs)
    counter = 0
    sortedList = []
    for x in inputs:
        if x == '':
            print("space between elves")
            bisect.insort(sortedList, counter)
            print(sortedList)
            counter = 0
            continue
        counter += int(x)
        print("current counter: " + str(counter))
    sortedList.reverse()
    return sortedList[0]+sortedList[1]+sortedList[2]

if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
