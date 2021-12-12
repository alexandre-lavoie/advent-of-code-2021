from collections import defaultdict, Counter

graph = defaultdict(list)
with open("../input.txt") as h:
    for s, e in [line.strip().split('-') for line in h.readlines()]:
        graph[s].append(e)
        graph[e].append(s)

def search(node=None, seen=None, visit_twice=False, visited_twice=False):
    if seen == None:
        seen = Counter()

    if node == None:
        node = "start"
    elif node == "start":
        return 0
    elif node == "end":
        return 1
    elif node.islower() and seen[node] >= 1:
        if visit_twice and not visited_twice:
            visited_twice = True
        else:
            return 0

    seen[node] += 1

    total = sum(search(adjacent, seen, visit_twice, visited_twice) for adjacent in graph[node])

    seen[node] -= 1

    return total

print("Task 1:", search(visit_twice=False))
print("Task 2:", search(visit_twice=True))
