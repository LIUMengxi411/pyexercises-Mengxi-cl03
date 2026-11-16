"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. In:
# A list of student scores.

# 2. Process, function by function:
# Function 1 calculates the total score.
# Function 2 finds the highest score.
# Function 3 calculates the average score.
# Function 4 combines the three results.

# 3. Out:
# Total score, highest score, and average score.

# 4. The question my fourth function answers:
# What is the overall performance of these scores?
# Splitting the work makes each function easier to test.


# Function 1: Calculate the total score
def calculate_total(scores):
    return sum(scores)


# Function 2: Find the highest score
def find_highest(scores):
    if len(scores) == 0:
        return None
    return max(scores)


# Function 3: Calculate the average score
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


# Function 4: Combine the three functions
def analyze_scores(scores):
    total = calculate_total(scores)
    highest = find_highest(scores)
    average = calculate_average(scores)

    print("Total score:", total)
    print("Highest score:", highest)
    print("Average score:", average)


# Test each small function separately
scores = [70, 80, 90, 60, 100]

# Test 1: Input [70, 80, 90, 60, 100]
# Expected total: 400
print("Test 1:", calculate_total(scores))

# Test 2: Input [70, 80, 90, 60, 100]
# Expected highest: 100
print("Test 2:", find_highest(scores))

# Test 3: Input [70, 80, 90, 60, 100]
# Expected average: 80.0
print("Test 3:", calculate_average(scores))

# Test the fourth function
print("Final analysis:")
analyze_scores(scores)

