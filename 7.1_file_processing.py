"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# -
# -
# -
# -

# What is wrong with names.txt:
# 1. Some lines are empty.
# 2. Some names have extra spaces.
# 3. Some names appear more than once.
# 4. Some names use inconsistent capitalization.
# 5. Some names use different separators.

# 1. In:
# The program reads names from names.txt.

# 2. Process:
# Remove empty lines and extra spaces.
# Standardize capitalization and separators.
# Remove duplicate names.
# Sort the names alphabetically by last name.

# 3. Out:
# A new file called cleaned_names.txt containing
# the cleaned and sorted names.

# 4. How I decide which word is the last name:
# For names written as First Last, I use the last word.
# For names written as Last, First, I use the word
# before the comma.


# Read names from the original file
with open("names.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

cleaned_names = []

for line in lines:
    name = line.strip()

    # Skip empty lines
    if name == "":
        continue

    # Handle comma-separated names
    if "," in name:
        parts = name.split(",", 1)
        last_name = parts[0].strip()
        first_name = parts[1].strip()
        name = first_name + " " + last_name

    # Remove extra spaces and fix capitalization
    name = " ".join(name.split()).title()

    # Avoid duplicate names
    if name not in cleaned_names:
        cleaned_names.append(name)

# Sort by last name
cleaned_names.sort(key=lambda name: name.split()[-1].lower())

# Save the cleaned names to a new file
with open("cleaned_names.txt", "w", encoding="utf-8") as file:
    for name in cleaned_names:
        file.write(name + "\n")

print("Names cleaned and sorted successfully!")
print("Total names:", len(cleaned_names))
print("Results saved to cleaned_names.txt")

