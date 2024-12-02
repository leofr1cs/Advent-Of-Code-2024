from aocd import get_data
import re

# Fetch the day's input data
data = get_data(day=1, year=2024)  # Specify the day and year
# data ="""3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""

data = data.split("\n")
listA, listB = [], []
for d in data:
    match = re.match(r"(\d+)\s{3}(\d+)",d).groups()
    listA.append(int(match[0]))
    listB.append(int(match[1]))

listA.sort()
listB.sort()

total = sum(abs(listA[i] - listB[i]) for i in range(len(listA)))

print("Part1: ", total)

total = 0
for v in listA:
    count = listB.count(v)
    total += (v * count)

print("Part 2:", total)


print()