import itertools

with open("../input.txt") as h:
    board = [[int(c) for c in line.strip()] for line in h.readlines()]

def add_one():
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            board[i][j] = (c + 1) % 10

def flash_one(i, j):
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
        return

    if board[i][j] > 0:
        board[i][j] = (board[i][j] + 1) % 10

def print_board():
    for row in board:
        print(''.join(str(c) for c in row))
    print()

DT = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
def flash(flashed=None):
    if flashed == None:
        previous = -1
        flashed = set()
    else:
        previous = len(flashed)

    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if not c == 0:
                continue

            if (i, j) in flashed:
                continue

            flashed.add((i, j))

            for di, dj in DT:
                flash_one(i + di, j + dj)

    if previous < len(flashed):
        return flash(flashed)
    else:
        return len(flashed)

t1 = 0
t2 = None
for step in itertools.count(start=1):
    add_one()
    flash_count = flash()

    if step <= 100:
        t1 += flash_count

    if t2 == None and flash_count >= len(board) * len(board[0]):
        t2 = step

        if step > 100:
            break

print("Task 1:", t1)
print("Task 2:", t2)
