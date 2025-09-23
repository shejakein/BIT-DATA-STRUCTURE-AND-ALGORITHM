(224004070) SHEJA-KEVIN-ALBERTO-S-DATA-STRUCTURE-AND-ALGORITHM-ASSIGNMENT 
The following is a brief summary of 102 project By SHEJA KEVIN Alberto about Bug Report Triage

1. Integers: Bug Counts and Basic Calculations
I started with a list of integers representing the number of bugs reported by various software teams, Then using Python’s built-in functions, I calculated:
Total number of bugs reported
Average number of bugs per team
Minimum and maximum bugs reported

2. Strings: Formatted Summary Report
A detailed report string was created using f-strings and it included the calculated calculations: total bugs, average bugs, minimum and maximum values.

3. Booleans: Threshold-Based Evaluation
I defined a threshold (10 bugs per team) to assess performance and i used a compound boolean condition:
If the average bugs per team exceeded the threshold AND the maximum number of bugs by a team was at least 15, the system labeled the triage as "Above Standard".
If not, it labeled it "Below Standard".

4. Lists: Managing Bug Sources
I used a list to represent team names that reported bugs, and used basic list operations:
I added a new team to the list using append().
I removed teams that didn’t meet a specific condition (e.g., teams that reported fewer than 6 bugs).
I sorted the list alphabetically using sort().

5. Arrays: Fixed Subset of Bug Data
I used Python’s array module to store a subset of bug counts in a fixed-type array and calculated the sum of this array and compared it to the sum of the same slice of the list to show that the results of calculations are consistent between lists and arrays for the same data.

6. Dictionaries: Bug Report Records

I created a list of dictionaries, each representing a bug report record with:
Id
Name (team name)
Value (number of bugs reported)

What was shown: 
Updating a bug count for a specific team (Team Gamma)
Deleting a team’s record (Team Delta)

Finally, computed the total number of bugs from the updated list of dictionaries.
