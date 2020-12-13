import re


def main():
    # Turn input into a dictionary like:
    # {
    #   'shiny gold': [(2, 'dark red')],
    #   'dark red': [(2, 'orange'), (1, 'red')]
    # }
    hashmap = dict()
    with open('test_input.txt', 'r') as file:
        for line in file:
            # print("line : " + line)
            parent, kids = re.match(r'^(.+?) bags contain (.+)\.$', line).groups()
            # groups() returns a tuple () of the matches that are in the brackets of the match
            kids = [re.match(r'(\d+) (.+) bags?', word).groups() for word in kids.split(', ') if word != 'no other bags']
            kids = [(int(num), c) for num, c in kids]
            hashmap[parent] = kids

    print(hashmap)
    # Part 1 - How many colours eventually have "shiny gold" inside?
    for key in hashmap.keys():
        print("===== ")
        print(colors_inside(key, hashmap))
    print("Part 1:", sum(['shiny gold' in colors_inside(key, hashmap) for key in hashmap.keys()]))

    # Part 2 - How many bags are inside shiny gold?
    print("Part 2:", bags_inside('shiny gold', hashmap))


def colors_inside(key, hashmap):
    print("key : " + key)
    """Returns a set of colours that are eventually inside the color"""
    answer_set = set()
    for num, value in hashmap[key]:
        answer_set.add(value)
        answer_set.update(colors_inside(value, hashmap))
    return answer_set


def bags_inside(color, colors):
    """Returns the number of bags inside a given color"""
    return sum([n + n * bags_inside(c, colors) for n, c in colors[color]])


if __name__ == '__main__':
    main()