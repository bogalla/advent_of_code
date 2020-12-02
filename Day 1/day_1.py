# this is day 1

def find_answer(filename):
    file = open(filename, 'r')
    numbers = []
    for x in file:
        numbers.append(int(x))
    print(numbers)
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    return i*j*k


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(find_answer('input.txt'))