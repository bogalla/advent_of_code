import re


def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def bit_mask(val, mask):
    new_val = list(format(int(val), '036b'))
    for key, val in mask.items():
        new_val[key] = val
    num = int(''.join([str(elem) for elem in new_val]), 2)
    return num


def part_one():
    inputs = file_to_list("input.txt")
    ans = dict()
    mask_positions = dict()
    for line in inputs:
        if "mask" in line:
            mask_positions = dict()
            mask = list(line[7:])
            print(mask)
            for inx, val in enumerate(mask):
                if val == "0" or val == "1":
                    mask_positions[inx] = val
        else:
            key, val = re.match(r'^mem\[(.+)] = (.+)$', line).groups()
            ans[key] = bit_mask(val, mask_positions)
    print(ans)
    return sum(ans.values())


if __name__ == '__main__':
    print("final : " + str(part_one()))
    # print("final : " + str(part_two()))
