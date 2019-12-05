def intcode_computer(instructions):
    intcode = instructions[:]
    # opcody:
    halt = 99
    add = 1
    multiply = 2
    inp = 3
    out = 4
    # The Loop:
    pos = 0
    while True:
        job = intcode[pos]
        # logika:
        if job == halt:
            # print('Pozycja: ', pos, 'zadanie: ', job)
            return intcode[0]
        elif job == add:
            # print('Pozycja: ', pos, 'zadanie: ', job, 'adres: ', intcode[pos + 1])
            intcode[intcode[pos + 3]] = intcode[intcode[pos + 1]] + intcode[intcode[pos + 2]]
            pos += 4
        elif job == multiply:
            intcode[intcode[pos + 3]] = intcode[intcode[pos + 1]] * intcode[intcode[pos + 2]]
            pos += 4
        elif job == inp:
            intcode[intcode[pos + 1]] = int(input('input: '))
            pos += 2
        elif job == out:
            print(intcode[intcode[pos + 1]])
            pos += 2

    return intcode[0]


if __name__ == '__main__':
    import time
    start = time.time()
    with open('inputs/5.in') as f:
        intcode = [int(x) for x in f.read().split(',')]

    # for debuging
    #         inp    inp   add         out   multiply    halt
    intcode = [3, 1, 3, 3, 1, 1, 3, 0, 4, 0, 2, 1, 3, 0, 99]   # return multiplication of inputs
    print(intcode_computer(intcode))

    print('czas: ', time.time() - start)
