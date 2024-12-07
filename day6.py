OBSTACLE = "#"
EMPTY = "."
DIR = {'^': (-1, 0), '>': (0, 1) ,'v': (1, 0), '<': (0, -1) }

# Sample data for testing
data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

# Converting the input string into a 2D grid list
def parse_input(data):
    """
    Converts the input string into a 2D list where each character is an element of the grid.
    """
    grid = [list(line) for line in data.splitlines()]
    return grid

# Function to solve part 1
def part1(data):
    """
    Solve Part 1: Determine when the guard leaves the grid.
    """
    steps = 0

    # Convert the input data into a 2D grid
    grid = parse_input(data)
    gridHeight = len(grid)
    gridWidth = len(grid[0])
    
    # Example: Display the grid structure for debugging
    print(grid)

    # Step 1: Identify the initial position of the guard (marked by '^', 'v', '<', '>')
    # HINT: Use a nested loop to find the character in the grid.
    guardLoc = (-1,-1)
    guard = ""
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] in "^<>v":
                guard = grid[r][c]
                guardLoc = (r,c)
    
    # Step 2: Determine the direction the guard is facing and its initial movement vector
    # Use a dictionary to map characters to movement vectors, e.g., {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}.
    guardVec = DIR[guard]

    # Step 3: Simulate the movement of the guard in the grid.
    # Use a while loop to move the guard step-by-step based on its direction.
    while True:
        row, col = guardLoc[0], guardLoc[1]
        newGuardRow = row + guardVec[0]
        newGuardCol = col + guardVec[1]
        steps += 1
    
    # Step 4: Check for conditions where the guard leaves the grid.
    # If the guard's position goes out of the grid bounds, stop and return the step count.
        if not (0 < newGuardCol < gridWidth) or not(0 < newGuardRow < gridHeight):
            return steps
        elif [newGuardRow][newGuardCol] == OBSTACLE:
            # turn right
            DIR.keys()[(DIR.keys().index(guard) + 1) % 4]
        
        grid[row][col] = EMPTY
        grid[newGuardRow][newGuardCol] = guard
        guardLoc = (newGuardRow,newGuardCol)





    return steps  # Replace this with the actual result

# Placeholder for Part 2 (if students wish to extend their learning)
def part2(data):
    """
    Solve Part 2 (to be implemented later).
    """
    pass

# Main execution
print(part1(data))  # Solve Part 1
print(part2(data))  # Placeholder for Part 2