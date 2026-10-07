# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-10-07 12:05, in .

**Me:** how to print a statement in python

**Tutor:**

Printing a statement in Python is done with the `print()` function.

```python
# TODO: print the sentence "Hello, marketers!"
print()
```

What is the only thing you must put inside the parentheses of `print()`?

---
## 2026-10-07 14:10, in .

**Me:** how to remove a item from a dictionary in python

**Tutor:**

Concept: Removing an item from a dictionary by its key.

```python
# Toy dictionary
campaign = {
    "id": 101,
    "name": "Summer Sale",
    "budget": 5000,
    "status": "active"
}

# TODO: Remove the key "budget" from the dictionary
# TODO: Print the updated dictionary

```

Question: Which method removes a key-value pair from a dictionary when you know the key?

---
## 2026-10-07 14:21, in .

**Me:** how to save a list of names in python

**Tutor:**

Storing a list of names in Python.
```python
# Create an empty list
names = []

# Add names one by one
names.append("alpha")
names.append("beta")
names.append("gamma")
```
What function adds a single item to a list?

---
## 2026-10-07 16:30, in .

**Me:** What is the difference between strip(), upper(), lower(), and title() in Python strings? Please explain with a simple example.

**Tutor:**

String case and whitespace helpers.

`strip()` removes leading and trailing whitespace.
`upper()` converts every character to uppercase.
`lower()` converts every character to lowercase.
`title()` capitalizes the first letter of every word.

Pattern:

```python
text = "  marketing data  "

print(text.strip())   # TODO: what does this print?
print(text.upper())   # TODO: what does this print?
print(text.lower())   # TODO: what does this print?
print(text.title())   # TODO: what does this print?
```

Which function changes the string in-place instead of returning a new string?

---
## 2026-10-07 16:31, in .

**Me:** Why do I need to save sentence.strip() in a new variable? Does strip() change the original sentence?

**Tutor:**

The concept: strings in Python are immutable, so methods like strip() return a new string instead of changing the original.

```python
sentence = "  hello  "
clean = sentence.strip()  # TODO: what is the value of clean?
```

Question: after running the code above, is the value of sentence still "  hello  " or has it become "hello"?

---
## 2026-10-07 20:26, in .

**Me:** I used strip(), lower(), upper(), and swapcase() in Exercise 2.1. Why does strip() remove the spaces at both ends, but lower(), upper(), and swapcase() keep the spaces? Please explain it using beginner-friendly Python.

**Tutor:**

String methods that change the case (lower, upper, swapcase) only affect letters.
Whitespace characters (spaces, tabs, newlines) are not letters, so they stay unchanged.

Pattern on toy data:

```python
text = "  PyThOn 123! "
cleaned = text.strip()          # removes spaces at both ends
lowered = cleaned.lower()       # changes letters to lower case
uppered = cleaned.upper()       # changes letters to upper case
swapped = cleaned.swapcase()    # swaps upper to lower and vice-versa
```

Question: Which string method only removes whitespace, and which methods only change the case of letters?
