"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The user's answer to the question "Do you want to continue?"
# 2. Process:The program keeps asking the question until the user enters "no" or reaches 5 attempts.
# 3. Out:The program displays a message when the loop ends and shows the number of attempts.
# 4. My stop condition, my attempt limit, my summary:
# The stop condition is when the user enters "no".
# The maximum number of attempts is 5.
# The summary shows how many attempts the user made and why the loop stopped.


# Your code below
# Your code below

i = 0
answer = ""

# Keep asking until the user says "no" or reaches 5 attempts.
while answer != "no" and i < 5:
    answer = input("Do you want to continue? ")
    answer = answer.strip().lower()
    i = i + 1

# Check why the loop stopped.
if answer == "no":
    print("The loop stopped because you entered no.")
else:
    print("The maximum number of attempts has been reached.")

# Display a summary.
print("Total number of attempts:", i)

# CHECK IT YOURSELF
# Test 1: I entered "yes" five times.
# The program stopped after 5 attempts, as expected.
#
# Test 2: I entered "   NO   " with capitals and extra spaces.
# The program recognized it as "no" and stopped, as expected.
#
# The summary correctly displayed the total number of attempts.
