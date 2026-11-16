"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""


"""
Exercise 7.0 - Collecting data and saving it

WHAT THE PROGRAM MUST DO
Ask the user for the information needed to record one entry,
then save it to a CSV file. Running the program twice must
produce two entries, not overwrite the first.

ANSWER THESE FIRST

1. What goes in?
The user enters their first name, last name, date of birth,
and student number.

2. What happens to it?
The program collects the information and checks that no
field is empty. It then saves the information to a CSV file.
If the file is new, the program writes the header first.
New records are added without deleting previous records.

3. What comes out?
File name: student_records.csv
Columns: First Name, Last Name, Date of Birth, Student Number

4. Which columns did you choose, and what would you
actually do with this file once it has 200 rows in it?
I chose these four columns because they contain basic
student information. With 200 rows, I could organize
student records and search for a student using their
student number.

WHAT THE AI CANNOT KNOW
I chose the columns based on the information I wanted
to collect. I decided to write the header only when the
file is new and ask again if the user enters an empty value.

CHECK IT YOURSELF
Run the program three times with different values.
The CSV file should contain three records and one header.

DELIVERABLE
This Python file and the CSV file it produces.
"""

# Import the modules needed to save data
import csv
import os

# Name of the output file
filename = "student_records.csv"

# Ask the user for information
print("Please fill in the following details:")

first_name = input("First Name: ").strip()
while first_name == "":
    print("This field cannot be empty.")
    first_name = input("First Name: ").strip()

last_name = input("Last Name: ").strip()
while last_name == "":
    print("This field cannot be empty.")
    last_name = input("Last Name: ").strip()

birth = input("Date of Birth (DD/MM/YYYY): ").strip()
while birth == "":
    print("This field cannot be empty.")
    birth = input("Date of Birth (DD/MM/YYYY): ").strip()

student_number = input("Student Number: ").strip()
while student_number == "":
    print("This field cannot be empty.")
    student_number = input("Student Number: ").strip()

# Check if the file is new or empty
file_is_new = (
    not os.path.exists(filename)
    or os.path.getsize(filename) == 0
)

# Open the CSV file in append mode
with open(filename, "a", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Write the header only once
    if file_is_new:
        writer.writerow([
            "First Name",
            "Last Name",
            "Date of Birth",
            "Student Number"
        ])

    # Add the new student information
    writer.writerow([
        first_name,
        last_name,
        birth,
        student_number
    ])

print("Data saved successfully!")
