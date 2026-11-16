"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# 1. In:
# Two values: 10 and 5.

# 2. Process:
# Compare the two values using comparison operators
# and logical operators.

# 3. Out:
# A table showing True or False for each comparison.

# 4. My values and surprising result:
# I chose 10 and 5.
# I found that "not (a > b)" gives False,
# even though "a > b" gives True.

# Your code below

a = 10
b = 5

print("Value A:", a)
print("Value B:", b)

print("-------------------------------")
print("Comparison       Result")
print("-------------------------------")

print("a == b           ", a == b)
print("a != b           ", a != b)
print("a > b            ", a > b)
print("a < b            ", a < b)
print("a >= b           ", a >= b)
print("a <= b           ", a <= b)

print("-------------------------------")
print("Logical Operators")
print("-------------------------------")

print("a > b and b > 0  ", a > b and b > 0)
print("a > b or b > 10  ", a > b or b > 10)
print("not (a > b)      ", not (a > b))


