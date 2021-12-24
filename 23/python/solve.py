"""
This solution doesn't work, I gave up like the last few days...
"""

import string
import heapq
import itertools
from typing import List
from enum import Enum
from dataclasses import dataclass, field

ENERGY = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

DEPTH = 2

class Direction(Enum):
    LEFT=-1
    RIGHT=1

@dataclass(order=True)
class State:
    g: int = field(compare=False)
    f: int = field(compare=True)

    burrows: List[List[str]] = field(compare=False)
    surface: List[str] = field(compare=False)

    @property
    def copy(self) -> 'State':
        return State(
            g=self.g,
            f=self.f,
            burrows=[burrow.copy() for burrow in self.burrows],
            surface=self.surface.copy()
        )

    @property
    def done(self) -> bool:
        for burrow, amphipod in zip(self.burrows, string.ascii_uppercase):
            if not burrow == [amphipod] * DEPTH:
                return False

        return True

    @property
    def transitions(self) -> List['State']:
        next_states = []

        for i, d in itertools.product(range(len(self.burrows)), Direction):
            next_state = self.copy
            try:
                next_state.enter(i, d)
                next_states.append(next_state)
            except AssertionError as e:
                pass

        for i, d in itertools.product(range(len(self.burrows)), Direction):
            next_state = self.copy
            try:
                next_state.exit(i, d)
                next_states.append(next_state)
            except AssertionError as e:
                pass

        for i, d in itertools.product(range(len(self.surface)), Direction):
            next_state = self.copy
            try:
                next_state.move(i, d)
                next_states.append(next_state)
            except AssertionError as e:
                pass

        return next_states

    @property
    def heuristic(self) -> int:
        energy = 0

        for burrow, target_amphipod in zip(self.burrows, string.ascii_uppercase):
            for depth, amphipod in enumerate(burrow):
                if amphipod == target_amphipod:
                    continue

                burrow_index_difference = abs(ord(target_amphipod[0]) - ord(amphipod[0]))
                burrow_depth = DEPTH - depth
                energy += self.energy(amphipod, distance=burrow_index_difference * 2 + burrow_depth + 1)

        for i, amphipod in enumerate(self.surface):
            if not amphipod:
                continue

            target_burrow = (ord(amphipod[0]) - ord('A')) * 2 + 2
            energy += self.energy(amphipod, distance=abs(target_burrow - i) + 1)

        return energy

    def energy(self, amphipod: str, distance: int) -> int:
        return ENERGY[amphipod] * distance

    def update(self):
        self.f = self.g + self.heuristic

    def enter(self, index: int, direction: Direction):
        from_index = index * 2 + direction.value + 2

        assert not self.surface[from_index] == None
        assert len(self.burrows[index]) < DEPTH
        # assert all(ord(amphipod) - ord('A') == index for amphipod in self.burrows[index])

        amphipod = self.surface[from_index]
        self.surface[from_index] = None
        self.burrows[index].append(amphipod)

        self.g += self.energy(amphipod, distance=DEPTH - len(self.burrows[index]) + 2)

    def exit(self, index: int, direction: Direction):
        target_index = index * 2 + direction.value + 2

        assert self.surface[target_index] == None
        assert len(self.burrows[index]) > 0

        amphipod = self.burrows[index].pop()
        self.surface[target_index] = amphipod

        self.g += self.energy(amphipod, distance=DEPTH - len(self.burrows[index]) + 1)

    def move(self, index: int, direction: Direction):
        assert not self.surface[index] == None

        target_index = index + direction.value
        if target_index > 0 and target_index < 10 and target_index % 2 == 0:
            target_index += direction.value

        assert target_index >= 0 and target_index < len(self.surface)
        assert self.surface[target_index] == None

        amphipod = self.surface[index]
        self.surface[index] = None
        self.surface[target_index] = amphipod

        self.g += self.energy(amphipod, distance=abs(target_index - index))

    @property
    def raw(self):
        return (''.join(a if a else '.' for a in self.surface), tuple(tuple(b) for b in self.burrows))

    def __repr__(self) -> str:
        s = "#" * (len(self.surface) + 2) + "\n"
        s += "#" + ''.join(a if a else "." for a in self.surface) + "#\n"

        burrows = list(zip(*[["."] * (DEPTH - len(b)) + list(reversed(b)) for b in self.burrows]))
        
        for burrow in burrows:
            bs = ["#"] * (len(self.surface) + 2)
            for i, a in enumerate(burrow):
                bs[i * 2 + 3] = a
            s += ''.join(bs) + "\n"
        s += "#" * (len(self.surface) + 2) + "\n"

        return s

def main(path: str):
    grid = open(path).read().replace("#", "").replace(" ", "").split("\n")
    initial_burrows = list(map(lambda v: list(reversed(v)), zip(*grid[2:-1])))
    initial_surface = [None] * len(grid[1])
    initial_state = State(
        g=0,
        f=0,
        burrows=initial_burrows,
        surface=initial_surface
    )

    queue = [initial_state]
    while len(queue) > 0:
        state = heapq.heappop(queue)

        print(state)

        if state.done:
            print(state)
            break

        for next_state in state.transitions:
            next_state.update()
            heapq.heappush(queue, next_state)

if __name__ == "__main__":
    main("../input.t1.txt")
