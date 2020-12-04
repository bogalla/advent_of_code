import re


def file_to_list(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    real_lines = []
    passport = ""
    i = 0
    # print('length: ' + str(len(lines)))
    while i < len(lines):
        # print(repr(lines[i]))
        # print(i)
        passport = passport + lines[i]
        if lines[i] == "\n":
            # print("blank line")
            passport = ''
        elif i == len(lines)-1:
            real_lines.append(passport)
            break
        elif lines[i+1] == "\n":
            # print("last line")
            real_lines.append(passport)
        i += 1
    # print(real_lines)
    return real_lines


def validate_byr(passport):
    # print(passport)
    if "byr" not in passport:
        return bool(False)
    cut_string = passport[passport.index("byr"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    # print("cut ====  " + cut_string_2)
    number = int(cut_string_2[4:])
    # print(number)
    if 1920 <= number <= 2002:
        return bool(True)
    print("INVALID ----- " + cut_string_2)
    return bool(False)


def validate_iyr(passport):
    # print(passport)
    if "iyr" not in passport:
        return bool(False)
    cut_string = passport[passport.index("iyr"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    # print("cut ====  " + cut_string_2)
    number = int(cut_string_2[4:])
    # print(number)
    if 2010 <= number <= 2020:
        return bool(True)
    print("INVALID ----- " + cut_string_2)
    return bool(False)


def validate_eyr(passport):
    # print("eyr === " + passport)
    if "eyr" not in passport:
        return bool(False)
    cut_string = passport[passport.index("eyr"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    # print("cut ====  " + cut_string_2)
    number = int(cut_string_2[4:])
    # print(number)
    if 2020 <= number <= 2030:
        return bool(True)
    print("INVALID ----- " + cut_string_2)
    return bool(False)


def validate_hgt(passport):
    # print(repr(passport))
    if "hgt" not in passport:
        return bool(False)
    cut_string = passport[passport.index("hgt"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    # print("cut ====  " + cut_string_2)
    number = int(cut_string_2[4:len(cut_string_2) - 2])
    # print(number)
    if "cm" in cut_string_2:
        if 150 <=  number <= 193:
            return bool(True)
    elif "in" in cut_string_2:
        if 59 <=  number <= 76:
            return bool(True)
    print("INVALID ----- " + cut_string_2)
    return bool(False)


def validate_hcl(passport):
    # print("eyr === " + passport)
    if "hcl" not in passport:
        return bool(False)
    cut_string = passport[passport.index("hcl"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    # print("cut ====  " + cut_string_2)
    number = cut_string_2[4:]
    # print(number)
    x = re.search("^\#[a-zA-Z0-9]{6}$", number)
    if x:
        return bool(True)
    print("INVALID ----- " + cut_string_2)
    return bool(False)


def validate_ecl(passport):
    # print("eyr === " + passport)
    if "ecl" not in passport:
        return bool(False)
    cut_string = passport[passport.index("ecl"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    # print("cut ====  " + cut_string_2)
    color = cut_string_2[4:]
    if color == "grn" or color == "amb" or color == "blu" or color == "hzl" or color == "brn" or color == "gry" or color == "oth":
        return bool(True)
    print("INVALID ----- " + cut_string_2)
    return bool(False)


def validate_pid(passport):
    # print("eyr === " + passport)
    if "pid" not in passport:
        return bool(False)
    cut_string = passport[passport.index("pid"):]
    cut_string_2 = cut_string[:cut_string.index(" ")]
    # print("cut ====  " + cut_string_2)
    number = cut_string_2[4:]
    # print(number)
    x = re.search("^\d{9}$", number)
    if x:
        return bool(True)
    print("INVALID ----- " + cut_string_2)
    return bool(False)


def part_one():
    passports_newline = file_to_list('input.txt')
    passports = []
    for passport in passports_newline:
        passports.append(passport.replace("\n", " ") + " ")
    counter = 0
    for passport in passports:
        if validate_byr(passport) and validate_iyr(passport) and validate_eyr(passport)\
                and validate_hgt(passport) and validate_hcl(passport)\
                and validate_ecl(passport) and validate_pid(passport):
            counter += 1

    return counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("final : " + str(part_one()))
    # print(part_two())
    # print(part_three())
