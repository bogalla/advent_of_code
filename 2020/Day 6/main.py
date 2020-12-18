def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip().replace('\n', ' ') for line in open("input.txt").read().split('\n\n')]
    # good_list = []
    # for line in file:
    #     for letter in line.strip():
    #         good_list.append(letter)
    # return good_list


def split(word):
    return [char for char in word]


def part_one():
    entries = file_to_list("input.txt")
    print(entries)
    counter = 0
    for entry in entries:
        no_spaces = entry.replace(" ", "")
        letter_list = split(no_spaces)
        print("-------------------------")
        print(letter_list)
        mylist = list(dict.fromkeys(letter_list))
        print(mylist)
        print("-------------------------")

        counter += len(mylist)
    return counter


def part_two():
    entries = file_to_list("input.txt")
    print(entries)
    count = 0
    for group in entries:
        persons = group.split(" ")
        print(persons)
        hashmap = dict()
        for person in persons:
            i = 0
            # print(person)
            while i < len(person):
                if person[i] in hashmap:
                    # print(person[i]+ " exists in hashmap")
                    hashmap[person[i]] += 1
                else:
                    # print(person[i]+ " does not exists in hashmap")
                    hashmap[person[i]] = 1
                i += 1
        print(hashmap)
        j = 0
        for value in hashmap:
            if hashmap[value] == len(persons):
                count += 1
        print("-----------------------")
    return count



if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))

