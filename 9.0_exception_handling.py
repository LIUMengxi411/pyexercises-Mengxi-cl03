"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# A number entered by the user.

# 2. Process:
# Convert the input into a number and divide 100 by it.
# Use try and except to handle different errors.
# Allow the user to try again if the input is invalid.

# 3. Out:
# The division result or a clear error message.

# 4. Possible failures:
# ZeroDivisionError happens when the user enters zero.
# ValueError happens when the user enters text or nothing.
# These errors need different messages because
# they happen for different reasons.
# I allow the user to try again instead of stopping.

# Your code below

while True:
    user_input = input("Enter a number (or q to quit): ")

    if user_input.lower() == "q":
        print("Program finished.")
        break

    try:
        number = float(user_input)
        result = 100 / number
        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter a number.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    print("Please try again.\n")
    