def get_steps_to_point(cable):
    positions = []
    pos = [0, 0]
    count = 0
    for move in cable:
        direction = move[0]
        way = int(move[1:])
        if direction == 'R':
            for _ in range(way):
                count += 1
                pos[1] += 1
                positions.append([tuple(pos), count])
        if direction == 'L':
            for _ in range(way):
                count += 1
                pos[1] -= 1
                positions.append([tuple(pos), count])
        if direction == 'U':
            for _ in range(way):
                count += 1
                pos[0] += 1
                positions.append([tuple(pos), count])
        if direction == 'D':
            for _ in range(way):
                count += 1
                pos[0] -= 1
                positions.append([tuple(pos), count])
    return positions


if __name__ == '__main__':
    import time
    start = time.time()
    # original data
    with open('inputs/3.in') as f:
        A, B = f.readlines()
        A, B = [x.split(',') for x in [A, B]]

    # for debbuging (result = 610)
    cable_1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    cable_2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    # for debbuging (result = 410)
    cable_1 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    cable_2 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']

    # geting positions
    positions_1 = get_steps_to_point(A)
    positions_2 = get_steps_to_point(B)
    pos_2 = [x for x, _ in positions_2]

    steps_to_crossings = []
    for position in positions_1:
        look_for = position[0]
        if look_for in pos_2:
            xA = position[1]
            xB = positions_2[pos_2.index(look_for)][1]
            print('can be: ', xA + xB)
            steps_to_crossings.append(xA + xB)

    print('ta kurwa to odpowiedz:')
    print(min(steps_to_crossings))
    print('mam nadzieje')
    print('czas: ', time.time() - start)
