import re


rules = []  # [[1,3], [5,7]]
near_tickets = []
final = []


def file_to_list():
    global rules
    global near_tickets
    for indx, line in enumerate(open("input_t.txt").read().split('\n\n')):
        for entry in line.split("\n"):
            if indx == 0:
                a, b = re.match(r'^.+: (.+)-(.+) or .+$', entry).groups()
                c, d = re.match(r'^.+ or (.+)-(.+)$', entry).groups()
                rules.append([[int(a), int(b)], [int(c), int(d)]])
            elif indx == 2 and ":" not in entry:
                list_int = [int(x) for x in entry.split(",")]
                near_tickets.append(list_int)
    # print(rules)
    # print(near_tickets)


def number_within_bounds(num):
    global final
    # print(num)
    # print("check to see if " + str(num) + " is in the bounds somewhere")
    for combos in rules:
        # print(combos)
        if combos[0][0] <= num <= combos[0][1] or combos[1][0] <= num <= combos[1][1]:
            return True
    # print(str(num) + " was not in " + str(combos[0]) + " and " + str(combos[1]))
    final.append(num)
    return False


def ticket_within_bounds(ticket):
    for num in ticket:
        # print("num in ticket : " + str(num))
        if not number_within_bounds(num):
            return False
    return True


def part_one():
    file_to_list()
    error_count = 0
    for ticket in near_tickets:
        print("ticket =  " + str(ticket))
        if not ticket_within_bounds(ticket):
            error_count += 1
        print("---------------")
    print(error_count)
    print(final)
    return sum(final)


def part_two():
    file_to_list()
    good_tickets = []
    for ticket in near_tickets:
        # print("ticket =  " + str(ticket))
        if ticket_within_bounds(ticket):
            good_tickets.append(ticket)
        # print("---------------")
    print(good_tickets)
    return 1


if __name__ == '__main__':
    # print("final : " + str(part_one()))
    print("final : " + str(part_two()))
