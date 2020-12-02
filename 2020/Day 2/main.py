# this is day 1
def part_one():
    valid_entries = 0
    for i in numbers:
        entry = str(i)
        dash_index = entry.index('-')
        space_index = entry.index(' ')
        colon_index = entry.index(':')
        first_num = entry[0:dash_index]
        second_num = entry[dash_index+1: space_index]
        special_letter = entry[space_index+1:colon_index]
        string_to_examine = entry[colon_index+2:]
        counter = 0
        for letter in string_to_examine:
            if letter == special_letter:
                counter += 1
        if counter >= int(first_num) and counter <= int(second_num):
            valid_entries += 1
    return valid_entries


def part_two():
    valid_entries = 0
    for i in numbers:
        entry = str(i)
        dash_index = entry.index('-')
        space_index = entry.index(' ')
        colon_index = entry.index(':')
        first_num = entry[0:dash_index]
        second_num = entry[dash_index+1: space_index]
        special_letter = entry[space_index+1:colon_index]
        string_to_examine = entry[colon_index+2:]
        if string_to_examine[int(first_num)-1] == special_letter or string_to_examine[int(second_num)-1] == special_letter:
            if string_to_examine[int(first_num)-1] == special_letter and string_to_examine[int(second_num)-1] == special_letter:
                print("")
            else:
                valid_entries += 1
    return valid_entries


def file_to_list(filename):
    file = open(filename, 'r')
    number_list = []
    for x in file:
        number_list.append(str(x))
    return number_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = file_to_list('input.txt')
    # print(part_one())
    print(part_two())
