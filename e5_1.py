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
        # opcode and job
        # opcode always 5 digits
        opcode = str(intcode[pos])
        if len(opcode) < 5:
            opcode = '0' * (5 - len(opcode)) + opcode
        print('pos: ', pos, 'opcode: ', opcode)
        opcode = [int(x) for x in opcode]
        if opcode[3]:
            job = 99
        else:
            job = opcode[4]
        mode1 = opcode[2]
        mode2 = opcode[1]
    # logic
        if job == halt:
            return intcode[0]
        elif job == add:
            if mode1:
                a = intcode[pos + 1]
            else:
                a = intcode[intcode[pos + 1]]
            if mode2:
                b = intcode[pos + 2]
            else:
                b = intcode[intcode[pos + 2]]
            intcode[intcode[pos + 3]] = a + b
            pos += 4
        elif job == multiply:
            if mode1:
                a = intcode[pos + 1]
            else:
                a = intcode[intcode[pos + 1]]
            if mode2:
                b = intcode[pos + 2]
            else:
                b = intcode[intcode[pos + 2]]
            intcode[intcode[pos + 3]] = a * b
            pos += 4
        elif job == inp:
            intcode[intcode[pos + 1]] = int(input('input: '))
            pos += 2
        elif job == out:
            if mode1:
                a = intcode[pos + 1]
            else:
                a = intcode[intcode[pos + 1]]
            print(a)
            pos += 2
        else:
            print('IntcodeError:', job, 'is not a valid opcode.')
            return intcode[0]
        if pos > len(intcode) - 1:
            break

    return intcode[0]


if __name__ == '__main__':
    import time
    start = time.time()
    with open('inputs/5.in') as f:
        intcode = [int(x) for x in f.read().split(',')]

    # for debuging
    #         inp    inp   add         out   multiply    halt
    # intcode = [3, 1, 3, 3, 1, 1, 3, 0, 4, 0, 2, 1, 3, 0, 99]   # return multiplication of inputs
    # intcode = [1002, 4, 3, 0, 33]       # 99, not end properly
    #intcode = [1101, 100, -1, 0]        # 99, end properly
    print(intcode_computer(intcode))

    print('czas: ', time.time() - start)
