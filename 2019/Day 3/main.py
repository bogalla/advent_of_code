import numpy as np


def file_to_list(filename):
    file = open(filename, 'r')
    number_list = []
    for x in file:
        number_list.append(str(x))
    return number_list


def line_to_words(list_of_orders):
    orders = []
    for word in list_of_orders.split(','):
        orders.append(str(word))
    return orders


def get_increment(order):
    if "\n" in order:
        return int(order[1:len(order)-1])
    else:
        return int(order[1:len(order)])


def calculate_path(wire_orders):
    cartesian_coords = {(0, 0)}
    current_position = (0, 0)
    for order in wire_orders:
        increment = get_increment(order)
        if order[0] == 'U':
            i = 0
            while i < increment:
                cartesian_coords.add(current_position)
                current_position = (current_position[0], current_position[1] + 1)
                i += 1
        elif order[0] == 'D':
            i = 0
            while i < increment:
                cartesian_coords.add(current_position)
                current_position = (current_position[0], current_position[1] - 1)
                i += 1
        elif order[0] == 'R':
            i = 0
            while i < increment:
                cartesian_coords.add(current_position)
                current_position = (current_position[0] + 1, current_position[1])
                i += 1
        elif order[0] == 'L':
            i = 0
            while i < increment:
                cartesian_coords.add(current_position)
                current_position = (current_position[0] - 1, current_position[1])
                i += 1
    return cartesian_coords


def find_same_coordinates(list_wire_one, list_wire_two):
    set_of_coordinates = list_wire_one.intersection(list_wire_two)
    return set_of_coordinates


def find_closest_to_origin(same_coordinate_list):
    minimum = 10000000000000000000
    for coord in same_coordinate_list:
        entry = abs(coord[0]) + abs(coord[1])
        if entry < minimum and entry != 0:
            minimum = entry
    return minimum


def part_one():
    numbers = file_to_list('input.txt')
    first_wire_orders = line_to_words(numbers[0])
    second_wire_orders = line_to_words(numbers[1])
    list_wire_one = calculate_path(first_wire_orders)
    list_wire_two = calculate_path(second_wire_orders)
    same_coordinate_list = find_same_coordinates(list_wire_one, list_wire_two)
    return find_closest_to_origin(same_coordinate_list)


def calculate_path_part_two(wire_orders):
    cartesian_coords = dict()
    current_position = (0, 0)
    steps = 0
    for order in wire_orders:
        increment = get_increment(order)
        if order[0] == 'U':
            i = 0
            # print('U')
            while i < increment:
                cartesian_coords[current_position] = steps
                current_position = (current_position[0], current_position[1] + 1)
                i += 1
                steps += 1
                print(current_position)
        elif order[0] == 'D':
            i = 0
            # print('D')
            while i < increment:
                cartesian_coords[current_position] = steps
                current_position = (current_position[0], current_position[1] - 1)
                i += 1
                steps += 1
                print(current_position)
        elif order[0] == 'R':
            i = 0
            # print('R')
            while i < increment:
                cartesian_coords[current_position] = steps
                current_position = (current_position[0] + 1, current_position[1])
                i += 1
                steps += 1
                print(current_position)
        elif order[0] == 'L':
            i = 0
            # print('L')
            while i < increment:
                cartesian_coords[current_position] = steps
                current_position = (current_position[0] - 1, current_position[1])
                i += 1
                steps += 1
                print(current_position)
    print(cartesian_coords)
    return cartesian_coords


def find_same_coordinates_part_two(list_wire_one, list_wire_two):
    list_of_steps = []
    for key in list_wire_one:
        if key in list_wire_two:
            total_steps = list_wire_two[key] + list_wire_one[key]
            print(total_steps)
            list_of_steps.append(total_steps)
    return list_of_steps


def find_minimum(list):
    minimum = 100000000000
    for entry in list:
        if entry < minimum and entry != 0:
            minimum = entry
    return minimum


def part_two():
    numbers = file_to_list('input.txt')
    first_wire_orders = line_to_words(numbers[0])
    second_wire_orders = line_to_words(numbers[1])
    list_wire_one = calculate_path_part_two(first_wire_orders)
    list_wire_two = calculate_path_part_two(second_wire_orders)
    same_coordinate_list = find_same_coordinates_part_two(list_wire_one, list_wire_two)
    return find_minimum(same_coordinate_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(part_one())
    print("final: " + str(part_two()))
