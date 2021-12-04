with open("../input.txt") as h:
    moves = h.readlines()

# P1

x, z = [0] * 2
for move in moves:
    name, value = move.split()
    value = int(value)

    if name == "forward":
        x += value
    elif name == "down":
        z += value
    elif name == "up":
        z -= value

print(x * z)

# P2

x, y, z = [0] * 3
for move in moves:
    name, value = move.split()
    value = int(value)

    if name == "forward":
        x += value
        z += y * value
    elif name == "down":
        y += value
    elif name == "up":
        y -= value

print(x * z)
