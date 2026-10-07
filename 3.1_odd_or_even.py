"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A number N entered by the user.
# 2. Process:The program checks every number from 1 to N and decides if it is odd or even.
# 3. Out:The program displays each number and says whether it is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
#   If the user enters 0, the program will display a message saying N must be positive.

#    If the user enters a negative number, the program will display the same message.

#    If the user enters 5000, the program will display a message saying the number is too large.

# Your code below
# Ask the user to enter a number.

N = int(input("Enter a number: "))

# Check if the number is zero or negative.

if N <= 0:

    print("Please enter a positive number.")

# Check if the number is too large.

elif N >= 5000:

    print("The number is too large.")

# If the number is valid, check every number from 1 to N.

else:

    for number in range(1, N + 1):

        # If the remainder after dividing by 2 is 0, the number is even.

        if number % 2 == 0:

            print(number, "is even.")

        # Otherwise, the number is odd.

        else:

            print(number, "is odd.")
## CHECK IT YOURSELF
#
# Test 1: N = 6
# Result: 1, 3, and 5 were odd. 2, 4, and 6 were even.
# There were three odd numbers and three even numbers, as expected.
#
# Test 2: N = 0
# Result: The program displayed "Please enter a positive number."
# This is what I expected.
#
# Test 3: N = -4
# Result: The program displayed "Please enter a positive number."
# This is what I expected.
#
# Test 4: N = 5000
# Result: The program displayed "The number is too large."
# This is what I expected.
