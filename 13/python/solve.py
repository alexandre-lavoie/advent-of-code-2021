dots = set()
folds = []

with open("../input.txt") as h:
    for line in h.readlines():
        line = line.strip()

        if "," in line:
            dots.add(tuple(int(v) for v in line.split(",")))
        elif "fold" in line:
            d, p = line.split(" ")[-1].split("=")
            folds.append((d, int(p)))

for i, (d, p) in enumerate(folds):
    new_dots = set()

    for x, y in dots:
        if d == "x":
            if x > p:
                x = x - 2 * (x - p)
        elif d == "y":
            if y > p:
                y = y - 2 * (y - p)

        new_dots.add((x, y))

    dots = new_dots

    if i == 0:
        print("Task 1:", len(dots))

grid = [['.' for _ in range(max([x for x, y in dots]) + 1)] for _ in range(max([y for x, y in dots]) + 1)]
for x, y in dots:
    grid[y][x] = "X"

print("Task 2:")
for row in grid:
    print(''.join(row))
