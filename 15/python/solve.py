from dataclasses import dataclass, field
from typing import List, Set, Tuple
import heapq

@dataclass(order=True)
class Entry:
    f: int
    g: int=field(compare=False)
    next: Tuple[int, int]=field(compare=False)

def search(grid):
    seen = {(0, 0): 0}
    queue = [Entry(f=0, g=0, next=(0, 0))]

    mx = len(grid[-1]) - 1
    my = len(grid) - 1

    while len(queue) > 0:
        entry = heapq.heappop(queue)

        if entry.next == (mx, my):
            return entry.g

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ox, oy = dx + entry.next[0], dy + entry.next[1]

            if oy < 0 or oy > my or ox < 0 or ox > mx:
                continue

            g = entry.g + grid[oy][ox]

            if (ox, oy) in seen and seen[(ox, oy)] <= g:
                continue

            seen[(ox, oy)] = g

            heapq.heappush(queue, Entry(g=g, f=g+(mx - ox)+(my - oy), next=(ox, oy)))

grid = [[int(c) for c in line.strip()] for line in open("../input.txt").readlines()]
print("Task 1:", search(grid))

grid5 = [[0 for _ in range(len(grid[-1]) * 5)] for _ in range(len(grid) * 5)]
for i in range(len(grid5)):
    io = i % len(grid)
    iw = i // len(grid)
    for j in range(len(grid5[-1])):
        jo = j % len(grid[-1])
        jw = j // len(grid[-1])
        nw = grid[io][jo] + iw + jw

        if nw >= 10:
            nw = (nw % 10) + 1

        grid5[i][j] = nw

print("Task 2:", search(grid5))
