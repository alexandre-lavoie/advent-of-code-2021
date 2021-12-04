with open("../input.txt") as h:
    data = [l.strip() for l in h.readlines()]

gamma = []
for bits in zip(*data):
    total = sum([1 if x == '1' else 0 for x in bits])
    gamma.append('1' if total / len(bits) > 0.5 else '0')
epsilon = ['0' if b == '1' else '1' for b in gamma]
gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

print("Task 1:", gamma * epsilon)

# TODO

print("Task 2:", 0)