# Open the file and read the data
with open('input.txt', 'r') as file:
    data = file.readlines()

# Parse each line into a list of integers
reports = [list(map(int, line.split())) for line in data]

def is_safe_report(report):
    """Check if a report is safe based on the original criteria."""
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)
    valid_differences = all(1 <= abs(diff) <= 3 for diff in differences)
    return (is_increasing or is_decreasing) and valid_differences

def can_be_made_safe(report):
    """Check if a report can be made safe by removing one level."""
    for i in range(len(report)):
        # Create a new report with the ith level removed
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False

# Count the number of safe reports
safe_count = 0
for report in reports:
    if is_safe_report(report) or can_be_made_safe(report):
        safe_count += 1

print(f"Number of safe reports with the Problem Dampener: {safe_count}")
