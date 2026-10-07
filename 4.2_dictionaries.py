"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:Information about a person: name, age, occupation, city, and salary.
# 2. Process:The program stores the five pieces of information in a dictionary.
# 3. Out:The program displays the information stored in the dictionary.
# 4. My object, my five fields, and why those:My object is a person. My five fields are name, age, occupation, city, and salary.
# I chose them because they describe basic personal and work information.


# Your code below
name="John Joe"
age=30
occupation="Software Engineer"
city="New York"
salary=50000

print("Name:"+name)
print("Age:"+str(age))
print("Occupation:"+occupation)
print("City:"+city)
print("Salary:$"+str(salary))

person = {
    "name":name,
    "age":age,
    "occupation": occupation,
    "city":city,
    "salary":salary
}

#print the dictionary
print("Person dictionary:", person)

#update the age field
person["age"]=51

#print the updated dictionary
print("Updated person dictionary:",person)

#remove the salary field
salary = person.pop("salary")

#print the dictionary after removing the salary field
print("Person dictionary after removing salary field:", person)
print("Removed salary:", salary)