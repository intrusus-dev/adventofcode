# Define a function to check if a report is safe after removing a single level
def can_be_safe(report):
    # Function to check if a sequence is strictly increasing or decreasing with valid differences
    def is_valid(sequence):
        increasing = all(1 <= sequence[i+1] - sequence[i] <= 3 for i in range(len(sequence) - 1))
        decreasing = all(1 <= sequence[i] - sequence[i+1] <= 3 for i in range(len(sequence) - 1))
        return increasing or decreasing

    # Check if the original report is safe
    if is_valid(report):
        return True
    
    # Check if removing one level makes the report safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_valid(modified_report):
            return True
    
    return False

# Count the safe reports using the Problem Dampener
safe_count_with_dampener = sum(1 for report in reports if can_be_safe(report))
safe_count_with_dampener
