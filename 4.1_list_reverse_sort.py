"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:4.0[2, 3, 4, 5]I change to[4, 2, 5, 3]
# 2. Process:The program displays the list in four different orders without changing the original list.
# 3. Out:Four different orders of the list and the original list at the end.
# 4. My four orders, and which ones modify the original:modified rather than copied?
# I chose the original order, reversed order, ascending order, and descending order.
# None of them modifies the original list because I create new lists for the changed orders.


# Your code below


# This is my original list from Exercise 4.0.
my_list = [4, 2, 5, 3]

# Display the list in its original order.
print("Original order:", my_list)

# Create a new list in reversed order.
reversed_list = my_list[::-1]
print("Reversed order:", reversed_list)

# Create a new list in ascending order.
ascending_list = sorted(my_list)
print("Ascending order:", ascending_list)

# Create a new list in descending order.
descending_list = sorted(my_list, reverse=True)
print("Descending order:", descending_list)

# Display the original list again to check that it has not changed.
print("Original list at the end:", my_list)

# CHECK IT YOURSELF
# My original list was [4, 2, 5, 3].
# The program displayed four different orders.
# The last output was [4, 2, 5, 3].
# It is the same as my original list, so the original list was not changed.