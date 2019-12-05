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
            intcode[intcode[pos + 3]] = intcode[pos + 1] + intcode[pos + 2]
            pos += 4
        elif job == multiply:
            # print('Pozycja: ', pos, 'zadanie: ', job, 'adres: ', intcode[pos + 1])
            intcode[intcode[pos + 3]] = intcode[pos + 1] * intcode[pos + 2]
            pos += 4
        elif job == inp:
            # print('Pozycja: ', pos, 'zadanie: ', job, 'adres: ', intcode[pos + 1])
            intcode[intcode[pos + 1]] = int(input('input: '))
            pos += 2
        elif job == out:
            # print('Pozycja: ', pos, 'zadanie: ', job, 'adres: ', intcode[pos + 1])
            print(intcode[intcode[pos + 1]])
            pos += 2
        # print('Pozycja: ', pos, 'zadanie: ', job)

    return intcode[0]


if __name__ == '__main__':
    import time
    start = time.time()
    with open('inputs/5.in') as f:
        intcode = [int(x) for x in f.read().split(',')]

    # for debuging
    intcodee = [3, 0, 4, 0, 1, 2, 2, 0, 4, 0, 2, 5, 5, 0, 99]
    print(intcode_computer(intcodee))

    print('czas: ', time.time() - start)
