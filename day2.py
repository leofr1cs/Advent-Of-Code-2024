from aocd import get_data
from itertools import combinations, permutations, product, chain
from collections import Counter, defaultdict, deque
import math
import re

# Fetch the day's input data
data = get_data(day=2, year=2024)  # Specify the day and year

# data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""


data = [[int(v) for v in row.split(" ")] for row in data.split("\n")]

safeCount = 0
for r in data:
    safe = True
    if r[1] > r[0]: asc = True
    else: asc = False
    for i in range(len(r) - 1):
        c, n = r[i], r[i+1]
        if asc:
            if c >= n:
                safe = False
                break
        elif not(asc):
            if n >= c:
                safe = False
                break
        if abs(n-c) > 3:
            safe = False
            break
    if safe:    safeCount += 1

print("Part1: ", safeCount)

def isSafe(r):
    safe = True
    if r[1] > r[0]: asc = True
    else: asc = False
    for i in range(len(r) - 1):
        c, n = r[i], r[i+1]
        if asc:
            if c >= n:
                safe = False
                break
        elif not(asc):
            if n >= c:
                safe = False
                break
        if abs(n-c) > 3:
            safe = False
            break
    return safe

safeCount = 0
for r in data:
    if isSafe(r): safeCount += 1
    else:
        # Try all variants with a reading removed
        for i in range(len(r)):
            r2 = r[::]
            r2.pop(i)
            if isSafe(r2):
                safeCount += 1
                break

print("Part2: ", safeCount)

print()