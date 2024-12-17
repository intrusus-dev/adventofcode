# Parse the corrupted memory to handle do() and don't() instructions
enabled = True  # Start with mul instructions enabled
total_sum = 0

# Linear scan through the file
tokens = re.split(r"(\bdo\(\)|\bdon't\(\)|mul\(\d{1,3},\d{1,3}\))", data)

# Process each token
for token in tokens:
    if token == "do()":
        enabled = True
    elif token == "don't()":
        enabled = False
    elif token.startswith("mul(") and enabled:
        # Extract numbers from the mul() instruction
        match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", token)
        if match:
            x, y = int(match[1]), int(match[2])
            total_sum += x * y

total_sum
