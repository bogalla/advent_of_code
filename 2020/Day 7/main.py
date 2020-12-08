from anytree import Node, RenderTree


  # List to keep track of visited nodes.
queue = []


def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def part_one():
    input_list = file_to_list("input.txt")
    hashmap = dict()
    for line in input_list:
        line_spaced = line.split(" ")
        print(line_spaced)
        parent = line_spaced[0] + line_spaced[1] + line_spaced[2][:-1]
        print("parent : " + parent)
        i = 5
        child_list = []
        while i < len(line_spaced):
            if line_spaced[i] == "other":
                child = str("")
            else:
                child = remove_s(line_spaced[i] + line_spaced[i + 1] + line_spaced[i + 2][:-1])
            print("child : " + str(child))
            if child != "":
                child_list.append(child)
            i += 4
        hashmap[parent] = child_list
    final_num = sum(['shinygoldbag' in recursive_search(key, hashmap) for key in hashmap.keys()])
    print(hashmap)
    return final_num


def remove_s(word):
    if word[-1:] == "s":
        return word[:-1]
    return word


def recursive_search(key, hashmap):
    answer_set = set()
    for value in hashmap[key]:
        answer_set.add(value)
        answer_set.update(recursive_search(value,hashmap))
    return answer_set


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
