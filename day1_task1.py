# Reading the data from the input file and computing the total distance
import pandas as pd

# Load the file
file_path = '/mnt/data/input.txt'

# Read the data into a dataframe
df = pd.read_csv(file_path, delim_whitespace=True, header=None, names=["Left", "Right"])

# Extract the two lists
left_list = df["Left"].tolist()
right_list = df["Right"].tolist()

# Function to calculate total distance
def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    return sum(abs(l - r) for l, r in zip(left_list, right_list))

# Calculate the total distance
total_distance = calculate_total_distance(left_list, right_list)
total_distance
