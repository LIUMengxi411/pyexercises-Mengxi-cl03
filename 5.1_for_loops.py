"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A list of names.
# 2. Process:A for loop goes through each name and finds its position and length.
# 3. Out:One line for each name showing the name, its position, and its length.
# 4. What I compute for each item, and why it is worth showing:
# I computed the length of each name.
# The reader learns the name's position in the list and how many letters it has.


# Your code below
# Go through every name in the list.
names = ["Alice", "Bob", "Trump", "John", "Mickey", "Wick", "Tom", "Jerry"]
for position in range(len(names)):

    name = names[position]

    # Calculate the length of each name.

    name_length = len(name)

    # Display the position, name, and length.

    print("Position:", position + 1, "- Name:", name, "- Length:", name_length)
## CHECK IT YOURSELF
# My list has 8 items.
# The program printed 8 lines, one line for each name.
# Each line shows the name, its position, and its length.
# The number of output lines is the same as the number of items in my list.