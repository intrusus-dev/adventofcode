# Reimport dependencies due to code reset
import re

# Re-read the input file and prepare the grid
file_path = '/mnt/data/input6.txt'

# Read the grid into a list of rows
with open(file_path, 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Define directions for searching: horizontal, vertical, diagonal
directions = [
    (0, 1),    # Right
    (0, -1),   # Left
    (1, 0),    # Down
    (-1, 0),   # Up
    (1, 1),    # Diagonal Down-Right
    (-1, -1),  # Diagonal Up-Left
    (1, -1),   # Diagonal Down-Left
    (-1, 1)    # Diagonal Up-Right
]

def is_valid(x, y, rows, cols):
    """Check if coordinates are within the grid boundaries."""
    return 0 <= x < rows and 0 <= y < cols

def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                # Check for the word in the current direction
                valid = True
                for k in range(word_len):
                    nx, ny = x + dx * k, y + dy * k
                    if not is_valid(nx, ny, rows, cols) or grid[nx][ny] != word[k]:
                        valid = False
                        break
                if valid:
                    count += 1
    return count

# Count all occurrences of "XMAS"
word_to_find = "XMAS"
total_occurrences = count_word_occurrences(grid, word_to_find)
total_occurrences
