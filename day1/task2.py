from collections import Counter

# Read the new input data
file_path = '/mnt/data/input2.txt'

# Load data into a DataFrame
df = pd.read_csv(file_path, delim_whitespace=True, header=None, names=["Left", "Right"])

# Extract the two lists
left_list = df["Left"].tolist()
right_list = df["Right"].tolist()

# Count the frequency of each number in the right list
right_count = Counter(right_list)

# Calculate the similarity score
similarity_score = sum(left * right_count[left] for left in left_list)

similarity_score
