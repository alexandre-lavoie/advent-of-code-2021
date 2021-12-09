with open("../input.txt") as h:
    board = [[int(n) for n in line.strip()] for line in h.readlines()]

OFFSETS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def on_board(i, j):
    return i >= 0 and j >= 0 and i < len(board) and j < len(board[i])

def min_adjacent(i, j):
    min_value = None

    for di, dj in OFFSETS:
        oi, oj = i + di, j + dj

        if not on_board(oi, oj):
            continue

        if min_value == None or board[oi][oj] < min_value:
            min_value = board[oi][oj]

    return min_value

min_points = set()
t1 = 0
for i, row in enumerate(board):
    for j, value in enumerate(row):
        if value < min_adjacent(i, j):
            t1 += value + 1
            min_points.add((i, j))

print("Task 1:", t1)

def spread(point, exclude=None):
    if not exclude:
        exclude = set()

    exclude.add(point)

    points = [point]
    for di, dj in OFFSETS:
        oi, oj = point[0] + di, point[1] + dj

        if not on_board(oi, oj):
            continue

        if (oi, oj) in exclude:
            continue

        if board[oi][oj] < 9:
            points += spread((oi, oj), exclude)

    return points

basins = []
for point in min_points:
    basins.append(spread(point))

t2 = 1
for basin in sorted(basins, key=lambda basin: len(basin))[-3:]:
    t2 *= len(basin)

print("Task 2:", t2)
