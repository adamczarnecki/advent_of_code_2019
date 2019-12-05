def intcode_computer(instructions):
    intcode = instructions[:]
    # opcody:
    halt = 99
    add = 1
    multiply = 2
    for pos in range(0, len(intcode), 4):
        # adresy:
        job = intcode[pos]
        a = intcode[intcode[pos + 1]]
        b = intcode[intcode[pos + 2]]
        res_pos = intcode[pos + 3]
        # logika:
        if job == halt:
            return intcode[0]
        elif job == add:
            intcode[res_pos] = a + b
        elif job == multiply:
            intcode[res_pos] = a * b
        # print('Pozycja: ', pos, 'zadanie: ', job, 'A:', a, 'B:', b, 'Adres zapisu: ', res_pos)

    return intcode[0]


if __name__ == '__main__':
    import time
    start = time.time()
    with open('inputs/5.in') as f:
        intcode = f.read().split(',')
    for i, x in enumerate(intcode):
        intcode[i] = int(x)

    print('czas: ', time.time() - start)
