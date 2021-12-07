from statistics import median

with open("../input.txt") as h:
    data = [int(i) for i in h.read().split(",")]

print("Task 1:", sum(abs(d - median(data)) for d in data))
print("Task 2:", min(sum((abs(d - i) * (abs(d - i) + 1)) // 2 for d in data) for i in range(min(data), max(data))))
