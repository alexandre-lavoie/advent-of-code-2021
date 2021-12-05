import re
from collections import defaultdict

def s(cs):
    g = defaultdict(int)

    for l in [[tuple(int(v) for v in p.split(",")) for p in l] for l in re.findall(r"([\d,]+)\s+->\s+([\d,]+)", open("../input.txt").read())]:
        p = l[0]
        d = [(1 if s < e else (-1 if s > e else 0)) for s, e in zip(*l)]

        if cs and sum(abs(v) for v in d) > 1: continue

        while p != l[1]:
            g[p] += 1
            p = tuple(v + o for v, o in zip(p, d))
        g[l[1]] += 1

    return sum(v > 1 for v in g.values())

if __name__ == "__main__":
    for i in range(1, 3):
        print(i, ":", s(i==1))
