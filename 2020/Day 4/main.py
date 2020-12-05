import re


def file_to_list(filename):
    # for line in file that is split based on \n\n
    # return the line with spaces
    return [line.strip().replace('\n', ' ') for line in open("input.txt").read().split('\n\n')]


def validate_byr(passport):
    if "byr" not in passport:
        return bool(False)
    cut_string = passport[passport.index("byr"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    number = int(cut_string_2[4:])
    if 1920 <= number <= 2002:
        return bool(True)
    return bool(False)


def validate_iyr(passport):
    if "iyr" not in passport:
        return bool(False)
    cut_string = passport[passport.index("iyr"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    number = int(cut_string_2[4:])
    if 2010 <= number <= 2020:
        return bool(True)
    return bool(False)


def validate_eyr(passport):
    if "eyr" not in passport:
        return bool(False)
    cut_string = passport[passport.index("eyr"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    number = int(cut_string_2[4:])
    if 2020 <= number <= 2030:
        return bool(True)
    return bool(False)


def validate_hgt(passport):
    cut_string = passport[passport.index("hgt"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    number = int(cut_string_2[4:len(cut_string_2) - 2])
    if "cm" in cut_string_2:
        if 150 <= number <= 193:
            return bool(True)
    elif "in" in cut_string_2:
        if 59 <= number <= 76:
            return bool(True)
    return bool(False)


def validate_hcl(number):
    x = re.search("^\#[a-zA-Z0-9]{6}$", number)
    if x:
        return bool(True)
    return bool(False)


def validate_ecl(color):
    return color == "grn" or color == "amb" or color == "blu" \
            or color == "hzl" or color == "brn" \
            or color == "gry" or color == "oth"


def validate_pid(number):
    x = re.search("^\d{9}$", number)
    if x:
        return bool(True)
    return bool(False)


def part_two():
    passports = file_to_list('input.txt')
    counter = 0
    for passport in passports:
        details = dict()
        for detail in passport.split():
            x, y = detail.split(":")
            details[x] = y
        details["cid"] = 0
        details.pop("cid")
        print(str(details))
        if len(details) != 7:
            continue
        if validate_byr(details["byr"]) and validate_iyr(details["iyr"]) and validate_eyr(details["eyr"])\
                and validate_hgt(details["hgt"]) and validate_hcl(details["hcl"])\
                and validate_ecl(details["ecl"]) and validate_pid(details["pid"]):
            counter += 1
    return counter


def part_one():
    passports = file_to_list('input.txt')
    counter = 0
    for passport in passports:
        if "byr" in passport and "iyr" in passport and "eyr" in passport \
                and "hgt" in passport and "hcl" in passport \
                and "ecl" in passport and "pid" in passport:
            counter += 1
    return counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
    # print(part_three())
