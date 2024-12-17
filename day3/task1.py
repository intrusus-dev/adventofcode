import re

# Read the corrupted memory file
file_path = '/mnt/data/input5.txt'

with open(file_path, 'r') as file:
    data = file.read()

# Define a regex to match valid mul(X,Y) instructions
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all valid matches
matches = re.findall(pattern, data)

# Calculate the total sum of multiplications
total_sum = sum(int(x) * int(y) for x, y in matches)
total_sum
