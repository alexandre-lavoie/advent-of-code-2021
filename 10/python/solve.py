with open("../input.txt") as h:
    lines = [line.strip() for line in h.readlines()]

delimiters = [("(", ")"), ("{", "}"), ("<", ">"), ("[", "]")]

on_stack = {}
for o, c in delimiters:
    on_stack[o] = True
    on_stack[c] = False

closing = dict(delimiters)

t1_mapping = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

t2_mapping = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

t1 = 0
t2 = []
for line in lines:
    stack = []

    for c in line:
        if on_stack[c]:
            stack.append(c)
            continue
        if not closing[stack.pop()] == c:
            t1 += t1_mapping[c]
            break
    else:
        score = 0

        for c in reversed(stack):
            score *= 5
            score += t2_mapping[c]

        t2.append(score)

t2 = sorted(t2)[len(t2) // 2]

print("Task 1:", t1)
print("Task 2:", t2)
