import math


def find_farthest_orbit(orbits):
    s_orbits = list(map(lambda x: x[0] * x[1] if not x[0] == x[1] else - 1, orbits))
    max_indx = s_orbits.index(max(s_orbits))
    return orbits[max_indx]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

# print(find_farthest_orbit(orbits))
