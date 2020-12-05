import re

if __name__ == '__main__':
    part1 = 0
    part2 = 0

    inputs = [line.strip().replace('\n', ' ') for line in open("input.txt").read().split('\n\n')]
    print("1 : " + str(inputs))
    for passport in inputs:
        details = dict()
        for detail in passport.split():
            key, value = detail.split(":")
            details[key] = value
        details["cid"] = 0
        details.pop("cid")
        if len(details) == 7:
            part1 += 1
        else:
            # doesnt have all the correct things, pass. not good for part 1 or 2
            continue
        byr = int(details['byr'])
        iyr = int(details['iyr'])
        eyr = int(details['eyr'])
        hgt = details['hgt']
        hcl = details['hcl']
        ecl = details['ecl']
        pid = details['pid']
        if (1920 <= byr <= 2002 and 2010 <= iyr <= 2020 and 2020 <= eyr <= 2030 and ('cm' in hgt or 'in' in hgt) and
                (('cm' in hgt and 150 <= int(hgt[:-2]) <= 193) or ('in' in hgt and 59 <= int(hgt[:-2]) <= 76)) and
                re.fullmatch(r'#[0-9a-f]{6}', hcl) and re.fullmatch(r'[0-9]{9}', pid) and
                ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            part2 += 1

    print(part1)
    print(part2)
