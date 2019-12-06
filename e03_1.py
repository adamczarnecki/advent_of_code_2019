def get_positions(cable):
    positions = set()
    pos = [0, 0]
    for move in cable:
        direction = move[0]
        way = int(move[1:])
        if direction == 'R':
            for _ in range(way):
                pos[1] += 1
                positions.add(tuple(pos))
        if direction == 'L':
            for _ in range(way):
                pos[1] -= 1
                positions.add(tuple(pos))
        if direction == 'U':
            for _ in range(way):
                pos[0] += 1
                positions.add(tuple(pos))
        if direction == 'D':
            for _ in range(way):
                pos[0] -= 1
                positions.add(tuple(pos))
    return positions


if __name__ == '__main__':
    # original data
    with open('inputs/3.in') as f:
        A, B = f.readlines()
        A, B = [x.split(',') for x in [A, B]]

    # for debbuging (result = 159)
    cable_1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    cable_2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

    # geting positions
    positions_1 = get_positions(A)
    positions_2 = get_positions(B)

    # finding common positions(intersection)
    common = positions_1.intersection(positions_2)

    # finding the lowest sum (closed to 0)
    print(min([abs(x) + abs(y) for x, y in common]))
