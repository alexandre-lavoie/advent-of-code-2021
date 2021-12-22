import re
from collections import defaultdict

TASK1_DOMAIN = [(-50,50),(-50,50),(-50,50)]

def intersection(c1, c2):
    cube = []

    for r1, r2 in zip(c1, c2):
        l, r = max(r1[0], r2[0]), min(r1[1], r2[1])
        if l > r: return None
        cube.append((l, r))

    return tuple(cube)

def volume(cube):
    if cube == None:
        return 0

    total = 1

    for l, r in cube:
        total *= r - l + 1

    return total

def main(path):
    lines = open(path).readlines()

    steps = []
    for line in lines:
        state, cube = line.split(" ")
        ranges = [(int(s), int(e)) for s, e in re.findall(r"([-\d]+)..([-\d]+)", cube)]
        steps.append((state == "on", tuple(ranges)))

    regions = defaultdict(int)
    for state, cuboid in steps:
        for region in regions.copy():
            intersect = intersection(region, cuboid)
            if intersect:
                regions[intersect] -= regions[region]
        if state:
            regions[cuboid] = 1

    print("Task 1:", sum(volume(intersection(TASK1_DOMAIN, region)) * count for region, count in regions.items()))
    print("Task 2:", sum(volume(region) * count for region, count in regions.items()))

if __name__ == "__main__":
    main("../input.txt")