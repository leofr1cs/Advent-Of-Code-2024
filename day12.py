from aocd import get_data
from itertools import combinations, permutations, product, chain
from collections import Counter, defaultdict, deque
import math
import re

# Fetch the day's input data
data = get_data(day=12, year=2024)  # Specify the day and year
print(data)

# Useful constants and helpers
NORTH, SOUTH, EAST, WEST = (-1, 0), (1, 0), (0, 1), (0, -1)
DIRECTIONS = [NORTH, SOUTH, EAST, WEST]

# Diagonal directions (optional, used in some puzzles)
DIAGONALS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Grid direction vectors (including diagonals)
ALL_DIRECTIONS = DIRECTIONS + DIAGONALS

# Useful itertools combinations
def get_combinations(iterable, r):
    "Return combinations of the given iterable of length r."
    return combinations(iterable, r)

def get_permutations(iterable, r=None):
    "Return permutations of the given iterable of length r."
    return permutations(iterable, r)

def cartesian_product(*iterables):
    "Return the cartesian product of the given iterables."
    return product(*iterables)

# Parsing helpers
def extract_numbers(s):
    "Extract all integers from a string."
    return list(map(int, re.findall(r'-?\\d+', s)))

# Example use case of constants and helpers
if __name__ == "__main__":
    # Parse the input if needed
    numbers = extract_numbers(data)
    print("Extracted numbers:", numbers)

    # Example: Iterate over the grid using direction vectors
    x, y = 0, 0  # Starting point
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        print(f"Move to ({{nx}}, {{ny}})")
