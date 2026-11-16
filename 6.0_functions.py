"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of numbers.
# 2. Process: Add all numbers in the list.
# 3. Out: The total sum of the numbers.
# 4. My function is called calculate_list_sum.
# I use return because the result can be used again.
# Print only shows the result on the screen.

# Your code below

# My list from exercise 4.0
list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]

def calculate_list_sum(numbers):
    sum_result = 0
    for num in numbers:
        sum_result = sum_result + num
    return sum_result

print("Result 1:", calculate_list_sum(list_of_numbers))
print("Result 2:", calculate_list_sum(list_of_numbers[:5]))
print("Result 3:", calculate_list_sum(list_of_numbers[5:]))

# Test with an empty list
print("Empty list:", calculate_list_sum([]))

# The empty list returns 0.
# This is acceptable because there are no numbers to add.
