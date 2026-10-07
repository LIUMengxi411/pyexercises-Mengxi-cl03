"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My four transformations, and when each is useful:


# Your code below
# 1. What goes in?

# A sentence entered by the user.

# 2. What happens to it?

# The program applies four different string transformations to the sentence.

# 3. What comes out?

# Four different versions of the user's sentence.

# 4. My four transformations:

# strip() removes spaces from the beginning and end, which is useful for cleaning user input.

# upper() changes all letters to uppercase, which is useful for emphasis.

# lower() changes all letters to lowercase, which is useful for standardizing text.

# title() capitalizes the first letter of each word, which is useful for titles or names.


sentence = input("Enter a sentence: ")

stripped_sentence = sentence.strip()
uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()
title_sentence = sentence.title()

print("Stripped:", stripped_sentence)
print("Uppercase:", uppercase_sentence)
print("Lowercase:", lowercase_sentence)
print("Title:", title_sentence)


# Test results:

# strip(): The result was what I expected because the spaces at both ends were removed.

# upper(): The result was what I expected because all letters became uppercase.

# lower(): The result was what I expected because all letters became lowercase.

# title(): The result was what I expected because the first letter of each word became uppercase.