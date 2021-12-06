from collections import Counter

m = Counter(int(d) for d in open("../input.txt").read().split(','))

for _ in range(256):
    m = Counter({k-1:v for k, v in m.items() if k > 0})+Counter({6:m[0],8:m[0]})

print(sum(m.values()))
