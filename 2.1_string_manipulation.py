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

# 1. In:A sentence entered by the user.
# 2. Process:
# The program uses four string methods to transform the sentence:strip(), lower(), upper(), and swapcase().
# 3. Out:Four different versions of the user's sentence are displayed.
# 4. My four transformations, and when each is useful:
#strip(): removes extra spaces at the beginning and end of text.
#lower(): makes all letters lowercase, useful for comparing text.
#upper(): makes all letters uppercase, useful for headings or emphasis.
#swapcase(): changes uppercase letters to lowercase and lowercase letters touppercase, useful for seeing how letter cases change.


# Your code below
# Ask the user to enter a sentence.

user_input = input("Enter a sentence: ")

stripped_text = user_input.strip()

print("Stripped:", stripped_text)

# Change all letters to lowercase.

lower_text = user_input.lower()

print("Lowercase:", lower_text)

# Change all letters to uppercase.

upper_text = user_input.upper()

print("Uppercase:", upper_text)

# Change uppercase letters to lowercase and lowercase letters to uppercase.

swapped_text = user_input.swapcase()

print("Swapcase:", swapped_text)