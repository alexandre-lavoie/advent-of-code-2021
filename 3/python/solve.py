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

def rating(type, data, bit=0):
    if len(data) == 1:
        return data[0]

    total = sum([1 if v[bit] == '1' else 0 for v in data])
    common = '1' if total / len(data) >= 0.5 else '0'

    if type == "c02":
        common = '0' if common == '1' else '1'

    data = [v for v in data if v[bit] == common]

    return rating(type, data, bit + 1)

print("Task 2:", int(rating("oxygen", data), 2) * int(rating("c02", data), 2))