def task1():
    with open("../input.txt") as h:
        data = [x.strip() for x in h.readlines()]

    bingo = data[0].split(',')
    boards = []

    while len(data) > 0:
        board = data[2:7]
        data = data[6:]

        boards.append([row.split() for row in board])

    score = 0
    done = False
    for k, b in enumerate(bingo):
        for board in boards:
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == b:
                        board[i][j] = ''
            
            for row in board:
                if all(c == '' for c in row):
                    done = True
                    break

            if not done:
                for col in zip(*board):
                    if all(c == '' for c in col):
                        done = True
                        break

            if done:
                for row in board:
                    for c in row:
                        if not c == '':
                            score += int(c)
                score *= int(b)
                break
        if done:
            break

    print("Task 1:", score)

def task2():
    with open("../input.txt") as h:
        data = [x.strip() for x in h.readlines()]

    bingo = data[0].split(',')
    boards = []

    while len(data) > 0:
        board = data[2:7]
        data = data[6:]

        boards.append([row.split() for row in board])

    score = 0
    done = [False] * len(boards)
    for k, b in enumerate(bingo):
        for bn, board in enumerate(boards):
            if done[bn]:
                continue

            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == b:
                        board[i][j] = ''
            
            for row in board:
                if all(c == '' for c in row):
                    done[bn] = True
                    continue

            if not done[bn]:
                for col in zip(*board):
                    if all(c == '' for c in col):
                        done[bn] = True
                        continue

            if done[bn] and sum([1 if v else 0 for v in done]) == len(boards) - 1:
                for row in board:
                    for c in row:
                        if not c == '':
                            score += int(c)
                score *= int(b)
                break
        if all(done):
            break

    print("Task 2:", score)

task1()
task2()
