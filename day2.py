from aocd import get_data

# Fetch the day's input data
data = get_data(day=2, year=2024)  # Specify the day and year

# Parse input data into a list of lists of integers
data = [[int(v) for v in row.split()] for row in data.split("\n")]

def is_safe(row):
    """
    Checks if a row is "safe" based on the given criteria.
    A row is safe if:
    1. It maintains a consistent ascending or descending order.
    2. The difference between consecutive numbers is at most 3.
    """
    ascending = row[1] > row[0]
    for i in range(len(row) - 1):
        current, next_val = row[i], row[i + 1]
        if ascending:
            if current >= next_val or abs(current - next_val) > 3:
                return False
        else:
            if next_val >= current or abs(current - next_val) > 3:
                return False
    return True

# Part 1: Count rows that are initially safe
safe_count = sum(1 for row in data if is_safe(row))
print("Part 1:", safe_count)

# Part 2: Handle rows that can be made safe by removing one element
def can_be_safe(row):
    """
    Determines if a row can be made safe by removing one element.
    """
    for i in range(len(row)):
        modified_row = row[:i] + row[i + 1:]  # Remove the ith element
        if is_safe(modified_row):
            return True
    return False

# Part 2: Count safe rows, considering modifications
safe_count = 0
for row in data:
    if is_safe(row) or can_be_safe(row):
        safe_count += 1

print("Part 2:", safe_count)