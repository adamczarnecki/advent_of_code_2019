def proces_map(map):
    orbits = {}
    for x in map:
        a, b = x.split(')')
        if a not in orbits:
            orbits[a] = []
        orbits[a].append(b)
    return orbits


def count_orbits(list_of_orbits, orbit):
    count = 0
    orbit = list_of_orbits.get(orbit, [])

    for con in orbit:
        count += count_orbits(list_of_orbits, con)
        count += 1
    return count


if __name__ == '__main__':
    with open('inputs/6.in') as f:
        orbit_map = [x.replace('\n', '') for x in f.readlines()]

    # for debugig result 42
    # orbit_map = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']

    orbits = proces_map(orbit_map)
    count = 0
    for orbit in orbits:
        count += count_orbits(orbits, orbit)
    print(count)
