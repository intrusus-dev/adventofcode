# Define a function to check if a report is safe
def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

# Read the input file
file_path = '/mnt/data/input3.txt'

# Read the data
with open(file_path, 'r') as f:
    reports = [[int(num) for num in line.split()] for line in f.readlines()]

# Count the safe reports
safe_count = sum(1 for report in reports if is_safe(report))

safe_count
