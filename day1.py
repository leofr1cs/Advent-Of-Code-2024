from aocd import get_data
from collections import Counter
import re

def parse_data(data):
    """
    Parse the input data into two lists of integers based on the given format.
    """
    listA, listB = [], []
    for line in data.split("\n"):
        match = re.match(r"(\d+)\s{3}(\d+)", line)
        if match:
            a, b = map(int, match.groups())
            listA.append(a)
            listB.append(b)
    return sorted(listA), sorted(listB)

def calculate_minimum_difference_sum(listA, listB):
    """
    Calculate the sum of absolute differences between corresponding elements in sorted lists.
    """
    return sum(abs(a - b) for a, b in zip(listA, listB))

def calculate_weighted_sum(listA, listB):
    """
    Calculate the weighted sum of elements in listA based on their occurrence in listB.
    """
    counts = Counter(listB)  # Count occurrences in listB once for efficiency
    return sum(a * counts[a] for a in listA)

# Fetch and parse the input data
data = get_data(day=1, year=2024)  # Specify the day and year
listA, listB = parse_data(data)

# Part 1: Calculate and print the total for the minimum difference sum
part1_total = calculate_minimum_difference_sum(listA, listB)
print("Part 1:", part1_total)

# Part 2: Calculate and print the weighted sum
part2_total = calculate_weighted_sum(listA, listB)
print("Part 2:", part2_total)