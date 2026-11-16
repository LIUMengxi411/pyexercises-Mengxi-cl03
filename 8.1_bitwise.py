"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# 1. In:
# Two sets of permissions for managing a marketing campaign.

# 2. Process:
# Use bitwise OR to combine permissions.
# Use bitwise AND to check a permission.
# Add and remove permissions using bitwise operators.

# 3. Out:
# The permission values in binary after each step.

# 4. My permissions:
# View: 001, Edit: 010, Publish: 100.
# These permissions control what a team member
# can do with a marketing campaign.

# Define permissions
VIEW = 0b001
EDIT = 0b010
PUBLISH = 0b100

# Two team members
person_a = VIEW | EDIT
person_b = VIEW | PUBLISH

print("Person A:", format(person_a, "03b"))
print("Person B:", format(person_b, "03b"))

# Combine permissions
combined = person_a | person_b
print("Combined:", format(combined, "03b"))

# Check if EDIT permission exists
print("Can edit:", bool(combined & EDIT))

# Add PUBLISH permission to Person A
person_a = person_a | PUBLISH
print("After adding publish:", format(person_a, "03b"))

# Remove EDIT permission from Person A
person_a = person_a & ~EDIT
print("After removing edit:", format(person_a, "03b"))