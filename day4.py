from aocd import get_data
from itertools import combinations, permutations, product, chain
from collections import Counter, defaultdict, deque
import math
import re

data = get_data(day=4, year=2024) 

def getCoords(x, y, dx, dy, SIZE_X, SIZE_Y, length=4):
    """
    Get the coordinates of a sequence in the grid starting from (x, y)
    in the direction (dx, dy) with the given length.
    """
    coords = [(x + dx * i, y + dy * i) for i in range(length)]
    # Check if all coordinates are within the grid bounds
    if all(0 <= cx < SIZE_X and 0 <= cy < SIZE_Y for cx, cy in coords):
        return coords
    return None


def part1(data):
    # XMAS hunting
    data = [[l for l in d] for d in data.split("\n")]
    SIZE_X = len(data)
    SIZE_Y = len(data[0])
    dataDict = {(x, y): data[x][y] for x in range(SIZE_X) for y in range(SIZE_Y)}
    
    count = 0
    target = "XMAS"
    length = len(target)
    
    # Iterate through every cell in the grid
    for x in range(SIZE_X):
        for y in range(SIZE_Y):
            # Check all directions
            for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                coords = getCoords(x, y, dx, dy, SIZE_X, SIZE_Y, length)
                if coords:
                    # Build the string dynamically
                    sequence = "".join(dataDict[c] for c in coords)
                    if sequence == target:
                        count += 1

    return count


# Test data
data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

print(part1(data))  # Output: Count of "XMAS" strings

