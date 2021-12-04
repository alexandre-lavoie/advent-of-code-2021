with open('../input.txt') as h:
    nums = [int(d) for d in h.readlines()]

a1 = sum(cur < nxt for cur, nxt in zip(nums[:-1], nums[1:]))
print("Part 1:", a1)

a2 = 0
rolling = nums[:3]
for n in nums[3:]:
    cur = sum(rolling)
    rolling = rolling[1:] + [n]
    nxt = sum(rolling)
    a2 += 1 if cur < nxt else 0

print("Part 2:", a2)
