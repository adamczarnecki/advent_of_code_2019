def intcode_computer(instructions):
    intcode = instructions[:]
    # opcody:
    hlt = 99
    add = 1
    mut = 2
    inp = 3
    out = 4
    jft = 5
    jif = 6
    lth = 7
    equ = 8
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
            job = int(str(opcode[3]) + str(opcode[4]))  # it could stay = 99 becouse anythig else is error
        else:                                           # but if input data are wrong it stops program
            job = opcode[4]                             # and opcode 98 zatrzyma halts program not rise exeption
        mode1 = opcode[2]
        mode2 = opcode[1]
    # logic
        if job == hlt:
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
        elif job == mut:
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
        elif job == jft:
            if mode1:
                a = intcode[pos + 1]
            else:
                a = intcode[intcode[pos + 1]]
            if mode2:
                b = intcode[pos + 2]
            else:
                b = intcode[intcode[pos + 2]]
            if a:
                pos = b
            else:
                pos += 3
        elif job == jif:
            if mode1:
                a = intcode[pos + 1]
            else:
                a = intcode[intcode[pos + 1]]
            if mode2:
                b = intcode[pos + 2]
            else:
                b = intcode[intcode[pos + 2]]
            if a:
                pos += 3
            else:
                pos = b
        elif job == lth:
            if mode1:
                a = intcode[pos + 1]
            else:
                a = intcode[intcode[pos + 1]]
            if mode2:
                b = intcode[pos + 2]
            else:
                b = intcode[intcode[pos + 2]]
            if a < b:
                intcode[intcode[pos + 3]] = 1
            else:
                intcode[intcode[pos + 3]] = 0
            pos += 4
        elif job == equ:
            if mode1:
                a = intcode[pos + 1]
            else:
                a = intcode[intcode[pos + 1]]
            if mode2:
                b = intcode[pos + 2]
            else:
                b = intcode[intcode[pos + 2]]
            if a == b:
                intcode[intcode[pos + 3]] = 1
            else:
                intcode[intcode[pos + 3]] = 0
            pos += 4
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
    intcode = [3, 1, 3, 3, 1, 1, 3, 0, 4, 0, 2, 1, 3, 0, 99]   # return multiplication of inputs
    intcode = [1002, 4, 3, 0, 33]       # 99, not end properly
    intcode = [1101, 100, -1, 0]        # 99, end properly
    intcode = [3, 21,               # 00 input to intcode[21]
               1008, 21, 8, 20,     # 02 if intcode[21] equal to 8 => intcode[20] = 1 else = 0
               1005, 20, 22,        # 06 if intcode[20] true jump to intcode[22]
               107, 8, 21, 20,      # 09 if if 8 is less than intcode[21] jump to intcode[intcode[20]]
               1006, 20, 31,        # 13 if intcode[20] false jump to intcode[31]
               1106, 0, 36,         # 16 if param false jump to intcode[36]
               98, 0, 0,            # 19 intcode[20] place to store if input == 8, intcode[21] place to store input
               1002, 21, 125, 20,   # 22 multiply intcode[21] and 125 and store intcode[intcode[20]]
               4, 20,               # 26 print intcode[20]
               1105, 1, 46,         # 38 if '1' True jump to intcode[46]
               104, 999,            # 31 print '999'
               1105, 1, 46,         # 33 if '1' True jump to intcode[46]
               1101, 1000, 1, 20,   # 36 add '1000' to '1' and store intcode[intcode[20]]
               4, 20,               # 40 print intcode[20]
               1105, 1, 46,         # 42 if '1' is True jump to intcode[46]
               98,                  # 45 some register, chuj wie
               99]                  # 46 halt
    print(intcode_computer(intcode))

    print('czas: ', time.time() - start)
