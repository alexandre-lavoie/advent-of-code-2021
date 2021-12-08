size_mapping = {
    2:1,
    3:7,
    4:4,
    7:8
}
intersect_values = (1,4)
intersection_mapping = {
    5:[(2,(1,2)),(3,(2,3)),(5,(1,3))],
    6:[(0,(2,3)),(6,(1,3)),(9,(2,4))]
}

t1 = 0
t2 = 0
for line in [line.strip() for line in open("../input.txt").readlines()]:
    patterns, outputs = line.split("|")

    mapping = {}
    for pattern in patterns.split():
        if len(pattern) in size_mapping:
            mapping[size_mapping[len(pattern)]] = set(pattern)

    for pattern in patterns.split():
        lp = len(pattern)
        if lp in intersection_mapping:
            sp = set(pattern)
            for value, intersection_counts in intersection_mapping[lp]:
                for test_value, intersection_count in zip(intersect_values, intersection_counts):
                    if not len(mapping[test_value] & sp) == intersection_count:
                        break
                else:
                    mapping[value] = sp
                    break

    conversion = {''.join(sorted(v)):k for k, v in mapping.items()}
    output = ""
    for pattern in outputs.split():
        v = conversion[''.join(sorted(pattern))]
        if v in size_mapping.values():
            t1 += 1
        output += str(v)
    t2 += int(output)

print("Task 1:", t1)
print("Task 2:", t2)
