def proces_map(map):
    """ teraz sprawdzamy jednocześnie w jedną i w drugą """
    orbits = {}
    for x in map:
        a, b = x.split(')')
        if a not in orbits:
            orbits[a] = []
        orbits[a].append(b)
        if b not in orbits:
            orbits[b] = []
        orbits[b].append(a)
    return orbits


def find_distance(orbist, start, goal):
    from collections import deque
    distances = {}
    current = deque()
    current.append((start, 0))      # starting object
    while current:
        x, d = current.popleft()    # wyciągamy aktualny obiejkt i dystans do niego
        if x in distances:
            continue                # jeśli już jest to po co go robić
        distances[x] = d
        for y in orbist[x]:
            current.append((y, d + 1))
    return distances[goal] - 2      # odejmujemy dwa bo interesuje nas dystans pomiędzy, bez start i goal


if __name__ == '__main__':
    with open('inputs/6.in') as f:
        orbit_map = [x.replace('\n', '') for x in f.readlines()]

    # for debugig result 4
    # orbit_map = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']

    orbits = proces_map(orbit_map)
    print(find_distance(orbits, 'YOU', 'SAN'))
