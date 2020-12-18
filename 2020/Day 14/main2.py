import math

if __name__ == '__main__':

    r = open('input_t.txt', 'r').read()
    input = [x.split(' = ') for x in r.splitlines()]

    mask = ''
    mem = {}
    for line in input:
        print(line)
        if line[0] == 'mask':
            mask = line[1]
        else:
            print("1")
            key = int(line[0][4:-1])
            data = int(line[1])
            floating = []
            target = ''
            for x in range(36):
                print("2")
                next = mask[35 - x]
                if next == '0':
                    next = str(key % 2)
                if next == 'X':
                    floating.append(35 - x)
                target = next + target
                key = key // 2
                print(floating)
            for i in range(0, int(math.pow(2, len(floating)))):
                for index in floating:
                    print("3")
                    target = target[:index] + str(i % 2) + target[index + 1:]
                    i = i // 2
                mem[int(target)] = data

    sum = 0
    for key in mem:
        sum = sum + mem[key]

    print(sum)