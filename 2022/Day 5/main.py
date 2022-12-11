import re

def file_to_list(filename):
    file = open(filename, 'r')
    return [line for line in file]

def part_one():
    inputs = file_to_list("input.txt")
    print(inputs)
    stacks_e, i = get_stacks(inputs)
    print(stacks_e)
    stacks = populate_stack(inputs, stacks_e, i)
    print(inputs[i+2:])
    for x in inputs[i+2:]:
        orders = re.findall(r'\b\d+\b', x)
        print(orders)
        for y in range(int(orders[0])):
            temp = stacks[int(orders[1])-1].pop()
            stacks[int(orders[2])-1].append(temp)
            print(stacks)

    ans = ""
    for stack in stacks:
        ans += stack.pop()
    return ans

def populate_stack(inputs, stacks, i):
    print(i)
    cutlists = inputs[:i]
    cutlists.reverse()
    # print(cutlists)
    for line in cutlists:
        count = 0
        for charIndex in (range(1, len(line), 4)):
            # print(line[charIndex], charIndex)
            if line[charIndex] != " ":
                stacks[count].append(line[charIndex])
            count+=1
    print(stacks)
    return stacks

def get_stacks(inputs):
    stackline = ""
    index = 0
    for i, line in enumerate(inputs):
        if line.startswith(" 1"):
            stackline = line
            index = i
            break
    nospacestackline = stackline.replace(" ", "")
    stacks = []
    for inst in nospacestackline.strip():
        stacks.append([])
    return stacks, index


def part_two():
    inputs = file_to_list("input.txt")
    print(inputs)
    stacks_e, i = get_stacks(inputs)
    print(stacks_e)
    stacks = populate_stack(inputs, stacks_e, i)
    print(inputs[i + 2:])
    for x in inputs[i + 2:]:
        orders = re.findall(r'\b\d+\b', x)
        # print(orders) # move 1 from 2 to 3
        group = []
        for y in range(int(orders[0])): # for y in move 3
            temp = stacks[int(orders[1]) - 1].pop() # take 3 from second num
            group.append(temp)
        print("group", group)
        # print(stacks[int(orders[2]) - 1] + group)
        group.reverse()
        stacks[int(orders[2]) - 1] = stacks[int(orders[2]) - 1] + group
        print((stacks))

    ans = ""
    for stack in stacks:
        ans += stack.pop()
    return ans


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
