import re


def file_to_list(filename):
    # for line in file that is split based on \n\n
    # return the line with spaces
    return [line.strip().replace('\n', ' ') for line in open("input.txt").read().split('\n\n')]


def validate_byr(number):
    return 1920 <= number <= 2002


def validate_iyr(number):
    return 2010 <= number <= 2020


def validate_eyr(number):
    return 2020 <= number <= 2030


def validate_hgt(passport):
    height = int(passport[:len(passport)-2])
    if "cm" in passport:
        if 150 <= height <= 193:
            return bool(True)
    elif "in" in passport:
        if 59 <= height <= 76:
            return bool(True)
    return bool(False)


def validate_hcl(number):
    return re.search("^\#[a-zA-Z0-9]{6}$", number)


def validate_ecl(color):
    return color == "grn" or color == "amb" or color == "blu" \
            or color == "hzl" or color == "brn" \
            or color == "gry" or color == "oth"


def validate_pid(number):
    return re.search("^\d{9}$", number)


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
        # print(str(details))
        if len(details) != 7:
            continue
        if validate_byr(int(details["byr"])) and validate_iyr(int(details["iyr"])) and validate_eyr(int(details["eyr"]))\
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
    print("final : " + str(part_one()))
    print("final : " + str(part_two()))
    # print(part_three())
