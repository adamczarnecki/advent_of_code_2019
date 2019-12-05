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
            return intcode[0]
        elif job == add:
            intcode[pos + 3] = intcode[pos + 1] + intcode[pos + 2]
            pos += 4
        elif job == multiply:
            intcode[pos + 3] = intcode[pos + 1] * intcode[pos + 2]
            pos += 4
        elif job == inp:
            intcode[pos + 1] = int(input('input: '))
            pos += 2
        elif job == out:
            print(intcode[pos + 1])
            pos +=2
    # print('Pozycja: ', pos, 'zadanie: ', job, 'A:', a, 'B:', b, 'Adres zapisu: ', res_pos)

    return intcode[0]


if __name__ == '__main__':
    import time
    start = time.time()
    with open('inputs/5.in') as f:
        intcode = [int(x) for x in f.read().split(',')]

    # for debuging
    # intcode = [3, 0, 4, 0, 99]
    print(intcode_computer(intcode))

    print('czas: ', time.time() - start)
