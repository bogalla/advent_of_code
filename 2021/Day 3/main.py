def file_to_list(filename):
    file = open(filename, 'r')
    return [line.strip() for line in file]


def part_one(inputs):
    print("pt 1")
    ans = []

    ans = getPlusMinus(inputs)

    gammarate = ''
    for integer in ans:
        if integer > 0:
            gammarate += '0'
        else:
            gammarate += '1'

    epsilonrate = ''
    for integer in ans:
        if integer > 0:
            epsilonrate += '1'
        else:
            epsilonrate += '0'

    gammaint = int(gammarate, 2)
    epsilonint = int(epsilonrate, 2)

    return gammaint*epsilonint

def getPlusMinus(inputs):
    ans = []
    firstrun = True

    for elem in inputs:
        x = list(elem)
        print(x)
        for indx,num in enumerate(x):
            if(firstrun):
                ans.append(0)
            if num == "0":
                ans[indx]+=1
            else:
                ans[indx]-=1
        firstrun = False

    return ans


def getMaxNumbers(arr):
    gammarate = ''
    for integer in arr:
        if integer > 0:
            gammarate += '0'
        else:
            gammarate += '1'
    return gammarate

def getMinNumbers(arr):
    epsilonrate = ''
    for integer in arr:
        if integer > 0:
            epsilonrate += '1'
        else:
            epsilonrate += '0'
    return epsilonrate

def part_two(inputs):
    print("fff")
    arr = getPlusMinus(inputs)

    gammarate = getMaxNumbers(arr)

    epsilonrate = getMinNumbers(arr)

    ogr = inputs
    csr = inputs
    print(arr)
    print(gammarate)
    for pos in range(len(inputs[0])):
        if len(ogr) != 1:
            ogr = list(filter(lambda num: num[pos] == gammarate[pos], ogr))
            print(ogr)
            arr = getPlusMinus(ogr)

            gammarate = getMaxNumbers(arr)


        if len(csr) != 1:
            csr = list(filter(lambda num: num[pos] == epsilonrate[pos], csr))
            arr = getPlusMinus(csr)


            epsilonrate = getMinNumbers(arr)

    oxygenint = int(ogr[0], 2)
    co2int = int(csr[0], 2)

    print(ogr[0])
    print(csr[0])

    return oxygenint*co2int


if __name__ == '__main__':
    inputs = file_to_list("input.txt")
    print(inputs)
    # print("final : " + str(part_one(inputs)))

    print("final : " + str(part_two(inputs)))
