"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# 1. In:
# The user enters a name, email, and student ID.

# 2. Process:
# Use regular expressions to check each input.
# Save the information only if all three are valid.

# 3. Out:
# A success message if all inputs are valid.
# Otherwise, show an error message.

# 4. My validation rules:
# Name: At least 2 English letters.
# Email: Must contain @ and a domain with a dot.
# Student ID: Exactly 7 digits.

import re

name = input("Enter your name: ")
email = input("Enter your email: ")
student_id = input("Enter your student ID: ")

name_pattern = r"[A-Za-z]{2,}"
email_pattern = r"[^@\s]+@[^@\s]+\.[^@\s]+"
id_pattern = r"[0-9]{7}"

if (re.fullmatch(name_pattern, name)
    and re.fullmatch(email_pattern, email)
    and re.fullmatch(id_pattern, student_id)):

    with open("valid_students.txt", "a") as file:
        file.write(name + "," + email + "," + student_id + "\n")

    print("Information saved successfully!")

else:
    print("Invalid information. Please check your input.")