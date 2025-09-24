# Integers: Bug counts from different teams

bug_counts = [12, 8, 17, 5, 9, 11]  # Bugs reported by different teams

total_bugs = sum(bug_counts)
average_bugs = total_bugs / len(bug_counts)
min_bugs = min(bug_counts)
max_bugs = max(bug_counts)

# Strings: Triage Summary Report

report = (
    f"Bug Report Triage Summary:\n"
    f"Total Bugs Reported: {total_bugs}\n"
    f"Average Bugs per Team: {average_bugs:.2f}\n"
    f"Min Bugs Reported by a Team: {min_bugs}\n"
    f"Max Bugs Reported by a Team: {max_bugs}"
)
print(report)

# Booleans: Threshold Check

threshold = 10
if average_bugs > threshold and max_bugs >= 15:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# Lists: Managing Bug Sources

bug_sources = ["Team Alpha", "Team Beta", "Team Gamma", "Team Delta", "Team Epsilon", "Team Zeta"]
print("\nOriginal Bug Sources:", bug_sources)

# Add a new source
bug_sources.append("Team Omega")

# Remove any team with fewer than 6 bugs (based on parallel index)
bug_sources_filtered = [source for i, source in enumerate(bug_sources) if i >= len(bug_counts) or bug_counts[i] >= 6]

# Sort updated list
bug_sources_filtered.sort()
print("Updated and Sorted Bug Sources:", bug_sources_filtered)

# Arrays: Fixed Subset of Bug Counts

import array

bug_array = array.array('i', bug_counts[:4])  # First 4 team bug counts
array_sum = sum(bug_array)
list_sum = sum(bug_counts[:4])

print(f"\nSum of bug counts using array: {array_sum}")
print(f"Sum of bug counts using list: {list_sum}")

# Dictionaries: Bug Report Records

bug_records = [
    {'id': 1, 'name': 'Team Alpha', 'value': 12},
    {'id': 2, 'name': 'Team Beta', 'value': 8},
    {'id': 3, 'name': 'Team Gamma', 'value': 17},
    {'id': 4, 'name': 'Team Delta', 'value': 5}
]

# Update Team Gamma's bug count
for record in bug_records:
    if record['name'] == 'Team Gamma':
        record['value'] = 19

# Delete Team Delta
bug_records = [record for record in bug_records if record['name'] != 'Team Delta']

# Calculate total bugs from remaining teams
total_recorded_bugs = sum(record['value'] for record in bug_records)

print("\nUpdated Bug Records:")
for record in bug_records:
    print(record)

print(f"Total Bugs from Updated Records: {total_recorded_bugs}")
